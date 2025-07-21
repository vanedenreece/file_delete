# File Delete

This automation uses a simple python script to delete files in the specified downloads folder

## How to:

Download python and pypi package manager
- clone repo
- Install [Python](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/) package manager
    - All libraries used in the main file come standard with python > 3.0



## Workflow

- 1) Specify Root Folder path, in [folder_path.py](conf/folder_path.py), usually downloads but can be specified to other folder where you want the script to run

- **NB** file path must be a **backslash** else an Index Error will show in the console

```
IndexError: list index out of range
```

- 2) Specify number of days since file was modified in [main.py](main.py)
- 3) Specify what files should be deleted in a tuple, example [file_endings.py](dict/file_endings.py): *(".pdf",".png")*
- 4) Files that are removed are deleted from the root folder ( downloads ) and logged to a [log](logs/logs.log) file 

## How does this script help me?

- [x] Can be used in conjunction with a batch/cron job to automate deletion of downloads ( per week, month)
- [x] Automates the manual task of reading through each downloaded file and removing it
- [x] Keeps a neat downloads folder that others envy 🫠
