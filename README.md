# FinOps Agent
A multi-agent system with FinOps capabilities.

## Usage
### Toolbox for Databases
To spin up the toolbox, pull the image
```powershell
docker pull us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:0.22.0
```
and then run the container. In powershell (from `finops-agents\gcp_agent`):
```powershell
docker run -p 5000:5000 `
  --rm `
  --name toolbox `
  -e GOOGLE_APPLICATION_CREDENTIALS="/gcp_key.json" `
  -v "$(Get-Location)\gcp_key.json:/gcp_key.json" `
  -v "$(Get-Location)\tools.yaml:/app/tools.yaml" `
  us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:0.22.0 `
  --tools-file "/app/tools.yaml" `
  --address 0.0.0.0
```
In bash (from `finops-agents\gcp_agent`):
```bash
docker run -p 5000:5000 \
  --name toolbox \
  -e GOOGLE_APPLICATION_CREDENTIALS="/gcp_key.json" \
  -v "$(pwd)/gcp_key.json:/gcp_key.json" \
  -v "$(pwd)/tools.yaml:/app/tools.yaml" \
  us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:0.22.0 \
  --tools-file "/app/tools.yaml" \
  --address 0.0.0.0
```
### Start the agents
The agent assumes that an GCP MCP Server is reachable at endpoint specified in `GCP_MCP_URL` environmental variable.

## Debugging
In this section we report the outcome of the debugging session, along with some possible solutions.

| Request | Response | Solution |
|--------|----------|----------|
| Analyse costs for project `<project_id>` for the last 30 day | I'm sorry, I was unable to retrieve the billing information for the project `<project_id>`. The Cloud Billing API might not be enabled for this project, or I might not have the necessary permissions. | Ensure the Cloud Billing API is enabled and that I have the correct permissions, then try again. |
| What are my current billing costs for project `<project_id>` in this month? | model_version: "gemini-2.5-flash"<br>finish_reason: "MALFORMED_FUNCTION_CALL"<br>error_code: "MALFORMED_FUNCTION_CALL" | N/A |
| What are my billing costs for the month of November 2025? | I cannot provide billing costs for November 2025 as it is in the future. I can only access billing data for past or the current month. | The model uses an incorrect internal mechanism to determine the current date.<br><br>The model explains that it relies on a system-provided current date to classify requests as past, present, or future. In this case, it incorrectly treated November 2025 as a future date.<br><br>Workaround: explicitly provide the current date (e.g., “Today is 28 December 2025, hence you can retrieve cost billing data for November 2025”). This allows the model to answer correctly.<br><br>Reference: https://gist.github.com/tanaikech/e5114194e059153de2b0511ca18ba4bd |



## Resources
- [GCP Cost Agent](https://github.com/aryanirani123/gcp-cost-agent/tree/main)
- [ADK MCP A2A Crash Course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)
- [Spin up Toolbox server using Docker](https://github.com/googleapis/genai-toolbox)