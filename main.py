from llama_cpp import Llama
from config import *
import time

MODEL = MODEL_PATH



llm = Llama(**LLAMA_SETTINGS)





history = []


def build_messages(user_input):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_input})
    return messages


def ask_llm(user_input):
    messages = build_messages(user_input)

    stream = llm.create_chat_completion(
        messages=messages,
        temperature=0.7,
        max_tokens=512,
        stream=True
    )

    full_text = ""

    for chunk in stream:
        delta = chunk["choices"][0]["delta"].get("content", "")
        if delta:
            print(delta, end="", flush=True)
            full_text += delta

    print()
    return full_text

def run_tool(tool_name, args):
    print(f"[TOOL REQUEST] {tool_name} -> {args}")


    if tool_name == "echo":
        return args

    return f"Tool '{tool_name}' nicht implementiert."


def handle_response(response):
    if response.startswith("TOOL:"):
        lines = response.split("\n")
        tool_line = lines[0]
        args_line = lines[1] if len(lines) > 1 else ""

        tool_name = tool_line.replace("TOOL:", "").strip()
        args = args_line.replace("ARGS:", "").strip()

        result = run_tool(tool_name, args)
        return f"[TOOL RESULT]: {result}"

    return response




def main():
    print("Local Agent gestartet (llama.cpp)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        response = ask_llm(user_input)
        final_output = handle_response(response)

        print("\nAgent:", final_output, "\n")

        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": final_output})





if __name__ == "__main__":
    main()