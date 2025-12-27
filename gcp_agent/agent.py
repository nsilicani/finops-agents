import os

from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

from dotenv import load_dotenv

from toolbox_core import ToolboxSyncClient

from .prompt import GCP_AGENT_PROMPT

load_dotenv()

# Initialize the toolbox client to connect to the tool server
toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

# Load the toolset defined in your tools.yaml
tools = toolbox.load_toolset("gcp-cost-agent-tools")

# GCP MPC deployed on Google Run
try:
    GCP_MCP_URL = os.environ["GCP_MCP_URL"]
except Exception:
    print("Please set GCP_MCP_URL in .env file")
    raise KeyError("Please set GCP_MCP_URL in .env file")
gcp_mcp = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=GCP_MCP_URL,
        timeout=120,
    ),
)


# Define the root agent
root_agent = Agent(
    name="GCPCostAgent",
    model="gemini-2.5-flash",
    description=(
        "An agent that provides insights into your Google Cloud Platform (GCP) costs "
        "by querying your billing data in BigQuery. It can retrieve total monthly "
        "costs and provide breakdowns of spending by project or by service."
    ),
    instruction=GCP_AGENT_PROMPT,
    tools=tools + [gcp_mcp],
)
