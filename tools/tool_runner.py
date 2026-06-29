from tools.echo import run as echo


TOOLS = {
    "echo": echo
}


def run_tool(tool_name, args):

    print(f"[TOOL] {tool_name} -> {args}")

    if tool_name not in TOOLS:
        return "Tool existiert nicht."

    return TOOLS[tool_name](args)