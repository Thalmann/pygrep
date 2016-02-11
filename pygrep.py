import os
from termcolor import colored
import argparse

cwd = os.getcwd()
dirs = list()
hits = list()

parser = argparse.ArgumentParser()
parser.add_argument('search_term', help='insert the search term you want to search for')
parser.add_argument('-r', help='search recursively', action='store_true')
args = parser.parse_args()
search_term = args.search_term
recursive_search = args.r

# Should use yield return
def get_files_recursive(path):
    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            yield os.path.join(dir_path,file_name)
        for dir_name in dir_names:
            dirs.append(os.path.join(dir_path, dir_name))
            
def get_files(path):
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            yield f

            
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


if recursive_search:
    for f in get_files_recursive('.'):
        search_file(f, search_term)
else:
    for f in get_files('.'):
        search_file(f, search_term)

file_number = input('Insert file number:\n')
print(hits[int(file_number)-1])
