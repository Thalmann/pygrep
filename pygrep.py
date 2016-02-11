import os
from termcolor import colored
import argparse

cwd = os.getcwd()
files = list()
dirs = list()
hits = list()

parser = argparse.ArgumentParser()
parser.add_argument('search_term')
args = parser.parse_args()
search_term = args.search_term

def get_files(path, recursive=True):
    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            files.append(os.path.join(dir_path,file_name))
        for dir_name in dir_names:
            dirs.append(os.path.join(dir_path, dir_name))
        
def search_file(file_path, search_term):
    with open(file_path, 'r') as f:
        try:
            line_number = 0
            for line in f:
                line_number += 1
                if search_term in line:
                    hits.append(file_path)
                    print(str(len(hits)) + colored(': ', 'blue') + file_path + colored(': ', 'blue') + str(line_number)+ ':' + highlight_search_term(line, search_term))
        except UnicodeDecodeError:
            return

def highlight_search_term(line, search_term):
    return line.replace(search_term,colored(search_term, 'red'))

get_files('.')

#print(files)
#print(dirs)

for f in files:
    search_file(f, search_term)

file_number = input('Insert file number:\n')
print(hits[int(file_number)-1])
