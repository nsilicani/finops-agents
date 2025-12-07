import asyncio
from toolbox_core import ToolboxClient


async def main():
    # Replace with the actual URL where your Toolbox service is running
    async with ToolboxClient("http://127.0.0.1:5000") as toolbox:
        gcp_tool = await toolbox.load_tool("get_cost_by_service")
        result = await gcp_tool(invoice_month="202512")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
