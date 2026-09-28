### Task 2.3: Write a recursive program that lists all the files and directories in the current directory, as well as all files and directories in its sub-directories and so on.
import os

print("*"*30)
print("Task 2.3: Write a recursive program that lists all the files and directories in the current directory, as well as all files and directories in its sub-directories and so on.")

def list_files_directories(cwd):

    files = [item for item in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, item))]
    directories = [item for item in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, item))]

    print(f"CWD: {cwd}")
    print(f"Dirs: {directories}")
    print(f"Files: {files}")
    print("\n")

    if len(directories) == 0: 
        return
    else:
        for directory in directories:
            list_files_directories(os.path.join(cwd,directory))
        

list_files_directories(os.getcwd())
print("*"*30)