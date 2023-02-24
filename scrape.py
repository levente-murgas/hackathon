import requests
import json
import socket

socket.getaddrinfo('localhost', 8080)
api_key = "RGAPI-60fe1387-7dff-489e-8403-eb737a5a7083"
summoner_name = "krisz2010"
region = "eune"
queue = "RANKED_SOLO_5x5"  # or "RANKED_FLEX_SR" for Flex queue


# Get summoner ID from summoner name
url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}"
response = requests.get(url)
summoner_data = json.loads(response.text)
summoner_id = summoner_data["accountId"]

# Get match list from summoner ID
url = f"https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{summoner_id}?endIndex=10&api_key={api_key}"
response = requests.get(url)
matchlist_data = json.loads(response.text)

# Get match details from match ID
for match in matchlist_data["matches"]:
    match_id = match["gameId"]
    url = f"https://{region}.api.riotgames.com/lol/match/v4/matches/{match_id}?api_key={api_key}"
    response = requests.get(url)
    match_data = json.loads(response.text)
    # Extract relevant information from match_data
    # Store the data in a database or a file


# Get summoner's league entry for a specific queue
url = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?queue={queue}&api_key={api_key}"
response = requests.get(url)
rank_data = json.loads(response.text)

# Extract relevant information from rank_data
if len(rank_data) > 0:
    tier = rank_data[0]["tier"]
    division = rank_data[0]["rank"]
    lp = rank_data[0]["leaguePoints"]
    print(f"{summoner_name} is currently in {tier} {division}, with {lp} LP.")
else:
    print(f"{summoner_name} is currently unranked in {queue}.")
