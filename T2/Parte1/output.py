from sys import stderr, exit

def print_header(head=False):
    if not head:
        print("Error when trying to print output header", file=stderr)
        exit(1)
    print("=====================================\n\n")
    print(head+"\n\n")
    print("=====================================\n\n")

def unique_value(key=False, value=False, dic=False):
    if not key or not value or not dic:
        exit(1)
    for i in dic.keys():
        if i != key:
            if(value in dic[i]):
                return False
    return True

def unique_permissions(data=False):
    if not data:
        exit(1)
    for key in data.keys():
        content = []
        for value in data[key]:
            if(unique_value(key=key, value=value, dic=data)):
                content.append(value)
        out = key + ": "
        print(key + ": " + str(content) + "\n")
        
def common_value(key=False, value=False, dic=False):
    if not key or not value or not dic:
        exit(1)
    for i in dic.keys():
        if i != key:
            if(not value in dic[i]):
                return False
    return True

def common_permissions(data=False):
    if not data:
        exit(1)
    content = []
    for key in data.keys():
        for value in data[key]:
            if value not in content:
                if(common_value(key=key, value=value, dic=data)):
                    content.append(value)
    print(content)

def output_f(data=False, args=False):
    if not data or not args:
        print("Error when trying to print output",file=stderr)
        exit(1)
    if(args.ppa):
        print_header(head="Permissões por APK")
        for item in data.keys():
            print(item + ": "+  str(data[item]) + "\n")
    if(args.unique):
        print_header(head="Permissões únicas por APK")
        unique_permissions(data=data)
    if(args.common):
        print_header(head="Permissões comuns das apks")
        common_permissions(data=data)
