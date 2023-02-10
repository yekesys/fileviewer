
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
    :param loi: a list of integers
                Each integer is the ordinal value of a character
    :param base: One of the following: "bin", "oct", "dec", "hex"
    """
    print(f"Converting to {base}")
    if base == "bin":
        return [bin(i)[2:] for i in loi]
    elif base == "oct":
        return [oct(i)[2:] for i in loi]
    elif base == "dec":
        return [str(i) for i in loi]
    elif base == "hex":
        return [better_hex(i) for i in loi]
    else:
        print(f"Unknown base: {base}, assume decimal")
        return [str(i) for i in loi]

    
def display_one_char(i: int) -> str:
    """
    Display an integer as the corresponding character,
    if the character can be displayed, 
    otherwise display the hex value between square brackets
    :param i: the ordinal value of a character
    """
    if i in range(0, 32):
        return CTRL_CHARS[i]
    elif i == 32:
        return "[ ]"
        #return "."
    elif i in range(33, 126):
        return chr(i)
    elif i == 127:
        return "[DEL]"
    elif i in range(128, 687):
        return chr(i)
    else:
        return "[" + better_hex(i) + "]"


def display_loi(loi: list[int]) -> list[str]:
    """
    Return a representation for each integer in the list
    :param loi: a list of integers
                Each integer is the ordinal value of a character
    """
    return [display_one_char(i) for i in loi]


def format_line(
        loi: list[int], 
        base: str,
        width: int,
        side: str,
        ) -> str:
    """
    Format a line
    Typically, the loi has 4 or 8 elements
    Show the loi elements in the one of the bases
    and show the characters on the side, if they can be printed
    """

    main = ' '.join(loi2show(loi, base))
    side = ' '.join(display_loi(loi))
    if side == "L":
        return side + ' | ' + main
    else:
        return main + ' | ' + side

if __name__ == "__main__":
    print("module executed as main")

