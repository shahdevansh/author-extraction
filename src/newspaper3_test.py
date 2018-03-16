from newspaper import Article

# Fetch & parse Article
url = 'http://americandigest.org/wp/skyway-paradise-open/'
a = Article(url, language='en')
a.download()
a.parse()

# Print Title & infered author(s)
print(a.title)
print("by")
print(a.authors)