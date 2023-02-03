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





