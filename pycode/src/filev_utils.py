# pylint: disable=C0305
"""
to do:
continuation character
pad out the line at the end of the file
decimals over three characters

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


class CharactersDoNotFitError(Exception):
    """
    Raise when trying to put too many characters in a given width
    """
    def __init__(self, width=0, loi_len=0):
        if loi_len:
            self.message  = f"Cannot fit {loi_len} characters "
        else:
            self.message  = "Cannot fit all characters "
        if width:
            self.message += f"on a line of width {width}"
        else:
            self.message += "on one line"
        self.message += ".  Try a higher width or display less characters"
        super().__init__(self.message)


def detect_encoding(input_string: bytes) -> str:
    """
    An attempt to detect the utf encoding
    """
    if input_string[0] == 255 and input_string[1] == 254:
        if input_string[2] == 0:
            return "utf-32"
        return "utf-16"
    return "utf-8 or other"


def txt2loi(input_string) -> list[int]:
    """
    Convert a string or bytes into a list of integers (loi)
    """
    #print(type(input_string))
    if isinstance(input_string, str):
        return [ord(c) for c in input_string]
    if isinstance(input_string, bytes):
        #print(detect_encoding(input_string))
        return list(input_string)
    print("Expecting types str or bytes, found:",type(input_string))
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
    #print(f"Converting to {base}")
    if base == "bin":
        return [bin(i)[2:] for i in loi]
    if base == "oct":
        return [oct(i)[2:] for i in loi]
    if base == "dec":
        return [str(i) for i in loi]
    if base == "hex":
        return [better_hex(i) for i in loi]
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
    if i == 32:
        return "[ ]"
        #return "."
    if i in range(33, 126):
        return chr(i)
    if i == 127:
        return "DEL"
    if i in [132, 133, ]:
        # 'blacklist' some characters that do not print right
        return ""
    if i in range(128, 687):
        return chr(i)
    return ""


def display_loi(loi: list[int]) -> list[str]:
    """
    Return a representation for each integer in the list
    :param loi: a list of integers
                Each integer is the ordinal value of a character
    """
    return [display_one_char(i) for i in loi]


def format_ln_guess_length(loi, one_side_char_width, one_ordinal_width):
    """
    working on it.  Maybe will not keep
    """
    return len(loi) * (one_side_char_width + one_ordinal_width) + 3


def format_ln_does_it_fit(loi, one_side_char_width, one_ordinal_width, width):
    """
    working on it.  Maybe will not keep
    """
    return format_ln_guess_length(loi, one_side_char_width, one_ordinal_width) > width


def format_line(
        loi: list[int],
        base: str,
        width: int=80,    # do I really need this?
        side: str="R",
        ) -> str:
    """
    Format a line
    Typically, the loi has 4 or 8 elements
    Show the loi elements in the one of the bases
    and show the characters on the side, if they can be printed
    Assume
       A max of 4 characters to display ordinals
       A max of 3 characters to display characters
       Two spots at beginning of line to show continuation ".."
       Separator " | " between ordinals and side
       Simple space as separator everywhere
    """
    # define a few things
    # Note that if a char needs more than the width below, we add a line
    char_sep = " "
    side_sep = " | "
    one_side_char_width = 3
    if base in ["dec", "oct", "hex"]:
        one_ordinal_width = 2
    elif base in ["bin", ]:
        one_ordinal_width = 8
    else:  # always a default
        one_ordinal_width = 2

    # can it all fit on one line?
    if format_ln_does_it_fit(loi, one_side_char_width, one_ordinal_width, width):
        #print("Displaying ",loi)
        raise CharactersDoNotFitError(width, len(loi))

    # list of strings
    loc_ordi = loi2show(loi, base)
    loc_side = display_loi(loi)

    # Allow for up to 8 lines to display
    max_lines = 8
    the_ordinals  = [[] for i in range(max_lines)]
    the_ordinals_str = [[] for i in range(max_lines)]
    chars_on_side = []

    # index 0 is right-most part of the number
    for one_ordi,one_side in zip(loc_ordi, loc_side):
        #print(one_ordi, one_side)
        c = one_ordi
        for i in range(max_lines):
            #print("======")
            #print(c)
            #print(the_ordinals)
            the_ordinals[i].append(c[-one_ordinal_width:].rjust(one_ordinal_width))
            c = c[:-one_ordinal_width]
            #print(c)
            #print(the_ordinals)
            #print("======")
        chars_on_side.append(one_side.center(one_side_char_width))
        #print(one_ordi, one_side)

    #print("input:")
    #print(loi)
    #print("results:")
    for i in range(max_lines):
        the_ordinals_str[i] = char_sep.join(the_ordinals[i])
        #print(the_ordinals_str[i])
    chars_on_side_str = char_sep.join(chars_on_side)
    #print(chars_on_side_str)
    #print("done")

    chars_on_side_curr_str = chars_on_side_str 
    built_output = ""
    line_sep = "" 
    for one_ord_str in the_ordinals_str[::-1]:
        if one_ord_str.lstrip(" "):
            if side == "L":
                built_output += line_sep + chars_on_side_curr_str + side_sep + one_ord_str + "[eol]"
            else:
                built_output += line_sep + one_ord_str + side_sep + chars_on_side_curr_str + "[eol]"
            # Print this just once, now put spaces
            chars_on_side_curr_str = ''.ljust(len(chars_on_side_str))
            # Add line separator
            line_sep = "\n"
    return built_output
    # this has to be across 8 lines


def view_file(
        file_name: str,
        base: str = "hex",
        chunk_size: int = 8,
        side: str = "R",
        ):
    with open(file_name, "rb") as f:
        while ch_bytes := f.read(chunk_size):
            print(format_line(
                loi=txt2loi(ch_bytes),
                base=base,
                width=10000,  # do I really need this?
                side=side,
                ))



	

if __name__ == "__main__":
    print("module executed as main")

