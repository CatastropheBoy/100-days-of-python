from bs4 import BeautifulSoup
import requests

# with open("./website.html", encoding="utf8") as f:
#     content = f.read()

# soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

# all_anchors = soup.find_all(name="a")
# print(all_anchors)

# for tag in all_anchors:
#     print(tag.getText())

# for tag in all_anchors:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name_tag = soup.select_one(selector="#name")
# print(name_tag)

# headings = soup.select(selector=".heading")
# print(headings)

resp = requests.get("https://news.ycombinator.com/")

yc_page = resp.text

soup = BeautifulSoup(yc_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

most_points = article_upvotes.index(max(article_upvotes))
print(article_texts[most_points])
print(article_links[most_points])