# importing required modules
import os
import datetime
import logging

from conf.folder_path import DOWNLOADS_PATH
from dict.file_endings import FILE_SUFFIX

#setup the logging object
logger = logging.getLogger("File Delete Logs")
logger.setLevel(logging.DEBUG)

ch = logging.FileHandler(filename="logs/logs.log")
ch.setLevel(logging.DEBUG)

#set logging formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

## current date time
now = datetime.datetime.now()
cur_dt = now.strftime('%d/%m/%y,%I:%M:%S')

# folder is the name of the folder in which we have to perform the delete operation [ specify in folder_path.py ]
folder = DOWNLOADS_PATH


# days is the number of days for which we have to check whether the file is older than the specified days or not [ specify]
days = 31

def check_exists(folder):
    path_check = folder
    if os.path.exists(path_check):
        print(f'path: {path_check} exists')
        return True
    else:
        print(f"the path {path_check} does not exist")
        return False

# function to perform delete operation based on condition
def check_and_delete(folder):
   
   logger.info('started run')

   
   """
   This function takes the root (downloads) folder in and deletes files only
   in the root specified folder
   [params]: file path
   [returns]: log file with the file paths that were deleted
   [returns]:os object that removes files
   """
   if check_exists(folder) is not True:
       print(f"The file path entered, {folder} is invalid")

   # os.walk returns 3 things: current path, files in the current path, and folders in the current path
   for (root,dirs,files) in os.walk(folder, topdown=True):

       for f in files:
            
            # temp variable to store path of the file
            file_path = os.path.join(root,f)

            # get the timestamp, when the file was modified
            timestamp_of_file_modified = os.path.getmtime(file_path)

            # convert timestamp to datetime
            modification_date = datetime.datetime.fromtimestamp(timestamp_of_file_modified)

            # find the number of days when the file was modified
            number_of_days = (datetime.datetime.now() - modification_date).days
            
            # adding certain document types that need to be romved (Leave .exe / .msi for apps)
            if number_of_days > days and f.endswith((FILE_SUFFIX)): #specify tuple
                os.remove(file_path)

                logger.info(f"removed file: {f}")
                print(f"removed file {file_path}")

            #check for files in subfolders too
            elif number_of_days > days and file_path.split("/")[3].endswith((FILE_SUFFIX)): #specify tuple
                os.remove(file_path)
                
                logger.info(f"removed file: {f}")
                print(f"removed file {file_path}")

            else:
               print(f"skipping file {file_path}")

        


if __name__ == "__main__":
    
    # call function
    print(f"\nYour root folder is: {folder}\n\n...running script\n\n")

    result = check_and_delete(folder)


