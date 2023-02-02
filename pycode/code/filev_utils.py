
"""

Glossary:
 - loi = list of integers

"""

def detect_encoding(s: bytes) -> str:
    """
    An attempt to detect the utf encoding
    """
    if s[0] == 255 and s[1] == 254:
        if s[2] == 0:
            return "utf-32"
        else:
            return "utf-16"
    else:
        return "utf-8 or other"


def txt2loi(s) -> list[int]:
    """
    Convert a string or bytes into a list of integers (loi)
    """
    print(type(s))
    if isinstance(s, str):
        return [ord(c) for c in s]
    elif isinstance(s, bytes):
        print(detect_encoding(s))
        return [c for c in s]
    else:
        print("Expecting types str or bytes, found:",type(s))
        return []




if __name__ == "__main__":
    print(txt2loi("abc"))
    print(txt2loi("ABC"))
    a = "123éàèðαא☺ꞅ"
    print(txt2loi(a))
    print(txt2loi(bytes(a, encoding="utf-8")))
    print(txt2loi(bytes(a, encoding="utf-16")))
    print(txt2loi(bytes(a, encoding="utf-32")))
    print(txt2loi(bytes("123", encoding="ascii")))

