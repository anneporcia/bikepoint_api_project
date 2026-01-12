# TfL BikePoint Data Pipeline

An automated data pipeline that extracts real-time bike docking station data from the **Transport for London (TfL) API**, saves it as structured JSON, and uploads it to an **AWS S3 bucket** for long-term storage and analysis.

---

## 🚀 Features

* **Real-time Extraction**: Connects to the TfL `BikePoint` endpoint to get live availability across London.
* **Resilient API Logic**: Implements a 3-try retry mechanism with wait times to handle network instability.
* **Automated Logging**: Tracks every success, retry, and error in a dedicated `/logs` folder with timestamped log files.
* **S3 Integration**: Uses `boto3` to transfer local JSON files to AWS S3.
* **Storage Efficiency**: Automatically deletes local files once the S3 upload is confirmed.

---

## 🛠 Setup and Usage

### 1. Requirements
Install the necessary Python libraries:
**Set Up**

Created a new repository, cloned it with github desktop and opened it in vscode. Created a virtual environment (**python -m venv .venv**) and activated it (**.venv/Scripts/activate**). Installed requests (**pip install requests**) - this is the only non-native package we used so it is the only one I had to install. Created a new branch (**git switch -c extract branch**). Created a requirements file (**pip freeze > requirements.txt**).

**Import Packages**

Imported packages to use in the script. Including:
 - **requests**: for calling the api
 - **os**: for finding the directory to save the file in
 - **datetime**: for timestamps
 - **json**: to use json.dump to write the file in a json format
 - **time**: to define the time it takes for it to error before it times out
 - **logging**: to create the log files and define the log messages
 - 
```bash
pip install requests python-dotenv boto3

```

### 2. Environment Configuration

Create a `.env` file in the project root to store your AWS details:

```env
AWS_ACCESS_KEY=your_access_key
AWS_SECRET_KEY=your_secret_key
bucket_name=your_s3_bucket_name

```

### 3. Execution

The pipeline consists of two main steps:

1. **Extraction**: Run the API script to pull data from TfL.
```bash
python tfl_api_extract.py

```


2. **Loading**: Run the load script to push the data to AWS S3.
```bash
python s3_load.py

```



---

## 📂 Project Structure

```text
.
├── .env                # AWS credentials
├── tfl_api_extract.py  # Script 1: Extract data from TfL API
├── s3_load.py          # Script 2: Upload JSON files to S3
├── logs/               # Log files created during extraction
└── data/               # Temporary storage for JSON files (cleaned after upload)

```

---

## ⚙️ How It Works

### Part 1: Extraction (`api_script.py`)

* **Endpoint**: `https://api.tfl.gov.uk/BikePoint`
* **Process**: The script calls the API and checks for a `200 OK` status.
* **Logging**: A log file is created for every run (named by timestamp) to record the success or failure of the download.
* **Outcome**: A JSON file containing the full list of bike points is saved in the `/data` folder.

### Part 2: Loading (`load_bike_point.py`)

* **Process**: The script scans the `/data` folder for any files ending in `.json`.
* **Transfer**: It uses the AWS SDK (`boto3`) to upload each file to the root of your specified S3 bucket.
* **Cleanup**: Upon a successful response from AWS, the local file is removed from your machine to prevent duplicate uploads and save space.

---

## 📝 Technical Notes

* **TfL API Limits**: While this script uses the public endpoint, frequent calls may require a TfL App ID/Key if you scale the project.
* **Logging**: If you don't see data in your bucket, check the `/logs` folder first to see if the API call was successful.
* **Timeout**: The API call is set with a 20-second timeout to prevent the script from hanging indefinitely.

---

