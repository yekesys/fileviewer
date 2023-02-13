
import code.filev_utils as fu
import code.run_filev


def call_format_line(loi, b, w, sd):
    print("trying:",loi)
    try:
        return fu.format_line(loi, b, w, sd)
    except fu.CharactersDoNotFitError as e:
        return str(e)


if __name__ == "__main__":
    print(fu.txt2loi("abc"))
    print(fu.txt2loi("ABC"))
    a = "123éàèðαא☺ꞅ"
    print(fu.txt2loi(a))
    print(fu.txt2loi(bytes(a, encoding="utf-8")))
    print(fu.txt2loi(bytes(a, encoding="utf-16")))
    print(fu.txt2loi(bytes(a, encoding="utf-32")))
    print(fu.txt2loi(bytes("123", encoding="ascii")))


    print(fu.loi2show(fu.txt2loi("abc"), "bin"))
    print(fu.loi2show(fu.txt2loi("abc"), "oct"))
    print(fu.loi2show(fu.txt2loi("abc"), "hex"))
    print(fu.loi2show(fu.txt2loi("abc"), "dec"))
    print(fu.loi2show(fu.txt2loi("abc")))

    for s in ["abc", "123", "éàèðα", "א☺ꞅ"]:
        for b in ["bin", "oct", "hex", "dec"]:
            print(fu.loi2show(fu.txt2loi(s), b))

    for s in ["abc", "123", "éàèðα", "א☺ꞅ"]:
        print(fu.display_loi(fu.txt2loi(s)))

    print(fu.display_loi(range(0,33)))

    #for s in ["abc", "123", "éàèðα", "א☺ꞅ", "abcdefgi"]:
    for s in ["éàèðα", "א☺ꞅ", ]:
        print(call_format_line(fu.txt2loi(s), "hex", 80, "R"))
        print(call_format_line(fu.txt2loi(s), "dec", 80, "L"))
        print(call_format_line(fu.txt2loi(s), "bin", 80, "L"))
        print(call_format_line(fu.txt2loi(s), "oct", 80, "L"))
        print(call_format_line(fu.txt2loi(s), "hex", 120, "R"))
        print(call_format_line(fu.txt2loi(s), "hex", 40, "R"))


