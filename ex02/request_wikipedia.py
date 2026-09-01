import requests
import sys

SEARCH_URL = "https://en.wikipedia.org/w/api.php"
HEADERS = {
        "User-Agent": "walter/1.01"
    }


def get_content(title):
   
   params = {
      "action": "query",
      "titles": title,
      "prop": "extracts",
      "explaintext": True,
      "exintro": True,
      "format":"json"
   }

   response = requests.get(SEARCH_URL, params=params, headers=HEADERS, timeout=10)
   response.raise_for_status()

   data = response.json()
   pages = data["query"]["pages"]

   page = next(iter(pages.values()))

   if "missing" in page:
    raise ValueError(f"Article '{title}' was not found")
   
   content = page.get("extract", "").strip()

   if not content:
        raise ValueError(f"Article '{title}' contains no readable text")
   
   return content

def search_wikipedia(search_param):

    params = {
        "action": "opensearch",
        "search": search_param,
        "limit": 1,
        "format": "json",
        "namespace": 0

    }

    response = requests.get(SEARCH_URL, params=params, headers=HEADERS, timeout=10)
    response.raise_for_status()
    
    result = response.json()
    if not result[1]:
        raise ValueError(f"No search result found for {search_param}")
    
    return   result[1][0]


def main():
    

    if len(sys.argv) < 2:
        print("============== invalid input ==============")
        print("usage python(3) request_wikipedia.py <search_term>")
        sys.exit(1)

    args = sys.argv[1:]
    search_param = ' '.join(args).strip()

    if not search_param:
        print("Error: search cannot be empty") 
        sys.exit(1)
    
    filename = search_param.replace(" ", "_") + ".wiki"

    try:
        title = search_wikipedia(search_param)
        content = get_content(title)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

    except (requests.RequestException, ValueError, KeyError, IndexError) as error:
        print(f"Error: {error}") 
        sys.exit(1)

if __name__ == "__main__":
    main()