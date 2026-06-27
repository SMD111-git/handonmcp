import asyncio
from fastmcp import Client

async def main():
    async with Client("server/server.py") as client:
        result = await client.call_tool(
            "multiply",
            {"a": 5, "b": 3}
        )
        print(result.data)

asyncio.run(main())

async def main2():
    async with Client("server/server.py") as client:
        result = await client.call_tool(
            "add",
            {"a": 5, "b": 3}
        )
        print(result.data)

asyncio.run(main2())