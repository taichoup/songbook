import os

directory = "E:/Docs/GitHub/songbook"

for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        # print(os.path.join(directory, filename))
        fo = open(filename, "r")
        songname = "%s.txt" % fo.readlines()[1].strip()
        print songname
        fo.close()
        try:
            os.rename(filename, songname)
        except Exception as e:
            continue

    else:
        continue