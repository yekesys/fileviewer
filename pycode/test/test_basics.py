import pytest
import sys

sys.path.append("code")
import filev_utils


a = "123éàèðαא☺ꞅ"

input_data = [ ( "123éàèðαא☺ꞅ",
                 [49, 50, 51, 233, 224, 232, 240, 945, 1488, 9786, 42885],
               ),
               ( bytes("123éàèðαא☺ꞅ", encoding="utf-8"),
                 [49, 50, 51, 195, 169, 195, 160, 195, 168, 195, 176, 206, 177, 215, 144, 226, 152, 186, 234, 158, 133],
               ),
               ( bytes("123éàèðαא☺ꞅ", encoding="utf-16"),
                 [255, 254, 49, 0, 50, 0, 51, 0, 233, 0, 224, 0, 232, 0, 240, 0, 177, 3, 208, 5, 58, 38, 133, 167],
               ),
               ( bytes("123éàèðαא☺ꞅ", encoding="utf-32"),
                 [255, 254, 0, 0, 49, 0, 0, 0, 50, 0, 0, 0, 51, 0, 0, 0, 233, 0, 0, 0, 224, 0, 0, 0, 
                  232, 0, 0, 0, 240, 0, 0, 0, 177, 3, 0, 0, 208, 5, 0, 0, 58, 38, 0, 0, 133, 167, 0, 0
                 ],
               ),
               ( "",
                 [],
               ),
             ]
@pytest.mark.parametrize("input_param", input_data)
def test_txt2loi(input_param):
    param_in, expected = input_param
    assert expected == filev_utils.txt2loi(param_in)
    

input_data = [ ( "str",
                 [49, 50, 51],
                 ["49", "50", "51"],
               ),
               ( "bin",
                 [49, 50, 51],
                 ["110001", "110010", "110011"],
               ),
               ( "oct",
                 [49, 50, 51],
                 ["61", "62", "63"],
               ),
               ( "hex",
                 [49, 50, 51],
                 ["31", "32", "33"],
               ),
               ( "",
                 [49, 50, 51],
                 ["49", "50", "51"],
               ),
               ( "anything",
                 [49, 50, 51],
                 ["49", "50", "51"],
               ),
               ( "bin",
                 [1488, 9786, 42885],
                 ["10111010000", "10011000111010", "1010011110000101"],
               ),
               ( "oct",
                 [1488, 9786, 42885],
                 ["2720", "23072", "123605"],
               ),
               ( "hex",
                 [1488, 9786, 42885],
                 ["5D0", "263A", "A785"],
               ),
               ( "dec",
                 [1488, 9786, 42885],
                 ["1488", "9786", "42885"],
               ),
             ]
@pytest.mark.parametrize("input_param", input_data)
def test_loi2show(input_param):
    base, input_loi, expected = input_param
    assert expected == filev_utils.loi2show(input_loi, base)


input_data = [ ( [97, 98, 99],
                 ["a", "b", "c"],
               ),
               ( [49, 50, 51],
                 ["1", "2", "3"],
               ),
               ( [233, 224, 232, 240, 945],
                 #["[E9]", "[E0]", "[E8]", "[F0]", "[3B1]"],
                 #[ "é", "à", "è", "ð", "[3B1]"],
                 [ "é", "à", "è", "ð", ""],
               ),
               ( [1488, 9786, 42885],
                 #["[5D0]", "[263A]", "[A785]"],
                 ["", "", ""],
               ),
               ( range(0, 33),
                 ["NUL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL", "BS", "HT", "LF", "VT", "FF", "CR", "SO", "SI", "DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US", "[ ]"],
               ),
               ( [127, ],
                 ["DEL", ],
               ),
             ]
@pytest.mark.parametrize("input_param", input_data)
def test_loi2show(input_param):
    input_loi, expected = input_param
    assert expected == filev_utils.display_loi(input_loi)



input_data = [ ( "abc", "utf-8 or other" ),
               ( bytes("abc", encoding="utf-8"), "utf-8 or other"),
               ( bytes("abc", encoding="utf-16"), "utf-16"),
               ( bytes("abc", encoding="utf-32"), "utf-32"),
             ]
@pytest.mark.parametrize("input_param", input_data)
def test_detect_encoding(input_param):
    s, expected = input_param
    assert expected == filev_utils.detect_encoding(s)


#input_data = [ "abcde",
#               "w35klasdfkéàèôêĝŵ^bä",
#               "123éàèðαא☺ꞅ",
#             ]
#@pytest.mark.parametrize("input_param", input_data)
#def test_guess_length(input_param):
#    loi = filev_utils.txt2loi(input_param)
#    assert len(filev_utils.format_line(loi, "bin", 80, "R")) == filev_utils.format_ln_guess_length(loi, 3, 8)
#    assert len(filev_utils.format_line(loi, "oct", 80, "R")) == filev_utils.format_ln_guess_length(loi, 3, 4)
#    assert len(filev_utils.format_line(loi, "dec", 80, "R")) == filev_utils.format_ln_guess_length(loi, 3, 4)
#    assert len(filev_utils.format_line(loi, "hex", 80, "R")) == filev_utils.format_ln_guess_length(loi, 3, 4)


