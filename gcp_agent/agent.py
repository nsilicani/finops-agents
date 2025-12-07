from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

from .prompt import GCP_AGENT_PROMPT

# Initialize the toolbox client to connect to the tool server
toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

# Load the toolset defined in your tools.yaml
tools = toolbox.load_toolset("gcp-cost-agent-tools")

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
    tools=tools,
)
