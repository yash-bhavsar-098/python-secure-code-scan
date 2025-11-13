# 🛡️ Python Secure Code Scanner

    A lightweight open-source Python security scanner designed to detect vulnerabilities in both local projects and GitHub repositories.  
    It uses **Bandit** for static code analysis and checks for **exposed secrets** in environment files, helping developers ensure their code is secure.

---

## 🚀 Features

- **🔍 Clone & Scan GitHub Repositories** — Automatically clones a GitHub repo for analysis.  
- **🧠 Python Code Analysis** — Uses Bandit to find common security vulnerabilities in Python code.  
- **🔑 Secrets Detection** — Scans `.env` and configuration files for exposed secrets (like API keys, tokens, etc.).  
- **📊 Report Generation** — Creates detailed scan reports in both text and JSON formats inside the `reports/` directory.  
- **🧩 Modular Structure** — Built with extensibility in mind for adding new scanning modules.

---

## 🏗️ Project Structure

python-secure-code-scan/
│
├── cmd/
│ ├── main.py # Entry point to run the scanner
│
├── scanner/
│ ├── code_scan.py # Handles Bandit scan logic
│ ├── config_scan.py # Checks for exposed secrets in .env
│ ├── repo_handler.py # Clones GitHub repos
│ ├── report_generator.py # Generates vulnerability reports
│ ├── init.py
│
├── reports/ # Auto-generated scan reports
│
├── vuln_example/ # Sample vulnerable Python project
│ └── vuln_example.py
│
├── requirements.txt # Python dependencies
└── README.md # Documentation

## ⚙️ Installation Steps
### 1. Prerequisites
Ensure you have **Python 3.8+** installed.  
To check:
```bash
python --version

### 2. Clone the Repository

git clone https://github.com/your-username/python-secure-code-scan.git
cd python-secure-code-scan

### 3. (Optional) Create a Virtual Environment

python -m venv venv
# Activate the virtual environment:
# Windows
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Install Bandit

If Bandit isn’t installed globally:

python -m pip install bandit

## ▶️ How to Run the Project

Option 1: Scan a Local Directory

If you have a local project (e.g., vuln_example) you want to scan:

cd cmd
python main.py "../vuln_example"

Option 2: Scan a GitHub Repository

To scan a public GitHub repository:

cd cmd
python main.py "https://github.com/we45/Vulnerable-Flask-App.git"