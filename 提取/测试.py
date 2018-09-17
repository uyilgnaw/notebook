import hashlib

def getMD5(v):
    md5 = hashlib.md5()

    md5.update(v.encode("utf-8"))

    sign = md5.hexdigest()

    return sign

print(getMD5('mrking'))