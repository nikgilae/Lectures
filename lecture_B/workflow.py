import os
from dotenv import load_dotenv
from ddgs.ddgs import DDGS  # можешь оставить, но Agno уже сам использует ddgs
from settings import OpenAISettings

# --- Agno ---
from agno.agent import Agent
from agno.models.openai.like import OpenAILike

from agno.tools.duckduckgo import DuckDuckGoTools

# --- Настройка окружения ---
load_dotenv()


# --- Агент LLM на базе Agno ---
def build_qa_agent() -> Agent:
    """
    Создаём Agno-агента, который будет суммаризировать текст поиска.
    Используем OpenAILike, чтобы ходить в твой OpenAI-совместимый endpoint.
    """
    settings = OpenAISettings()

    model = OpenAILike(
        id="Qwen/Qwen3-Next-80B-A3B-Instruct",  # твоя модель
        api_key=settings.openai_api_key.get_secret_value(),
        base_url=str(settings.openai_base_url),
    )

    agent = Agent(
        name="SearchQAAssistant",
        model=model,
        system_message=(
            "Ты — умный ассистент, который анализирует предоставленный текст "
            "из поиска и отвечает на вопрос пользователя строго на основе этого текста."
        ),
        markdown=False,
    )
    return agent


# Инициализируем один раз, чтобы не создавать клиента на каждый запрос
qa_agent = build_qa_agent()

# Инструмент поиска от Agno (внутри использует ddgs)
duckduckgo_tool = DuckDuckGoTools()


# --- УЗЕЛ ПОИСКА (через Agno DuckDuckGoTools) ---
def search_duckduckgo(query: str) -> str:
    """
    Выполняет поиск с помощью DuckDuckGoTools из Agno.
    Под капотом используется ddgs, как и в твоём исходном решении.
    """
    print(f"🔎 Выполняю поиск по запросу: '{query}'...")
    try:
        # Agno-обёртка вокруг ddgs
        results = duckduckgo_tool.duckduckgo_search(query=query, max_results=3)

        if not results:
            print("⚠️ Поиск не дал результатов.")
            return "Поиск не дал результатов."

        # results — список словарей с полями вроде 'title', 'body', 'href'
        bodies = [r.get("body", "") for r in results if r.get("body")]
        context = " ".join(bodies)

        print(f"✅ Поиск завершен. Найдено {len(bodies)} результатов.")
        return context or "Поиск не дал результатов (нет текстовых сниппетов)."

    except Exception as e:
        print(f"❌ Критическая ошибка при поиске: {e}")
        return f"Ошибка при выполнении поиска: {e}"


# --- УЗЕЛ LLM (через Agno Agent) ---
def summarize_with_llm(text_to_summarize: str, user_query: str) -> str:
    """
    Отправляет текст в Agno-агента для получения ответа на основе этого текста.
    """
    print(f"🤖 Отправляю данные в модель для анализа...")

    # Если заранее видим, что поиск не удался — сразу отвечаем
    if not text_to_summarize or "Ошибка" in text_to_summarize or "не дал результатов" in text_to_summarize:
        print("⚠️ Пропускаю LLM, так как поиск завершился ошибкой или без результатов.")
        return "Не удалось найти информацию по вашему запросу."

    user_message = f"""
Проанализируй следующий текст, полученный из интернета:
---
{text_to_summarize}
---
Используя ТОЛЬКО этот текст, дай ясный и краткий ответ на мой вопрос: '{user_query}'
"""

    try:
        # Агент Agno сам ходит в твой OpenAI-совместимый backend
        response = qa_agent.run(user_message)
        answer = response.content
        print("✅ Модель успешно ответила.")
        return answer
    except Exception as e:
        print(f"❌ Ошибка при работе с LLM: {e}")
        return f"Ошибка при обращении к LLM: {e}"


# --- WORKFLOW (логика та же, но шаги теперь используют Agno) ---
def run_workflow(query: str):
    """
    Запускает последовательное выполнение узлов нашего pipeline.
    """
    print(f"\n🚀 Запускаю workflow для запроса: '{query}'")

    # Шаг 1: Поиск (Agno DuckDuckGoTools + ddgs)
    search_results = search_duckduckgo(query)

    # --- ОТЛАДКА: Смотрим, что нашел поисковик ---
    print("\n" + "=" * 20 + " ТЕКСТ ДЛЯ LLM " + "=" * 20)
    print(search_results)
    print("=" * 55 + "\n")
    # ---------------------------------------------

    # Шаг 2: Анализ (Agno Agent + OpenAILike)
    final_answer = summarize_with_llm(search_results, query)

    # Шаг 3: Вывод
    print("\n--- ✨ Итоговый ответ ---")
    print(final_answer)
    print("------------------------\n")


# --- Запуск ---
if __name__ == "__main__":
    run_workflow("Сколько лет Трампу ?")
