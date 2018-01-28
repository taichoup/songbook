import os
from bs4 import UnicodeDammit

ml = []

input_directory = "E:/Docs/GitHub/songbook/songs_mangled"

for filename in os.listdir(input_directory):
    # dammit = UnicodeDammit(filename)
    # print dammitfor filename in os.listdir(input_directory):.unicode_markup
    # print dammit.original_encoding
    # print dammit



    # filename.decode("windows-1252")
    # print filename.encode("utf-8")

    print filename.decode("windows-1252").encode("utf-8")
    ml.append(filename.decode("windows-1252").encode("utf-8"))
print ml