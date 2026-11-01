# 🚀 NexoraAI Cloud Platform

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

> A next-generation, scalable cloud platform designed for deploying, managing, and scaling artificial intelligence models and microservices with enterprise-grade security and real-time monitoring.

---

## 🔗 Live Links & Demo

* **Public Application:** [https://nexoraai-cloud-platform.vercel.app](https://nexoraai-cloud-platform.vercel.app)
* **API Documentation:** [https://api.nexoraai-cloud.com/docs](https://api.nexoraai-cloud.com/docs)
* **System Status:** [https://status.nexoraai-cloud.com](https://status.nexoraai-cloud.com)

---

## 🏗 System Architecture

```text
                               +-------------------+
                               |   Client/User     |
                               +---------+---------+
                                         |
                                         v
                         +---------------+---------------+
                         |  API Gateway / Edge Router    |
                         |     (Rate Limiting & Auth)    |
                         +---------------+---------------+
                                         |
                  +----------------------+----------------------+
                  |                                             |
                  v                                             v
       +----------+----------+                       +----------+----------+
       |   Frontend Service  |                       |   Core Microservices    |
       |  (Next.js Dashboard)|                       |    (Node.js / Express)  |
       +---------------------+                       +----------+----------+
                                                                |
                                             +------------------+------------------+
                                             |                                     |
                                             v                                     v
                                  +----------+----------+               +----------+----------+
                                  |  AI Model Engine    |               | PostgreSQL & Redis  |
                                  | (FastAPI Inference) |               | (Data & Cache Store)|
                                  +---------------------+---------------+---------------------+

🧰 Detailed Tooling & Ecosystem Explanation
1. User Interface & Operations Dashboard
 * Next.js (v14+): Serves as the web framework utilizing Server-Side Rendering (SSR) and Server Components to deliver fast loading speeds and optimal SEO performance.
 * TypeScript: Provides strict type checking across the entire codebase to reduce runtime errors and streamline developer workflows.
 * Tailwind CSS & Shadcn UI: A flexible styling setup that generates a lightweight design system with fully accessible UI elements.
 * Recharts: Powers the analytical dashboard by rendering interactive, real-time charts for monitoring server resources, API response times, and model usage metrics.
2. Core API Gateway & Backend Services
 * Node.js & Express.js: Operates as the main backend gateway handling asynchronous client requests, middleware integration, user authentication, and route orchestration.
 * FastAPI (Python): Powers dedicated AI microservices, leveraging Python’s native ecosystem for high-speed machine learning inference and execution.
 * JWT & OAuth 2.0: Handles identity verification, encrypted token generation, role-based access control (RBAC), and user session security.
3. Database, Caching & Message Queue Layer
 * PostgreSQL: Acts as the primary relational database system, storing structured data such as user accounts, API key registries, project metadata, and deployment configurations.
 * Redis: Serves as a high-throughput in-memory data store for handling dynamic API rate-limiting, active session storage, dynamic caching, and async job queues.
 * Prisma / TypeORM: Provides object-relational mapping (ORM) for schema migrations, database queries, and type safety across backend models.
4. Machine Learning & Inference Runtime
 * PyTorch: Provides the execution runtime for deep learning models, model loading, and GPU acceleration.
 * Hugging Face Transformers: Integrates pre-trained natural language processing (NLP) and vision models directly into inference pipelines.
 * ONNX Runtime: Optimizes machine learning models into high-performance binaries to enable faster, cross-platform execution.
5. Cloud Infrastructure & DevOps Pipeline
 * Docker & Docker Compose: Encapsulates dependencies inside container images, guaranteeing consistent development, testing, and production environments.
 * Kubernetes (K8s): Manages container orchestration, automated deployments, horizontal pod scaling, and self-healing workloads.
 * Vercel & AWS (EC2/S3): Hosts frontend user dashboards on Vercel's edge network while executing heavy backend compute and model storage on Amazon Web Services.
 * GitHub Actions: Automates continuous integration and deployment (CI/CD) workflows for automated testing, building, and environment deployment.
🌟 Key Features
 * 🤖 Automated Model Deployment: Deploy open-source LLMs and custom ML algorithms using automated containerization.
 * ⚡ Serverless Auto-scaling: Dynamic compute allocation that scales infrastructure automatically based on real-time request volume.
 * 📊 Live Telemetry & Analytics: Intuitive monitoring for latency, CPU/GPU utilization, bandwidth, and API success rates.
 * 🛡️ Secure Key Scoping: Issue and revoke API keys with granular scopes, expiration dates, and configurable rate limits.
📦 Getting Started & Installation
Prerequisites
Make sure the following dependencies are installed locally:
 * Node.js (v18.0.0 or higher)
 * Python (v3.10 or higher)
 * Docker Desktop
 * Git
🚀 Step-by-Step Setup
1. Clone the Repository
git clone [https://github.com/Nisarg-Modi/nexoraai-cloud-platform.git](https://github.com/Nisarg-Modi/nexoraai-cloud-platform.git)
cd nexoraai-cloud-platform

2. Environment Configuration
Create a .env file in the project root:
# Application Settings
PORT=5000
NODE_ENV=development

# Database Connections
DATABASE_URL=postgresql://postgres:password@localhost:5432/nexoraai_db
REDIS_URL=redis://localhost:6379

# Authentication & Security
JWT_SECRET=super_secret_jwt_key_change_in_production
API_KEY_PREFIX=nx_live_

# Public Frontend Variables
NEXT_PUBLIC_API_URL=http://localhost:5000/api

3. Run with Docker Compose (Recommended)
docker-compose up --build

4. Run Services Individually (Manual Setup)
Start Backend Gateway:
cd backend
npm install
npm run dev

Start AI Inference Service:
cd ml-services
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

Start Frontend Application:
cd frontend
npm install
npm run dev

📂 Project Structure
nexoraai-cloud-platform/
├── .github/              # GitHub Actions CI/CD workflows
├── backend/              # Express API gateway & core business logic
├── frontend/             # Next.js web application and operational dashboards
├── ml-services/          # FastAPI Python services for AI inference
├── docker/               # Dockerfiles and environment setups
├── docker-compose.yml    # Development stack container composition
├── LICENSE               # Open-source license terms
└── README.md             # Project documentation

🤝 Contributing
Contributions make the open-source community an incredible place to learn, inspire, and create. Any contributions you make are greatly appreciated.
 * Fork the Repository
 * Create your Feature Branch (git checkout -b feature/AmazingFeature)
 * Commit your Changes (git commit -m 'Add some AmazingFeature')
 * Push to the Branch (git push origin feature/AmazingFeature)
 * Open a Pull Request
📄 License
Distributed under the MIT License. See LICENSE for more information.
<p align="center">
Crafted with ❤️ by <a href="https://github.com/Nisarg-Modi">Nisarg Modi</a>
</p>


