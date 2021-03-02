import git
import os
import csv

from m_data import M_data

l = ["true", "fake"]

def populate_data():
    db = "./database/"
    for cat in l:
        with open(db+cat+".csv", "w") as _csv:
            #csv writer instance
            csv_writer = csv.writer(_csv, dialect='unix', quoting=csv.QUOTE_MINIMAL)
            #data header
            data_rows = ["text"
                        ,M_data.CATEGORY
                        ,M_data.NUM_WITHOUT_PONCT
                        ,M_data.NUM_UPPERCASE
                        ,M_data.NUM_SUBJ_IMP
                        ,M_data.AVG_SENT_LEN
                        ,M_data.SPEL_ERROR]
            header = [X.name for X in data_rows[1:]]
            header.insert(0, data_rows[0])
            csv_writer.writerow(header)
            #pwd to construct others
            pwd = "./Fake.br-Corpus/full_texts/" + cat + "/"
            pwd_f = "./Fake.br-Corpus/full_texts/" + cat + "-meta-information/"
            #list of archives on directory
            dir_content = os.listdir(pwd)
            #for each archive
            for archive in dir_content:
                #the meta info of a archive consists of its name + "-meta"
                meta = archive.split(".")
                meta[0] += "-meta"
                meta = ".".join(meta)
                with open(pwd+archive) as data, open(pwd_f+meta) as metadata:
                    a = metadata.readlines()
                    categories = []
                    for wanted in data_rows[1:]:
                        categories.append(a[wanted.value].strip())
                    
                    
                    joint = [data.readline().strip()] + categories
                    joint[0] = str(joint[0])
                    csv_writer.writerow(joint)

if __name__ == "__main__":
    # git.Git("./").clone("https://github.com/roneysco/Fake.br-Corpus.git")
    # print("path %s" % os.getcwd())
    # print(os.listdir(os.getcwd()))
    # try:
    #     os.mkdir("./database")
    # except:
    #     print("failed")
    #     exit(1)
    populate_data()