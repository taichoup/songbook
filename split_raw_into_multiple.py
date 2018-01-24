_filename = "raw_2018_01_24.txt"

with open(_filename, "r") as fo:
    start = 0
    op = ""
    cntr = 1

    for x in fo.read().split("\n"):
        if x == "= = = = = = = = = = = = = = = = = = = = = = = = = =":
            if (start == 1):
                with open(str(cntr) + ".txt", "w") as opf:
                    print "writing file %s" % cntr
                    opf.write(op)
                    opf.close()
                    op = ""
                    cntr += 1
            else:
                start = 1
        else:
            op = op + "\n" + x

    fo.close()