from goose3 import Goose

url = 'http://americandigest.org/wp/skyway-paradise-open/'
g = Goose()
article = g.extract(url=url)
field = "authors"
author_list = getattr(article, field, None)

#Print Title & infered author(s)
print(article.title)
print("by")
print(author_list)