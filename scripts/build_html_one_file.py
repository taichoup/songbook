import os, codecs
from bs4 import BeautifulSoup


input_directory = "E:/Docs/GitHub/songbook/songs"
output_directory = "E:/Docs/GitHub/songbook/songs_html_unique"
ebook_title = "Manu's Songbook"

soup_string = '<!doctype html><html lang="en"><head><meta charset="utf-8" /> <title>%s</title><link rel="stylesheet" href="style.css"  type="text/css" /></head><body><div id="toc"><h2>Manu&apos;s Songbook<br /></h2><ul></ul></div><div class="pagebreak"></div></body>' % ebook_title

soup = BeautifulSoup(soup_string, "lxml")

body = soup.body
toc = soup.ul

print toc

counter = 0 # this is used to set id attributes for song titles.
list_of_songs = {} # this is used to populate the TOC at the end of the loop

for filename in os.listdir(input_directory):

    counter += 1

    print "Treating %s" % filename

    # create HTML tags for the song...
    title = soup.new_tag('h3')
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
            list_of_songs[chapter_title] = title['id'] # add to the TOC while we're at it
            content.insert(1, chapter_content)

            #create entry in table of contents for the current song
            toc_entry = soup.new_tag("li")
            toc_entry_link = soup.new_tag("a", href="#%s" % title['id'])
            toc.append(toc_entry)
            toc_entry.append(toc_entry_link)
            toc_entry_link.string = chapter_title


        # Write all of this to a unique html file
        outfile = codecs.open('../songs_html_unique/export.html', 'w+', encoding="utf-8")
        outfile.write(soup.prettify())
        outfile.close()

    except Exception as e:
        print e
        continue

print list_of_songs