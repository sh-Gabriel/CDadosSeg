from sys import stderr, exit

def print_header(head=False):
    if not head:
        print("Error when trying to print output header", file=stderr)
        exit(1)
    print("=====================================\n")
    print(head+"\n")
    print("=====================================\n")

def output_f(data=False):
    if not data:
        exit(1)
    for i in data.keys():
        print_header(head=("Seções executáveis de " + i.split("/")[-1]))
        print(data[i],"\n\n")
    
def output_f_compare(sections1=False, sections2=False, common=False):
    if not common or not sections1 or not sections2:
        exit(1)
    print_header(head="Seções comuns aos PEs")
    print(common,"\n\n")
    print_header(head="Seções presentes somente no PRIMEIRO PE")
    print([i for i in sections1 if i not in common], "\n\n")
    print_header(head="Seções presentes somente no SEGUNDO PE")
    print([i for i in sections2 if i not in common], "\n\n")