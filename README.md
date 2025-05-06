# DevOps Daily Journal 🛠📓

A personal logging system for developers, engineers, and chaotic creators who want to track their work, ideas, and system configs in structured Markdown — and keep everything observably tagged and searchable in Obsidian

## Features

- 📝 Generate pre-formatted daily log templates
- 🧠 Automatically inject metadata tags into Obsidian-compatible headers
- 🛡 Detect and log tag updates to track content drift over time
- 🧰 CLI friendly — build into your cron rituals

### Log message format

level=`<log_level>` event=`<event_name>` file=`<file_name>` [reason=`<reason>`] [tags=`<tags>`]
Example: level=warn event=tag_skipped file=example.md reason=malformed_front_matter
Example: level=info event=tag_injected file=example.md tags=devops,grafana,loki,promtail

### Folder Structure

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

## 📓 Taglog Script

### Purpose

Automatically manage and update metadata tags in Obsidian-compatible Markdown files.  
This script injects YAML front matter based on inline hashtags and tracks any changes in a centralized log, supporting structured observability for personal logs or DevOps documentation.

### Key Features

#### 1. Automatic File Naming

- Operates on `.md` files modified in the last 24 hours within a specified directory.

#### 2. Pre-Filled Template

- If no YAML front matter is present, it extracts inline `#tags` from line 3 and injects them as a properly formatted YAML list.

#### 3. Logging

- Appends structured log entries to `taglog.log` for every operation:
  - `tag_injected` for newly created tags
  - `tag_updated` when tags change
  - `tag_skipped` when skipping malformed or untaggable files

#### 4. Integration with CLI

- Can be used in cron jobs or shell scripts with no external interaction.
- Simple to integrate into pipelines or other automation workflows.

### Workflow

#### 1. File Creation

- Walks the target directory recursively.
- Identifies markdown files modified in the last 24 hours.

#### 2. Logging the Event

- Logs follow this format:  
  `level=<level> event=<event> file=<file_name> [reason=<reason>] [tags=<tags>]`

- Example:  
  `2025-04-19T13:00:00 level=info event=tag_injected file=19-04-2025.md tags=docker,devops,loki`

#### 3. User Notification

- No terminal output unless integrated with other scripts — logging happens silently.
- Errors are logged instead of thrown to the user.

#### Example Use Case

You’ve written a daily log in Obsidian and added inline hashtags like:

```markdown
# 19.04.2025  
#docker #grafana #promtail
```

The script will detect no front matter, extract the hashtags, and transform your file into:

```markdown
---
tags:
  - docker
  - grafana
  - promtail
---

# 19.04.2025  
#docker #grafana #promtail
```

A log entry is created:

```log
2025-04-19T13:00:00 level=info event=tag_injected file=19-04-2025.md tags=docker,grafana,promtail
```

### Notes

- Uses **PyYAML** for parsing and formatting.
- Will **not** overwrite existing tag entries unless malformed.
- Validates tag changes by comparing current YAML with the latest log entry.
- Rejects files with:
  - No tags
  - Invalid or malformed YAML
  - Errors during read/write
- Aimed at **personal observability**, not enterprise-scale nonsense

## Why?

Because Bash is a liar and metadata deserves better.
> I didn't want a journal.
> I wanted observability for his soul.
