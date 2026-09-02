import sys
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://en.wikipedia.org/wiki/"


def get_page(title):
    url = BASE_URL + title.replace(" ", "_")

    response = requests.get(
        url,
        headers={"User-Agent": "walter/1.0"}
    )

    if response.status_code != 200:
        return None

    return BeautifulSoup(response.text, "lxml")


def find_first_link(soup):
    content = soup.find("div", class_="mw-parser-output")

    if content is None:
        return None

    for element in content.children:

        if element.name in ("h2", "h3"):
            break

        if element.name != "p":
            continue

        for link in element.find_all("a", href=True):

            if link.find_parent("i") or link.find_parent("em"):
                continue

            if link.find_parent("sup"):
                continue

            href = link["href"]

            if not href.startswith("/wiki/"):
                continue

            target = href[len("/wiki/"):]
            
            if ":" in target:
                continue

            return target.replace("_", " ")

    return None


def build_road(start):
    current = start
    road = []
    visited = set()

    while True:
        if current in visited:
            print("Cycle detected.")
            break

        visited.add(current)
        road.append(current)

        if current.lower() == "philosophy":
            break

        soup = get_page(current)

        if soup is None:
            print(f"Could not retrieve: {current}")
            break

        next_article = find_first_link(soup)

        if next_article is None:
            print(f"No valid link found in: {current}")
            break

        current = next_article

    return road


def main():
    if len(sys.argv) < 2:
        print("Usage: python roads_to_philosophy.py <article>")
        return

    start = " ".join(sys.argv[1:])

    road = build_road(start)

    for index, article in enumerate(road, start=1):
        print(f"{index}. {article}")

    if road and road[-1].lower() == "philosophy":
        print(f"\nRoad length: {len(road)} articles")


if __name__ == "__main__":
    main()