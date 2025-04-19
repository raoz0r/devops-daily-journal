#!/usr/bin/env python3

import os
from datetime import datetime

# Configuration
LOG_FILE = "/mnt/storage/logs/taglog.log"


def main():
    # Compute today's date and filenames
    today = datetime.now().strftime("%d-%m-%Y")
    filename = f"{today}.md"

    # Template for the daily log file
    template = f"""# {today}

#replace-with-tags <!-- markdownlint-disable-line MD018 -->

## 🌟 Daily Goals

- [ ] Task 1

## 📑 Work Log

## 🧠 Insights & Decisions

## 👨🏽‍💻 Troubleshooting 🕵️

## 🧰 Tools 📓 📝 <!-- markdownlint-disable MD024 -->

### 📓 Bash Script Heading Sample

#### Purpose

#### Key Features

##### 1. Automatic File Naming

##### 2. Pre-Filled Template

##### 3. Logging

##### 4. Integration with CLI

#### Workflow

##### 1. File Creation

##### 2. Logging the Event

##### 3. User Notification

#### Example Use Case

#### Notes

## 🗃️  Step-by-Step Guide 🛠️ ⚙️ 

## 🔗 Resources

## 🗓️ Next Day Preview
"""

    # Write the template to the new file
    try:
        with open(filename, 'w') as f:
            f.write(template)
        print(f"📝 Log created: {filename}")
    except IOError as e:
        print(f"⚠️ Error creating {filename}: {e}")
        return

    # Append the event to the log file
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    log_entry = f"{timestamp} level=info event=daily_log_initialized file={filename}\n"
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, 'a') as lf:
            lf.write(log_entry)
        print(f"Log entry added to {LOG_FILE}")
    except IOError as e:
        print(f"⚠️ Error writing to log file {LOG_FILE}: {e}")

if __name__ == '__main__':
    main()
