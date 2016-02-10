import os
from termcolor import colored

cwd = os.getcwd()
files = list()
dirs = list()
success_files = list()

def get_files(path, recursive=True):
    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            files.append(os.path.join(dir_path,file_name))
        for dir_name in dir_names:
            dirs.append(os.path.join(dir_path, dir_name))
        
def search_file(file_path, keyword):
    with open(file_path, 'r') as f:
        try:
            for line in f:
                if keyword in line:
                    success_files.append(file_path)
                    print(str(len(success_files)) + ':     ' + file_path + ':     ' + highlight_keyword(line, keyword))
        except UnicodeDecodeError:
            return

def highlight_keyword(line, keyword):
    return line.replace(keyword,colored(keyword, 'red'))

get_files('.')

#print(files)
#print(dirs)

for f in files:
    search_file(f, 'ECB')

file_number = input('Insert file number:\n')
print(success_files[int(file_number)-1])
