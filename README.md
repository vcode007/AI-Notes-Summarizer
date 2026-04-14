# AI Notes Summarizer with Gemini

A beginner-friendly Python project that summarizes multiple `.txt` files using the Google Gemini API and saves structured JSON outputs.

This project is designed as an entry-level AI engineering workflow:
- Load secure API credentials from `.env`
- Read text files from an input directory
- Generate model-based summaries in JSON format
- Save one output file per input file

---

## Features

- Uses the **Google GenAI Python SDK**
- Reads all `.txt` files from `input_files/`
- Summarizes each file with `gemini-2.5-flash`
- Requests **JSON-formatted output** from the model
- Handles temporary API server issues with a **retry loop** (3 attempts, 5-second interval)
- Saves output JSON files to `outputs/`

---

## Project Structure

```bash
day 2/
├── main.py
├── .env
├── .gitignore
├── input_files/
│   ├── file.txt
│   ├── file1.txt
│   └── file2.txt
└── outputs/
    ├── file_summary.json
    ├── file1_summary.json
    └── file2_summary.json
```
## Tech Stack
----------

*   Python 3.11+
    
*   [google-genai](https://pypi.org/project/google-genai/)
    
*   [python-dotenv](https://pypi.org/project/python-dotenv/)
    

Setup
-----

### 1) Clone the repository

git clone cd /day\\ 2

### 2) Create and activate a virtual environment

**Windows (PowerShell):**

python -m venv .venv.venv\\Scripts\\Activate.ps1

**macOS/Linux:**

python3 -m venv .venvsource .venv/bin/activate

### 3) Install dependencies

pip install google-genai python-dotenv

### 4) Configure environment variables

Create a .env file in the project root (day 2/):

GEMINI\_API\_KEY=your\_api\_key\_here

Usage
-----

1.  Add .txt files into input\_files/
    
2.  Run the script:
    

python main.py

1.  Check generated summaries in outputs/
    

Output file naming pattern:

*   input\_files/file1.txt -> outputs/file1\_summary.json
    

Expected Output Format
----------------------

Each summary is saved as JSON with this structure:

{ "title": "string", "key\_points": \["string", "string", "string"\], "sentiment": "string"}

Error Handling
--------------

The script currently handles:

*   Missing GEMINI\_API\_KEY
    
*   Missing input files/folders
    
*   Empty .txt files
    
*   Temporary Gemini server overload (503) with retries
    

Example Output
--------------

{ "title": "Building Reliable AI Coding Workflows for Unreal Engine 5", "key\_points": \[ "Agentic code assistants accelerate Unreal development tasks.", "Reliable outputs require project-specific context and conventions.", "Better retrieval systems reduce context gaps in large codebases." \], "sentiment": "Positive"}

Learning Outcomes
-----------------

This project helped me practice:

*   API integration with Gemini
    
*   Prompt engineering for structured outputs
    
*   JSON parsing and file writing in Python
    
*   Retry logic for production-like robustness
    
*   Batch file processing with pathlib
