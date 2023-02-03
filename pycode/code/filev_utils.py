
"""

Glossary:
 - loi = list of integers

"""


CTRL_CHARS = { 0: "NUL",
               1: "SOH",
               2: "STX",
               3: "ETX",
               4: "EOT",
               5: "ENQ",
               6: "ACK",
               7: "BEL",
               8: "BS",
               9: "HT",
               10: "LF",
               11: "VT",
               12: "FF",
               13: "CR",
               14: "SO",
               15: "SI",
               16: "DLE",
               17: "DC1",
               18: "DC2",
               19: "DC3",
               20: "DC4",
               21: "NAK",
               22: "SYN",
               23: "ETB",
               24: "CAN",
               25: "EM",
               26: "SUB",
               27: "ESC",
               28: "FS",
               29: "GS",
               30: "RS",
               31: "US",
               }

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

def better_hex(i: int) -> str:
    """
    My preferred representation of hex
    """
    return hex(i)[2:].upper()

def loi2show(loi: list[int], base: str = "dec") -> list[str]:
    """
    Return a list of strings, with each string being
    the representation of the integer
    :param base: One of the following: "bin", "oct", "dec", "hex"
    """
    if base == "bin":
        print(f"Converting to {base}")
        return [bin(i)[2:] for i in loi]
    elif base == "oct":
        print(f"Converting to {base}")
        return [oct(i)[2:] for i in loi]
    elif base == "dec":
        print(f"Converting to {base}")
        return [str(i) for i in loi]
    elif base == "hex":
        print(f"Converting to {base}")
        return [better_hex(i) for i in loi]
    else:
        print(f"Unknown base: {base}, assume decimal")
        return [str(i) for i in loi]

    
def display_one_char(i: int) -> str:
    """
    Display an integer as the corresponding character,
    if the character can be displayed, 
    otherwise display a ...
    """
    if i in range(0, 32):
        return CTRL_CHARS[i]
    if i == 32:
        return "[ ]"
        #return "."
    if i in range(33, 126):
        return chr(i)
    else:
        return "[" + better_hex(i) + "]"


def display_loi(loi: list[int]) -> list[str]:
    return [display_one_char(i) for i in loi]


if __name__ == "__main__":
    print(txt2loi("abc"))
    print(txt2loi("ABC"))
    a = "123éàèðαא☺ꞅ"
    print(txt2loi(a))
    print(txt2loi(bytes(a, encoding="utf-8")))
    print(txt2loi(bytes(a, encoding="utf-16")))
    print(txt2loi(bytes(a, encoding="utf-32")))
    print(txt2loi(bytes("123", encoding="ascii")))


    print(loi2show(txt2loi("abc"), "bin"))
    print(loi2show(txt2loi("abc"), "oct"))
    print(loi2show(txt2loi("abc"), "hex"))
    print(loi2show(txt2loi("abc"), "dec"))
    print(loi2show(txt2loi("abc")))

    for s in ["abc", "123", "éàèðα", "א☺ꞅ"]:
        for b in ["bin", "oct", "hex", "dec"]:
            print(loi2show(txt2loi(s), b))

    for s in ["abc", "123", "éàèðα", "א☺ꞅ"]:
        print(display_loi(txt2loi(s)))

    print(display_loi(range(0,33)))



