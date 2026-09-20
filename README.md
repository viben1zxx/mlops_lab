# 🚀 MLOps FastAPI CI/CD Pipeline

## 📌 Project Overview
This repository demonstrates a foundational MLOps workflow. It features a Python FastAPI microservice that is fully containerized using Docker, with an automated Continuous Integration and Continuous Deployment (CI/CD) pipeline managed by GitHub Actions.

## 🛠️ Technology Stack
* **Framework:** FastAPI (Python 3.11)
* **Server:** Uvicorn
* **Containerization:** Docker
* **CI/CD Automation:** GitHub Actions
* **Version Control:** Git & GitHub

## ⚙️ CI/CD Pipeline Architecture
The automated workflow (`ci-cd.yml`) triggers on every push or pull request to the `main` branch. It performs the following quality gates:
1. **Environment Setup:** Provisions an Ubuntu runner and configures Python 3.11.
2. **Dependency Installation:** Upgrades `pip` and installs required packages from `requirements.txt`.
3. **Container Build:** Builds the Docker image from scratch (`mlops-fastapi:latest`) to ensure environment reproducibility.
4. **Integration Testing:** Deploys the container locally on port `8000`, waits for server initialization, and runs a health-check curl request to verify execution.

## 💻 Local Development Setup

To run this project locally on your machine, ensure you have Docker installed, then run the following commands:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/viben1zxx/mlops_lab.git](https://github.com/viben1zxx/mlops_lab.git)
   cd mlops_lab
