from typing import Union

from fastapi import FastAPI
from .mcp import mcp

app = FastAPI()

web_app = FastAPI()

@web_app.get("/")
def read_root():
    return {"Hello": "World"}


@web_app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# TODO https://github.com/modelcontextprotocol/python-sdk/issues/585
# because the python sse client has a bug in the url construction
# the mounting needs to be '/' otherwise the post request to /messages would break

# mounts the /sse and /messages/?session_id=<session_id> endpoints for the mcp server
# Order sensitive, setting mcp to root first would cause the /web endpoints to be not discoverable
app.mount("/web", web_app)
app.mount("/", mcp.sse_app())
