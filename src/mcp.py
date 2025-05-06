from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Example")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def square(a: int) -> int:
    """Square a number"""
    return a * a

@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
