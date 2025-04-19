# DevOps Daily Journal 🛠📓

A personal logging system for developers, engineers, and chaotic creators who want to track their work, ideas, and system configs in structured Markdown — and keep everything observably tagged and searchable in Obsidian

## Features

- 📝 Generate pre-formatted daily log templates
- 🧠 Automatically inject metadata tags into Obsidian-compatible headers
- 🛡 Detect and log tag updates to track content drift over time
- 🧰 CLI friendly — build into your cron rituals

## Folder Structure

devops-daily-journal/
├── README.md
├── LICENSE
├── scripts/
│   ├── newlog.py         # generates daily log files
│   └── taglog.py         # detects tag changes and logs them
├── bin/
│   ├── newlog            # optional symlink to scripts/newlog.py
│   └── taglog            # optional symlink to scripts/taglog.py
├── logs/
│   └── taglog.log        # default output (append-only, not versioned)
├── tests/
│   └── test_taglog.py    # placeholder for future testing
├── requirements.txt
└── .gitignore

## Why?

Because Bash is a liar and metadata deserves better.

---

> I didn't want a journal.
> I wanted observability for his soul.
