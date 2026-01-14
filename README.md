<div align="center">

# 🚲 TfL BikePoint Data Pipeline

<img src="https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python" alt="Python">
<img src="https://img.shields.io/badge/AWS-S3-orange?style=for-the-badge&logo=amazon-aws" alt="AWS">
<img src="https://img.shields.io/badge/Source-TfL_API-red?style=for-the-badge&logo=london-underground" alt="TfL">

<br />

<p>
  <b>A ELT script that extracts live cycle hire data from Transport for London (TfL) and archives it to AWS S3.</b>
</p>

</div>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Workflow Architecture](#-workflow-architecture)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Environment Configuration](#-environment-configuration)
- [Running the Pipeline](#-running-the-pipeline)

---

## 📖 Overview

This project captures real-time data from the **TfL BikePoint API**, which provides the status, location, and availability of cycle hire docking stations across London. The pipeline is designed to:

1.  **Extract:** Query the TfL API for the latest station data.
2.  **Save:** Store the raw JSON response locally with a precise timestamp.
3.  **Load:** Upload the JSON file to a specified AWS S3 bucket.
4.  **Cleanup:** Remove the local file to maintain a clean environment.

---

## ⚙️ Workflow Architecture



```mermaid
graph TD;
    Start([main.py]) -->|Initialize| Env[Load .env Variables];
    Env --> API[GET tfl.gov.uk/BikePoint];
    API -- "Success (200)" --> Save["Save JSON to /data"];
    API -- Fail --> Retry["Retry (Max 3)"];
    Save --> Upload[Upload to AWS S3];
    Upload --> Cleanup[Delete Local JSON];
    Cleanup --> End([Finish]);
    
    subgraph Logging
    Log1[extract Logs]
    Log2[load Logs]
    end
    
    API -.-> Log1
    Upload -.-> Log2

```

---

## 📂 Project Structure

The project assumes the following modular structure:

```text
├── modules/
│   ├── __init__.py       # (Optional)
│   ├── extract.py        # Logic to fetch data from TfL API
│   ├── load.py           # Logic to upload files to S3
│   └── logging.py        # Logging configuration
├── main.py               # Orchestrator script
├── .env                  # Secrets (Not committed to Git)
└── requirements.txt      # Dependencies

```

---

## 🛠 Prerequisites

Ensure you have Python installed. Install the necessary packages using pip:

```bash
pip install requests boto3 python-dotenv

```

---

## 🔐 Environment Configuration

Create a `.env` file in the root directory. This keeps your AWS credentials secure.

```ini
# .env file

# AWS Credentials
AWS_ACCESS_KEY=your_access_key_here
AWS_SECRET_KEY=your_secret_key_here

# S3 Configuration
bucket_name=your_s3_bucket_name

```

---

## 🚀 Running the Pipeline

To execute the script, simply run `main.py`. This is ideal for setting up as a Cron job or a Scheduled Task.

```bash
python main.py

```

### Outputs

* **Console:** Displays status messages (e.g., `Download successful`, `found X files`).
* **Logs:** Generates folder-based logs (`extract_logs/`, `load_logs/`) timestamped for every run.
* **S3:** The JSON data will appear in the root of your target S3 bucket.

---

<div align="center">
<sub>Built with 💖 using Python</sub>
</div>
