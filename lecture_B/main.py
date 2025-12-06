import os
from dotenv import load_dotenv
from duckduckgo_search import DDGS
from openai import OpenAI
from settings import OpenAISettings

# --- ШАГ 0: Настройка (ТВОЙ СПОСОБ) ---

# Загружаем переменные окружения из файла .env
load_dotenv()

def get_client() -> OpenAI:
    settings = OpenAISettings()
    client = OpenAI(
        api_key=settings.openai_api_key.get_secret_value(),
        base_url=str(settings.openai_base_url),
    )
    return client

# --- УЗЕЛ 1: ИНСТРУМЕНТ ПОИСКА (БЕЗ ИЗМЕНЕНИЙ) ---
def search_duckduckgo(query: str) -> str:
    """
    Выполняет поиск в DuckDuckGo и возвращает объединенный текст из нескольких результатов.
    """
    print(f"🔎 Выполняю поиск по запросу: '{query}'...")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            if not results:
                print("⚠️ Поиск не дал результатов.")
                return "Поиск не дал результатов."

        context = " ".join([result['body'] for result in results])
        print("✅ Поиск завершен. Получен контекст.")
        return context
    except Exception as e:
        print(f"❌ Ошибка при поиске: {e}")
        return f"Ошибка при выполнении поиска: {e}"

# --- УЗЕЛ 2: ИНСТРУМЕНТ ОБРАБОТКИ LLM (АДАПТИРОВАН) ---
def summarize_with_llm(text_to_summarize: str, user_query: str) -> str:
    """
    Отправляет текст в твою LLM для получения ответа на основе этого текста.
    """
    print(f"🤖 Отправляю данные в модель для анализа...")
    try:
        # Используем твою функцию для получения клиента
        client = get_client()
        
        # Промпт остается тем же
        messages = [
            {
                "role": "system",
                "content": "Ты — умный ассистент, который анализирует предоставленный текст и отвечает на вопрос пользователя строго на основе этого текста."
            },
            {
                "role": "user",
                "content": f"""
                Проанализируй следующий текст, полученный из интернета:
                ---
                {text_to_summarize}
                ---
                Используя ТОЛЬКО этот текст, дай ясный и краткий ответ на мой вопрос: '{user_query}'
                """
            }
        ]
        
        # Вызываем модель, которую ты указал
        completion = client.chat.completions.create(
            # ВАЖНО: Указываем твою модель. Ты можешь поменять ее на любую другую.
            model="GigaChat/GigaChat-2-Max", 
            messages=messages
        )
        
        answer = completion.choices[0].message.content
        print("✅ Модель успешно ответила.")
        return answer
            
    except Exception as e:
        print(f"❌ Ошибка при работе с LLM: {e}")
        return f"Ошибка при обращении к LLM: {e}"

# --- НАШ WORKFLOW (логика не меняется) ---
def run_workflow(query: str):
    """
    Запускает последовательное выполнение узлов нашего workflow.
    """
    print(f"\n🚀 Запускаю workflow для запроса: '{query}'")
    
    # Шаг 1: Поиск
    search_results = search_duckduckgo(query)
    
    # Шаг 2: Анализ
    if "Ошибка" not in search_results and "не дал результатов" not in search_results:
        final_answer = summarize_with_llm(search_results, query)
    else:
        final_answer = search_results

    # Шаг 3: Вывод
    print("\n--- ✨ Итоговый ответ ---")
    print(final_answer)
    print("------------------------\n")

# --- Запуск ---
if __name__ == "__main__":
    run_workflow("Как часто метеориты падают на землю ?")
