#!/bin/bash

# Target dataset path 
DATA_FILE="twitter_dataset.csv"

# Verify the target dataset exists and can be read before launching the pipeline
if [ ! -r "$DATA_FILE" ]; then
    echo "Error: Cannot read $DATA_FILE. Please ensure the file is inside this folder."
    exit 1
fi

# The exact command chain required by your manager's prompt:
# 1. cut - Isolates and extracts only the Username data (Column 2)
# 2. sort - Arranges usernames alphabetically to group identical entries together
# 3. uniq - Collapses those adjacent duplicates and displays the matching counts
# 4. sort - Reruns a sort numerically (-n) in reverse/descending order (-r)
# 5. head - Clips the resulting output stream to show only the Top 5 items
cut -d',' -f2 "$DATA_FILE" | sort | uniq -c | sort -nr | head -n 5
