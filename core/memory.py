history = []


def add_user(text):
    history.append({
        "role": "user",
        "content": text
    })


def add_assistant(text):
    history.append({
        "role": "assistant",
        "content": text
    })


def get_history():
    return history