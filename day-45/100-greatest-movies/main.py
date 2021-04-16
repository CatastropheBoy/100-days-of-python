from bs4 import BeautifulSoup
import requests

# This doesn't actually work since Empire made their site scraping hostile

resp = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(resp.text, "html.parser")
print(soup.prettify())

all_movies = soup.find_all(name="h3")
print(all_movies)
movies = [movie.getText() for movie in all_movies]

movies.reverse()

with open("movies.txt", "w") as f:
    for movie in movies:
        f.write(f"{movie}\n")
