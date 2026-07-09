from anthropic import Anthropic
from sqlmodel import Session

from app.config import ANTHROPIC_API_KEY, CLAUDE_MODEL
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.tools.tool_definitions import TOOLS
from app.services import watchlist_service as ws

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def run_tool(tool_name: str, tool_input: dict, session: Session):

    if tool_name == "add_movie":
        movie = ws.add_movie(session, tool_input["title"], tool_input["genre"])
        if movie is None:
            return f"'{tool_input['title']}' is already on the watchlist."
        return f"Added '{movie.title}' ({movie.genre}) to the watchlist."

    if tool_name == "list_movies":
        movies = ws.list_movies(session)
        if not movies:
            return "The watchlist is empty."
        return "\n".join(f"- {m.title} ({m.genre})" for m in movies)

    if tool_name == "remove_movie":
        movie = ws.remove_movie(session, tool_input["title"])
        if movie is None:
            return f"'{tool_input['title']}' was not found on the watchlist."
        return f"Removed '{movie.title}' from the watchlist."

    if tool_name == "pick_random_movie":
        movie = ws.pick_random_movie(session)
        if movie is None:
            return "The watchlist is empty, nothing to pick."
        return f"Random pick: '{movie.title}' ({movie.genre})"

    return f"Unknown tool: {tool_name}"


def get_response(messages: list[dict], session: Session) -> str:

    while True:
        response = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )


        if response.stop_reason != "tool_use":
            text_blocks = [b.text for b in response.content if b.type == "text"]
            return "\n".join(text_blocks)

        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result_text = run_tool(block.name, block.input, session)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result_text,
                })

        messages.append({"role": "user", "content": tool_results})