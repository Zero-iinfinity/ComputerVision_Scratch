#--------------------------------------------------------------------------------------------------
# THIS FILE CONTAINS NECESSARY OS FUNCTIONS IN IT (don't run the whole code might cause some error)
#--------------------------------------------------------------------------------------------------


import os

'''gives the current working directory'''
print(os.getcwd())

'''change the working directory'''
os.chdir(r"Directory_path")

'''make single directory '''
os.mkdir('python_1')

'''can make directories with in the directories'''
os.makedirs('python_2/python_3/python_4')

'''delect the exact directory only one'''
os.rmdir('python_1')

'''removed sub-dir also'''
os.removedirs("python_2/python_3")

'''renames the directory'''
os.rename('python_2','os_demo')

'''gives the stats of the given file like date time size'''
print(os.stat('Books_SEM_4'))

'''gives the list of directories '''
print(os.listdir())

'''walk through all the files in the given directory and gives tuple of 3 path , directory, file'''
for dirpath, dirnames, filenames in os.walk(r"C:\Users\Vikas Dubey\Desktop"):
    print('current directory: ', dirpath)
    print('directory: ', dirnames)
    print('files: ', filenames)
    print()

'''lists the environments'''
print(os.environ)

'''joins two paths so no need to care for those slashes // '''
os.path.join('first','second')

'''gives the last file '''
print(os.path.basename(r'/tmp/test.txt'))

'''gives the directory name of the file'''
print(os.path.dirname(r'/tmp/test.txt'))

'''gives the split of the path tuple of directory and file'''
print(os.path.split(r'/tmp/test.txt'))

'''this checks whether the path  exists or not'''
print(os.path.exists(r'/tmp/test.txt'))

'''splits the path and extension'''
print(os.path.splitext(r'/tmp/test.txt'))


#to append a whole list use .extent

'''spliting filename and extension'''
import os
array = ['ABCD.txt', 'XYZ.txt']
new_array = [os.path.splitext(name)[0] for name in array] # This [0] is for getting 1 item of a list for the example it is ABCD,XYZ
#if you use [1] it output .txt,.txt
print(new_array)

'''to remove file'''
os.remove('test.txt')

'''difference btw exists and isfile'''
# 1. `os.path.exists()`:
#     - Checks if a path exists
#     - Returns for both files AND directories `True`
#     - Use when you just need to know if something exists, regardless of type
#
# 2. `os.path.isfile()`:
#     - Checks if a path exists AND is a regular file
#     - Returns ONLY for files `True`
#     - Returns for directories, symbolic links, etc. `False`
#     - Use when you specifically need to confirm something is a file

'''moving file from one directory to another directory'''
import os

# Define the source file path and the destination directory path
source_file = 'path/to/source/file.txt'
destination_directory = 'path/to/destination/'

# Move the file
os.rename(source_file, destination_directory + os.path.basename(source_file))

'''always use os.path.join() to add paths or to define paths'''