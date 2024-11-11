import uuid

def generateKey(key_list):
    key = ""
    for i in range(0, len(key_list)):
        if len(key_list[i]) == 2 and key_list[i][1] == "-":
            key += i + uuid.uuid4().hex[0: 12]
        if i != (len(key_list) - 1):
            key += "-"
    return key