# Description
Simple example web app + client showing Model Context Protocol server mounted on an existing fastapi server

[Model Context Protocol](https://github.com/modelcontextprotocol/python-sdk)

[FastAPI Mounting](https://fastapi.tiangolo.com/advanced/sub-applications/)

Files

./src/main.py -> main fastapi server app

./src/mcp.py -> mcp sub server app logic

./client/client.py -> sample client showing some communication logic using mcp client lib

# Set up

## Using Docker to start server

```bash
docker build -t fastapi-mcp .
docker run -p 8000:8000 --net=host fastapi-mcp
```

## Set up python environment & run client

```
pip install -r requirements.txt
python client/client.py

# to run server as well without docker
uvicorn src.main:app
```

# Known Issues

## MCP server can only be mounted on root '/'
[GitHub Issue](https://github.com/modelcontextprotocol/python-sdk/issues/585)

Limitations on MCP python sdk that currently only allows for MCP server to work when mounted on root /

