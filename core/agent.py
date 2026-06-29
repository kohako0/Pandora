from tools.tool_runner import run_tool


def handle_response(response):

    if not response.startswith("TOOL:"):
        return response

    lines = response.split("\n")

    tool = lines[0].replace("TOOL:", "").strip()
    args = ""

    if len(lines) > 1:
        args = lines[1].replace("ARGS:", "").strip()

    result = run_tool(tool, args)

    return f"[TOOL RESULT]: {result}"