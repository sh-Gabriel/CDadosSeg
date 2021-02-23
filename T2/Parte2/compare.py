from sys import argv, stderr
import pefile


def get_sections(pes=False):
    if not pes:
        exit(1)
    sections = [[], []]
    for i in range(1,3):
        pe = pefile.PE(pes[i])
        for sect in pe.sections:
            string = str(sect.Name.decode('utf-8').encode("unicode_escape")).split("\\")[0]
            sections[i-1].append(string.split("'")[1])
    
    return sections[0], sections[1]

def compare(sections1=False, sections2=False):
    if not sections1 or not sections2:
        exit(1)
    common = []
    for contentA in sections1:
        for contentB in sections2:
            if contentB == contentA:
                common.append(contentA)
    print("As seguintes seções são comuns a ambos os arquivos: ", common, "\n")
    print("As seguintes seções pertencem somente ao PRIMEIRO PE: ", [i for i in sections1 if i not in common], "\n")
    print("As seguintes seções pertencem somente ao SEGUNDO PE", [i for i in sections2 if i not in common], "\n")

if __name__ == "__main__":
    if len(argv) != 3:
        print("Wrong number of arguments",stderr)
        exit(1)
    sections1, sections2 = get_sections(pes=argv)
    compare(sections1=sections1, sections2=sections2)
