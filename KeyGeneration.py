import uuid

def generateKey():
    return uuid.uuid4().hex[0: 12]