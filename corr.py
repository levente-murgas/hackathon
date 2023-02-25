import pandas as pd
import json
import os
import matplotlib.pyplot as plt

def get_field_values(json_obj, field_name):
    """
    Returns a list of all values of the specified field in the JSON object
    with any level of nesting.
    """
    result = []
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if key == field_name:
                result.append(value)
            else:
                result.extend(get_field_values(value, field_name))
    elif isinstance(json_obj, list):
        for item in json_obj:
            result.extend(get_field_values(item, field_name))
    return result

records = []
for filename in os.listdir("data\matches"):
    with open(f'data\matches\{filename}', encoding="utf-8") as f:
        data = json.load(f)
    participants = get_field_values(data, 'participants')    
    if len(participants[0]) != 10:
        continue
    loser_team_kills = 0
    winner_team_kills = 0
    for player in participants[1]:
        if get_field_values(player, 'win')[0] == True:
            winner_team_kills += get_field_values(player, 'kills')[0]
        else:
            loser_team_kills += get_field_values(player, 'kills')[0]
    records.append([os.path.splitext(filename)[0], winner_team_kills, "Yes"])
    records.append([os.path.splitext(filename)[0], loser_team_kills, "No"])

df = pd.DataFrame(records,columns=['match_id','kill_count','win'])

# filter dataframe by kill_count >= 7
df = df[df['kill_count'] >= 7]

df = df.sort_values(by=['kill_count'], ascending=True)

# group by kill_count and sum wins and losses
grouped = df.groupby('kill_count')['win'].value_counts().unstack(fill_value=0)

# add percentage of wins column
grouped['win_percentage'] = grouped['Yes'] / (grouped['Yes'] + grouped['No'])

# filter groups with less than 2 matches
grouped_filtered = grouped[grouped.sum(axis=1) >= 15]

# plot data
plt.plot(grouped_filtered.index, grouped_filtered['win_percentage'], 'o-')
plt.xlabel('Kill Count')
plt.ylabel('Win Percentage')
plt.title('Win Percentage by Kill Count')
plt.show()

grouped_filtered.to_csv("kills_to_win.csv")