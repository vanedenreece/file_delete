# File Delete

This automation uses a simple python script to delete files in the specified downloads folder

## How to:

- Install [Python](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/) package manager


## Workflow

- 1) Specify Root Folder path,usually downloads but can be something else 
- 2) Specify number of days since file was modified
- 3) Specify what files should be deleted in a tuple, example: *(".pdf",".png")*
- 4) Files that are removed are deleted from the root folder ( downloads ) and logged to a log file

## How does this script help me?

- [x] Can be used in conjunction with a batch/cron job to automate deletion of downloads ( per week, month)
- [x] Automates the manual task of reading through each downloaded file and removing it
- [x] Keeps a neat downloads folder that others envy 🫠