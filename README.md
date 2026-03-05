# 🗂 Desktop File Organizer

A Python automation script that organizes your Desktop files by extension, automatically categorizing, moving, and logging everything in one run.

---

## Overview

**Desktop File Organizer** scans your Desktop directory and:

- Creates a dated destination folder
- Categorizes files by extension into subfolders
- Moves files into their matching category
- Generates a detailed log file
- Displays a summary of the operation

---

## ⚙️ How It Works

1. Detects the user's Desktop path via environment variables
2. Creates a folder named: `moved_file_MM-YY-DD`
3. Iterates over all files on the Desktop
4. Matches each file's extension against predefined categories
5. Moves files into the corresponding subfolder
6. Logs all operations (moved / skipped / errors)
7. Prints a final execution summary

---

## 📂 File Categories

```python
folders_ext = {
    "Python":    (".py",),
    "Images":    (".png", ".jpg"),
    "Documents": (".txt", ".pdf"),
    "Ai":        (".ai",)
}
```

> Files that don't match any extension are placed in `Others/`

---

## Requirements

- **Python 3.8+**
- **Standard Library only**  no external dependencies required:
  - `os`
  - `shutil`
  - `datetime`

---

##  Usage

Run the script from your terminal:

```bash
python file_name.py
```

After execution, a new folder will appear on your Desktop:

```
Desktop/
└── moved_file_{today_date}/
    ├── Python/
    ├── Images/
    ├── Documents/
    ├── Ai/
    ├── Others/
    └── Log_file.txt
```

---

## Code Structure

### `move_files(src, dest_folder, log, moved, skipped, errors)`

Responsible for:
- Moving files from source to destination
- Logging each result
- Updating operation counters

### `main()`

Handles:
- Environment detection
- Dated folder creation
- File iteration and extension matching
- Final statistics output

---

## Output Example

**Console output:**

```
MOVED   : 12
SKIPPED : 3
ERRORS  : 1
```

**Log file (`Log_file.txt`):**

```
----------------------------------
The process started at 03-26-05

[MOVED]  example.py
[ERROR]  file.txt : Permission denied

-->
MOVED   : 12
SKIPPED : 3
ERRORS  : 1
```

---

## Error Handling

- `try/except` blocks are used inside `move_files`
- Exceptions are logged without stopping execution
- All errors are counted and reported in the final summary

---

## Future Improvements

- [ ] Add dry-run mode (preview without moving)
- [ ] Add CLI arguments via `argparse`
- [ ] Use Python's `logging` module instead of manual file logging
- [ ] Add unit tests
- [ ] Prevent overwriting existing files
- [ ] Case-insensitive extension matching
