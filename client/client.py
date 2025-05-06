from mcp import ClientSession
from mcp.client.sse import sse_client


async def run():
    async with sse_client(url="http://localhost:8000/sse") as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

            # List available prompts
            prompts = await session.list_prompts()

            print(prompts)

            # List available resources
            resources = await session.list_resources()

            print(resources)

            # List available tools
            tools = await session.list_tools()

            print(tools)

            # Get a particular prompt from the example server
            prompt = await session.get_prompt(
                "review_code", arguments={"code": "sum = 1 + 2"}
            )
            print(prompt)

            # call a tool
            result = await session.call_tool("add", arguments={"a": 3, "b": 5})
            print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())