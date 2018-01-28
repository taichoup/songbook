import os

directory = "E:\Docs\GitHub\songbook\songs"

equiv = {}

for filename in os.listdir(directory):

    if filename.endswith(".txt"): 

        full_path = os.path.join(directory, filename)
        
        with open(full_path, "r") as fo:
            songname = fo.readlines()[0].strip()

            try:
                # os.rename(full_path, "%s.txt" % songname)
                equiv[filename] = "%s.txt" % songname
            except Exception as e:
                print e
                continue


        os.rename(filename, equiv[filename])

    else:
        continue