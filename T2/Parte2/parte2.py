
import pefile
from sys import argv, exit, stderr
import argparse
from os import listdir, path


def is_executable(charac=False):
    if not charac:
        exit(1)
    b = []
    for i in range(len(charac)):
        b.append(str(0))
    b[0] = str(8)
    div = "".join(b)
    if hex(int(charac, 16)//int(div, 16)).split("x")[1] != str(0):
        charac = hex(int(charac, 16) - int(div, 16))
    b[0] = str(4)
    div = "".join(b)
    if hex(int(charac, 16)//int(div, 16)).split("x")[1] != str(0):
        charac = hex(int(charac, 16) - int(div, 16))
    b[0] = str(2)
    div = "".join(b)
    if hex(int(charac, 16)//int(div, 16)).split("x")[1] != str(0):
        return True
    return False

def dict_building(pe_list = False):
    if not pe_list:
        exit(1)
    
    sect_permissions={}
    for item in pe_list:
        pe = pefile.PE(item)
        sect_permissions[item] = []
        for i in pe.sections:
            charac = hex(i.Characteristics).split("x")[1]
            if(is_executable(charac=charac)):
                string = str(i.Name.decode('utf-8').encode("unicode_escape")).split("\\")[0]
                sect_permissions[item].append(string.split("'")[1])
    return sect_permissions

def print_output(permissions=False):
    if not permissions:
        exit(1)
    for i in permissions.keys():
        print("O executável ", i.split("/")[-1], " possui as seguintes seções executáveis: ", permissions[i], "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--archive", default=None, help="Path to the directory containing the xml archives", 
                        dest="archive")
    parser.add_argument("-dp", "--directory_path", default=None, help="Print the found permissions per apk. Default to true", 
                        dest="directory_path")
    args = parser.parse_args()

    if not (args.archive or args.directory_path):
        parser.error("Give at last one archive or a path to the directory containing it") 
        exit(1)
    elif args.archive and args.directory_path:
        parser.error("Use oly one option")
        exit(1)

    archives = []
    if args.directory_path:
        try:
            l = path.exists(args.directory_path)
        except:
            print("Path argument not found",file=stderr)
            exit(1)
        dir_content = listdir(args.directory_path)
        path = args.directory_path.split("/")
        path.append(" ")
        for item in dir_content:
            path[-1] = item
            archives.append("/".join(path))
        
    else:
        archives.append(args.archive)
    permissions = dict_building(pe_list=archives)
    print_output(permissions=permissions)