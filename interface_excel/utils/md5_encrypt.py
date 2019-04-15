import hashlib


def md5_encrypt(text):
    m5 = hashlib.md5()
    # TypeError: Unicode-objects must be encoded before hashing for python3
    m5.update(text.encode("utf-8"))
    value = m5.hexdigest()
    return value

if __name__ == "__main__":
    print(md5_encrypt("ccc"))

# 9df62e693988eb4e1e1444ece0578579
# 9df62e693988eb4e1e1444ece0578579
