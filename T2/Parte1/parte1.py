from os import path, listdir
from sys import argv, exit, stderr
import argparse
from output import output_f

#given the xml line, formats it to append to the dictionary
def format_permissions(line=None):
    if(line == None):
        print("Error accessing the xml line to format permissions",file=stderr)
        exit(1)
    if("uses-permission" in line and ".permission" in line):
        tmp = line.split(".permission")[1].strip()
        return tmp.split("\"")[0]

#iterate through the .xml files to create the dictionary with the permissions
def dict_building(files=None):
    if(files == None):
        print("Error when accessing the .xml archive list",file=stderr)
        exit(1)
    app = {}
    for f in files:
        key = f.split("_")[1]
        key = key.split(".xml")[0]
        if(not key in app):
            app[key] = []
        with open(f, "r") as xml:
            for xml_line in xml:
                if("uses-permission" in xml_line and ".permission" in xml_line):
                    app[key].append(format_permissions(line=xml_line))
    return(app)

#iterates through the given directory to gather the .xml files
def directory_iteration(directory=None):
    if(directory == None):
        print("Error when accessing the directory to iterate", file=stderr)
        exit(1)
    dir_content = listdir(directory)
    #list containing only xml files from the given directory
    iterable = []
    for item in dir_content:
        if(".xml" in item):
            iterable.append("/".join([directory,item]))

    return(dict_building(files=iterable))

if __name__ == "__main__":
    #Command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-dp", "--database_path", default=None, help="Path to the directory containing the xml archives", 
                        required=True, dest="database_path")
    parser.add_argument("-ppa", "--permissions_per_apk", default=True, help="Print the found permissions per apk. Default to true", 
                        required=False, dest="ppa", action="store_false")
    parser.add_argument("-u", "--unique", default=False, help="Prints only the unique permissions per apk. Default to false",
                        required=False, dest="unique", action="store_true")
    parser.add_argument("-c", "--common", default=False, help="Prints only the common permissions for all the apks. Default to false",
                        required=False, dest="common", action="store_true")
    
    args = parser.parse_args()
    #pegando o path inteiro como parâmetro
    try:
        l = path.exists(args.database_path)
        if(not l):
            print("The given path doesn't exists", file=stderr)
            exit(1)
    except:
        exit(1)
    data = directory_iteration(directory=args.database_path)
    output_f(data, args)
    