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
