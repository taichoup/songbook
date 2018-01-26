import os, codecs
from bs4 import BeautifulSoup


input_directory = "E:/Docs/GitHub/songbook/songs"
output_directory = "E:/Docs/GitHub/songbook/songs_html_unique"

soup = BeautifulSoup("", "lxml")
body = soup.new_tag('body')
soup.insert(0, body)

for filename in os.listdir(input_directory):
    print "______\nTreating %s" % filename

    
    # soup = BeautifulSoup(features = "xml")
    title = soup.new_tag('h1')
    content = soup.new_tag('pre')
    body.insert(0, title)
    body.insert(1, content)

    try:


        with open("%s/%s" % (input_directory, filename), "r") as infile:
            chapter_title = infile.readline().strip()
            chapter_content = infile.read()
            title.insert(0, chapter_title)
            content.insert(1, chapter_content)




        outfile = codecs.open('../songs_html_unique/export.html', 'w+', encoding="utf-8")
        outfile.write(soup.prettify())
        outfile.close()


    except Exception as e:
        print e
        continue

print soup