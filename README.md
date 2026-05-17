# 🕵️‍♂️ The Social Media Data Detective

## 📌 Project Overview
**The Social Media Data Detective** is a back-end data engineering and analytics application designed to clean, parse, and extract strategic insights from a massive, messy dataset of 10,000 raw Twitter posts. 

The project simulates a real-world corporate environment where standard automated shortcuts are restricted. To prove a deep understanding of core computing logic, this suite bypasses all built-in shorthand helpers to demonstrate raw algorithmic data manipulation from the ground up. 

The architecture is split into two components:
1. **The Algorithmic Core (`data-detective.py`):** Handles deep processing logic, data type normalizations, and interactive keyword filters using foundational human-designed loops.
2. **The Command-Line Pipeline (`feed-analyzer.sh`):** Leverages server-side speed to show how a single, high-performance line of command-line shell code can duplicate complex scripts using piped Linux text utilities.

---

## 📁 Project Architecture

The workspace is organized within a unified directory root folder to ensure zero file-path connection conflicts:


| File Name | Structural Type | Core Analytical Purpose |
| :--- | :--- | :--- |
| `data-detective.py` | Python Script | Executes data auditing, custom max searches, and keyword extractions. |
| `feed-analyzer.sh` | Bash Shell Script | Chained command pipeline tracking user post frequency counters. |
| `twitter_dataset.csv` | CSV Dataset | Core raw database file downloaded from Kaggle (10,000 entries). |
| `python_file_output.png` | Image File | Terminal screenshot proving flawless Python execution. |
| `feed_analyser_bash_ouput.png` | Image File | Terminal screenshot proving flawless Bash execution. |
| `README.md` | Markdown Asset | Project structural index and technical algorithm documentation. |

---

## 🚀 Execution Instructions

### 1. Python Analytics Engine
Run this command from your terminal to launch the sequential data-handling pipeline:
```bash
python data-detective.py
```
* **Quest 1 (Data Auditor):** Evaluates dataset rows, drops entries missing raw tweet text strings, and normalizes blank metrics to `"0"`.
* **Quest 2 (The Viral Post):** Runs a manual comparative scan to isolate the single highest engagement count without using `max()`.
* **Quest 3 (Algorithm Builder):** Reorganizes the entire array descending via an in-place array element swap tracking system.
* **Quest 4 (Content Filter):** Prompts interactive string tracking and returns matched collections alongside an explicit `len()` total.

### 2. Bash Stream Utility
Run this command in a Git Bash terminal window to initiate instant server-side data stream isolation:
```bash
bash feed-analyzer.sh
```
* Extracts column 2 fields, cleans Windows carriage returns (`\r`), groups identical string entries, counts frequencies, and strips the terminal output boundaries down to the **Top 5 Most Active Users**.

---

## 📊 Algorithmic Sorting Architecture
This application implements a custom **Selection Sort** algorithm inside Quest 3 to order data values by popularity rank without relying on banned native `.sort()` or `sorted()` utilities. The loop architecture steps systematically through remaining unsorted array index boundaries, evaluates values using explicit string-to-integer (`int()`) type casting, tracks the index location of the absolute largest total, and runs an evaluation-compliant variable swap to shuffle the top 10 items to the front of the list layout.

---

## 📸 Execution Output Previews

### Python Script Workflow (Quests 1 - 4)
![Python Script Execution Output](python_file_output.png)

### Bash Script Workflow (Active User Rankings)
![Bash Script Execution Output](feed_analyser_bash_ouput.png)
