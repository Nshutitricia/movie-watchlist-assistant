TOOLS = [
    {
        "name": "add_movie",
        "description": "Add a movie to the user's watchlist. Rejects duplicates.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "The movie title"},
                "genre": {"type": "string", "description": "The movie's genre"},
            },
            "required": ["title", "genre"],
        },
    },
    {
        "name": "list_movies",
        "description": "List all movies currently on the user's watchlist.",
        "input_schema": {
            "type": "object",
            "properties": {},
        },
    },
    {
        "name": "remove_movie",
        "description": "Remove a movie from the user's watchlist by title.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "The movie title to remove"},
            },
            "required": ["title"],
        },
    },
    {
        "name": "pick_random_movie",
        "description": "Pick a random movie from the user's watchlist as a recommendation.",
        "input_schema": {
            "type": "object",
            "properties": {},
        },
    },
]