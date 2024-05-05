import requests
from lxml import html
from rich import print
session = requests.session()
session.headers.update(
    {
        "user-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "origin": "https://www.azlyrics.com",
    }
)

session.get("https://www.azlyrics.com")


def search(query):
    """
    Search for songs on azlyrics.com
    """

    url = f"https://search.azlyrics.com/search.php?q={query}&w=songs&p=1&x=ed9c0064dc3df114b5d2967c7a2eebaf28f631cd07a3f97ba1962ff8323b8843"
    response = session.get(url)
    html_content = response.content  # Extract HTML content from the response

    # Parse the HTML content using lxml
    tree = html.fromstring(html_content)
    songs = []
    # Extract song names using XPath
    song_names = tree.xpath("//td[@class='text-left visitedlyr']/a/span/b/text()")
    song_artists = tree.xpath("//td[@class='text-left visitedlyr']/a/b/text()")
    # print(song_artists)
    # Extrtact song link using XPath
    song_links = tree.xpath("//td[@class='text-left visitedlyr']/a/@href")
    for song in song_names:
        songs.append(
            {
                "name": song.strip().replace('"', ''),
                "artist": song_artists[song_names.index(song)],
                "url": song_links[song_names.index(song)],
            }
        )
    return songs


