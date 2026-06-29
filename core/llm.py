from llama_cpp import Llama
from lib.config import LLAMA_SETTINGS
from core.messages import build_messages

llm = Llama(**LLAMA_SETTINGS)


def ask_llm(user_input):

    messages = build_messages(user_input)

    stream = llm.create_chat_completion(
        messages=messages,
        temperature=0.7,
        max_tokens=512,
        stream=True
    )

    text = ""

    for chunk in stream:

        delta = chunk["choices"][0]["delta"].get("content", "")

        if delta:
            print(delta, end="", flush=True)
            text += delta

    print()

    return text