# FinOps Agent
A multi-agent system with FinOps capabilities.

## Usage
To spin up the toolbox, pull the image
```powershell
docker pull us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:0.22.0
```
and the run the container:
```bash
docker run -p 5000:5000 -v "$(pwd)\tools.yaml:/app/tools.yaml" -v "C:\path\to\gcp_key.json:/root/.config/gcloud/application_default_credentials.json" us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:0.22.0 --tools-file "/app/tools.yaml" --address 0.0.0.0
```
In powershell:
```powershell
docker run -p 5000:5000 `
  --name toolbox `
  -e GOOGLE_APPLICATION_CREDENTIALS="/gcp_key.json" `
  -v "$(Get-Location)\gcp_key.json:/gcp_key.json" `
  -v "$(Get-Location)\tools.yaml:/app/tools.yaml" `
  us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:0.22.0 `
  --tools-file "/app/tools.yaml" `
  --address 0.0.0.0
```
## Resources
- [GCP Cost Agent](https://github.com/aryanirani123/gcp-cost-agent/tree/main)
- [ADK MCP A2A Crash Course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)
- [Spin up Toolbox server using Docker](https://github.com/googleapis/genai-toolbox)