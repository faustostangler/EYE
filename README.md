Goal: Explain what the project is and how to run it in under 5 minutes.

Structure:

1. Project Title & Badges (CI Status, Python Version, License).
2. Short Description: A 1-paragraph "elevator pitch" of what EYE is (Clinical Semantic Extraction + RAG).
3. Key Features: Bullet points (e.g., Deterministic Extraction, Local Inference, SOTA Stack).
4. Service Topology: (The text we just approved).
Include a simple ASCII or Mermaid diagram here if possible.
5. Prerequisites:
Docker & Docker Compose.
NVIDIA Drivers (if using GPU).
uv (if using local Python management).
6. Quick Start (The "Happy Path"):
Clone repo.
cp .env.example .env
docker compose up -d
Curl example to test health.
7. Development Workflow:
How to run in Dev mode (docker compose -f ...).
How to attach the debugger.
8. Project Structure: A brief tree view of the folders.
This is project root as so far
EYE/
├── .github/                   # CI/CD Workflows
├── app/                       # Source Code
├── docs/                      # Extract images/diagrams here
│   └── diagrams/
├── .env.example               # Config Template
├── .gitignore
├── ARCHITECTURE.md            # Technical Deep Dive
├── CHANGELOG.md               # Version History
├── CONTRIBUTING.md            # Dev Guidelines
├── docker-compose.yml         # Production Orchestration
├── docker-compose.dev.yml     # Dev Overrides
├── LICENSE
├── pyproject.toml             # Python Dependencies (Single Source)
├── README.md                  # Entry Point
└── uv.lock                    # Deterministic Lockfile
