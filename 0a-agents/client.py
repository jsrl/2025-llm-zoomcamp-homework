import asyncio
from fastmcp import Client

async def main():
    print("Connecting to server...")
    async with Client("weather_server.py") as mcp_client:
        print("Connected. Fetching tools...")
        tools = await mcp_client.list_tools()
        print("Tools found:", tools)

if __name__ == "__main__":
    asyncio.run(main())
