POST_SCHEMA = {
    "type": "Object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string", "enum": ["POST"]}

    },
    "required": ["id"]

}
# {'id': 1, 'title': 'Post 1'}
