import os
import shutil

#This paths format refers to paths in windows operating system
source_path = 'C:\\Desktop\\folder1\\folder2\\folder3'
destination_path = 'C:\\folder4\\folder5\\folder6'

#Get all the files in the source path
files_in_folder = os.listdir(source_path)

#Loop in all the files and check for file ending with the extention required
#Here it looks for .log extetion
for file in files_in_folder:
	if os.path.isfile(source_path+'\\'+file) and file.endswith('.log'):
    #Move the files to the dest folder if the above conditions satisfies
		shutil.move(source_path+'\\'+file, destination_path)
