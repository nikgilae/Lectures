import os
import dotenv
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from openai import OpenAI
from settings import OpenAISettings

dotenv.load_dotenv(dotenv.find_dotenv())

MODEL_NAME = "ai-sage/GigaChat3-10B-A1.8B"

def get_client() -> OpenAI:
    settings = OpenAISettings()
    client = OpenAI(
        api_key=settings.openai_api_key.get_secret_value(),
        base_url=str(settings.openai_base_url),
    )
    return client

def chat_loop():
    client = get_client()
    console = Console()
    
    messages = [
        {
            "role": "system",
            "content": "Ты русский православный батюшка матершинник, который составляет молитвы людям с кучей мата и брани, и эмодзи",
        },
    ]

    console.print("[bold cyan]Начало чата[/bold cyan]")
    console.print("Доступные команды: /exit, /clear, /system <новый промпт>")

    while True:
        user_input = console.input("Вы: ")

        if user_input.lower() == "/exit":
            console.print("\n[bold red]Чат завершён.[/bold red]")
            break

        if user_input.lower() == "/clear":
            messages = [msg for msg in messages if msg["role"] == "system"]
            console.print("[bold yellow]История чата очищена.[/bold yellow]")
            continue

        if user_input.lower().startswith("/system "):
            new_system_prompt = user_input[len("/system "):].strip()
            # Replace existing system message
            for i, msg in enumerate(messages):
                if msg["role"] == "system":
                    messages[i] = {"role": "system", "content": new_system_prompt}
                    break
            else: # if no system message exists
                messages.insert(0, {"role": "system", "content": new_system_prompt})
            console.print(f"[bold yellow]Системный промпт изменен на: '{new_system_prompt}'[/bold yellow]")
            continue

        messages.append({"role": "user", "content": user_input})

        with console.status("[bold green]Модель думает...[/bold green]"):
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
            )
        
        assistant_reply = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_reply})

        md = Markdown(assistant_reply)
        console.print(
            Panel(
                md,
                title="[bold green]Ответ модели[/bold green]",
                border_style="green",
                padding=(1, 2),
            )
        )
        console.print()

if __name__ == "__main__":
    chat_loop()