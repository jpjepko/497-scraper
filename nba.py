import requests
import json


def get_news(n: int, **kwargs):
    """Get latest news.

    Parameters
    ----------
    n : int
        Max number of articles to fetch
    
    Keyword Arguments
    -----------------
    sportSite : str
        Site to fetch (general) news from.
        Cannot be set with `player` or `team`
        Sites: nba, nba_canada, bleacher_report, espn, yahoo, slam
    player : str
        Fetch latest news about player.
        Cannot be set with `sportSite` or `team`
        Format as 'first-last`, e.g.: `cade-cunningham`
    team : str
        Fetch latest news about team.
        Cannot be set with `sportSite` or `news`
        Use name, not city (e.g. 'pistons' but not 'detroit')

    Returns
    ------
    list[dict[str, str]]
        Latest news in ascending order, each article is a dictionary
    """

    # Constants
    url = "https://nba-stories.herokuapp.com/news"
    validSites = ["nba", "nba_canada", "bleacher_report", "espn", "yahoo", "slam"]
    
    # Process kwargs
    if len(kwargs) > 1:
        raise Exception("Error: multiple kwargs passed in")
    
    for key, val in kwargs.items():
        key = key.lower()
        val = val.lower()
        if (key == "sportSites" and val in validSites) or (key == "player") or (key == "team"):
            url += f"/{key}/{val}"

    r = requests.get(url, params = {"limit": str(n)})
    if not r.ok:
        return []
   
    r.close()
    return r.json()

