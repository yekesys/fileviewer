
"""

Glossary:
 - loi = list of integers

"""

def txt2loi(s) -> list[int]:
    """
    Convert a string or bytes into a list of integers (loi)
    """
    return [ord(c) for c in s]


