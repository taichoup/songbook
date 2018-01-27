from bs4 import BeautifulSoup, Doctype, Declaration


# # /////////////////////////////////
# # CHANGING TAG NAMES AND ATTRIBUTES
# # /////////////////////////////////

# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'lxml')
# tag = soup.b

# print tag
# # <b class="boldest">Extremely bold</b>

# tag.name = "blockquote"
# tag['class'] = 'verybold'
# tag['id'] = 1

# print tag
# # <blockquote class="verybold" id="1">Extremely bold</blockquote>


# # //////////////////
# # MODIFYING .string
# # //////////////////


# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'

# soup = BeautifulSoup(markup, "lxml")

# tag = soup.a
# tag.string = "New link text."

# print tag
# # <a href="http://example.com/">New link text.</a>

# # /////////
# # append()
# # /////////

# soup = BeautifulSoup("<a>Foo</a>", "lxml")
# soup.a.append("Bar")

# print soup.prettify()
# # <html><body><a>FooBar</a></body></html>

# print soup.a.contents
# # [u'Foo', u'Bar']



soup = BeautifulSoup('<!doctype html><html lang="en"><head><meta charset="utf-8" /> <title>Your Book Title</title><link rel="stylesheet" href="style.css"  type="text/css" /></head><body></body>', 'lxml')
print soup.prettify()
print soup.html
print soup.body
print soup.div

print Doctype("html")