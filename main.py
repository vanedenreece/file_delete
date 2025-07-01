# importing required modules
import os
import datetime
import logging

#setup logging object
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)

# folder is the name of the folder in which we have to perform the delete operation
folder = "PATH TO ROOT FOLDER"

# days is the number of days for which we have to check whether the file is older than the specified days or not
days = 31

# function to perform delete operation based on condition
def check_and_delete(folder):


   # os.walk returns 3 things: current path, files in the current path, and folders in the current path
   for (root,dirs,files) in os.walk(folder, topdown=True):

       for f in files:
            # temp variable to store path of the file
            file_path = os.path.join(root,f)

            # get the timestamp, when the file was modified
            timestamp_of_file_modified = os.path.getmtime(file_path)

            #    convert timestamp to datetime
            modification_date = datetime.datetime.fromtimestamp(timestamp_of_file_modified)

            # find the number of days when the file was modified

            number_of_days = (datetime.datetime.now() - modification_date).days

            if number_of_days > days and f.endswith((".txt",".pdf",".xlsx",".csv",".png","docx","jpg")):
                os.remove(file_path)
                logging.info(f"removed file{f}")

            elif number_of_days > days and file_path.split("/")[3].endswith((".dat",".zip")):
                os.remove(file_path)
                logging.info(f"removed file{f}")

            else:
               logging.info(f'skipping file{f}')


# call function
check_and_delete(folder)