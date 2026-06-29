from prompts.systemprompt import SYSTEM_PROMPT
from core.memory import get_history


def build_messages(user_input):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(get_history())

    messages.append({
        "role": "user",
        "content": user_input
    })

    return messages