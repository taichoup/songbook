import os, codecs
from bs4 import BeautifulSoup


input_directory = "E:/Docs/GitHub/songbook/songs"
output_directory = "E:/Docs/GitHub/songbook/songs_html_unique"
ebook_title = "Manu's Songbook"

soup_string = '<!doctype html><html lang="en"><head><meta charset="utf-8" /> <title>%s</title><link rel="stylesheet" href="style.css"  type="text/css" /></head><body></body>' % ebook_title

soup = BeautifulSoup(soup_string, "lxml")

body = soup.body

counter = 0 # this is used to set id attributes for song titles.

for filename in os.listdir(input_directory):

    counter += 1

    print "\nTreating %s" % filename

    # create HTML tags for the song...
    title = soup.new_tag('h2')
    title['id'] = "song_%d" % counter
    content = soup.new_tag('pre')
    page_break = soup.new_tag('div')
    page_break['class'] = "pagebreak"

    # ... and add them to the document
    body.append(title)
    body.append(content)
    body.append(page_break)

    try:

        # Fill in the HTML tags with the right values from the files in the directory
        with open(u"%s/%s" % (input_directory, filename), "r") as infile:
            chapter_title = infile.readline().strip()
            chapter_content = infile.read()
            title.insert(0, chapter_title)
            content.insert(1, chapter_content)


        # Write all of this to a unique html file
        outfile = codecs.open('../songs_html_unique/export.html', 'w+', encoding="utf-8")
        outfile.write(soup.prettify())
        outfile.close()


    except Exception as e:
        print e
        continue