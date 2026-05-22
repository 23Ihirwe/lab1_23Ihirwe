#!/bin/bash

# Target dataset path 
DATA_FILE="twitter_dataset.csv"

# Verify the target dataset exists and can be read before launching the pipeline
if [ ! -r "$DATA_FILE" ]; then
    echo "Error: Cannot read $DATA_FILE. Please ensure the file is inside this folder."
    exit 1
fi

# The exact command chain required by your manager's prompt:
# 1. tail - Skips the CSV header row
# 2. cut - Extracts column 2 (Username)
# 3. sort - Groups identical usernames together alphabetically
# 4. uniq -c - Collapses duplicates and generates the occurrence counts
# 5. sort -nr - Sorts the results numerically in descending order
# 6. head -n 5 - Filters the output stream to show only the Top 5 items
# 7. tr -d - Strips hidden Windows formatting characters right before final text display
tail -n +2 "$DATA_FILE" | cut -d',' -f2 | sort | uniq -c | sort -nr | head -n 5 | tr -d '\r'



