import requests
import json
from bs4 import BeautifulSoup

api_key = "RGAPI-60fe1387-7dff-489e-8403-eb737a5a7083"
summoner_name = "Graaland"
region_code = "eun1"
region = "europe"
queue = "RANKED_SOLO_5x5"  # or "RANKED_FLEX_SR" for Flex queue

class Summoner:
    def __init__(self, summoner_id: str, puuid: str, region_code: str):
        self.summoner_id = summoner_id
        self.puuid = puuid
        self.region_code = region_code
    
    def get_match_list(self):
        # Get match list from summoner ID
        url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{self.puuid}/ids?start=0&count=20&api_key={api_key}"
        response = requests.get(url)
        matchlist_data = json.loads(response.text)
        return matchlist_data

    def get_tier(self):
        # # Get summoner's league entry for a specific queue
        url = f"https://{self.region_code}.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.summoner_id}?api_key={api_key}"
        response = requests.get(url)
        rank_data = json.loads(response.text)
        # # Extract relevant information from rank_data
        if len(rank_data) > 0:
            return rank_data[0]["tier"]
        else:
            print(f"{summoner_name} is currently unranked in {queue}.")

        

def get_summoner(_region_code, summoner_name, api_key):
    # Get summoner ID from summoner name
    url = f"https://{region_code}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}"
    response = requests.get(url)
    summoner_data = json.loads(response.text)
    puuid = summoner_data["puuid"]
    summoner_id = summoner_data["id"]
    return Summoner(summoner_id=summoner_id,puuid=puuid, region_code=_region_code)



def get_match_details(match_id: str):
    # # Get match details from match ID
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
    response = requests.get(url)
    match_data = json.loads(response.text)
    return match_data

def serialize_match(match: dict):
    with open("sample.json", "w") as outfile:
        json.dump(match, outfile)

# # Code sample
krisz = get_summoner(region_code,summoner_name=summoner_name,api_key=api_key)
matches = krisz.get_match_list()
serialize_match(get_match_details(matches[0]))


# # Send a request to the webpage
# url = 'https://www.op.gg/leaderboards/tier'
# response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# # Use BeautifulSoup to parse the HTML content of the page
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all the elements with the class name "summoner-name"
# summoner_names = soup.find_all('strong', {'class': 'summoner-name'})

# # Print the results
# for name in summoner_names:
#     print(name.text)

