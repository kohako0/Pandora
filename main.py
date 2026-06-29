from core.llm import ask_llm
from core.agent import handle_response
from core.memory import add_user, add_assistant


def main():

    print("Local Agent gestartet\n")

    while True:

        user = input("You: ")

        if user.lower() in ["exit", "quit"]:
            break

        response = ask_llm(user)

        final = handle_response(response)

        print("\nAgent:", final, "\n")

        add_user(user)
        add_assistant(final)


if __name__ == "__main__":
    main()