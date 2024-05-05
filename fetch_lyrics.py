import requests
from bs4 import BeautifulSoup as bs
from rich import print
session = requests.session()
session.headers.update({'user-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36', 'Accept': '*/*', 'Connection': 'keep-alive', 'origin': 'https://z3.fm'})

def fetch_lyrics(url):
    """
    Fetch lyrics from a given URL
    """
    html = session.get(url)
    html.encoding = 'utf-8'
    parsed = bs(html.text, "lxml")

    # Find the div containing the lyrics (empty class)
    lyrics_div = parsed.select("div.container.main-page div.row div.col-xs-12.col-lg-8.text-center div:nth-child(8)")
    # print(lyrics_div)
    # Check if the last div element exists and has no class
    if lyrics_div:
        # Extract the text content of the div and strip any leading/trailing whitespace
        lyrics_text = lyrics_div[0].get_text(separator="\n", strip=True)
        # print(lyrics_text)
        return lyrics_text
    else:
        print("Lyrics not found or unable to fetch.")


if __name__ == "__main__":
    # Example usage
    song_url = "https://www.azlyrics.com/lyrics/miyagix/minor.html"
    lyrics = fetch_lyrics(song_url)
    # print(lyrics)
