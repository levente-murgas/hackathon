import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import numpy as np

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
    loser_deaths = 0
    winner_deaths = 0
    loser_kills = 0
    winner_kills = 0
    loser_heal = 0
    winner_heal = 0
    winner_goldEarned = 0
    loser_goldEarned = 0
    with open(f'data\matches\{filename}', encoding="utf-8") as f:
        data = json.load(f)
    participants = get_field_values(data, 'participants')    
    if len(participants[0]) != 10:
        continue

    for player in participants[1]:
        if get_field_values(player, 'win')[0] == True:
            winner_kills += get_field_values(player, 'kills')[0]
            winner_deaths += get_field_values(player, 'deaths')[0]
            winner_heal += get_field_values(player, 'totalHeal')[0]
            winner_goldEarned += get_field_values(player, 'goldEarned')[0]
        else:
            loser_kills += get_field_values(player, 'kills')[0]
            loser_deaths += get_field_values(player, 'deaths')[0]
            loser_heal += get_field_values(player, 'totalHeal')[0]
            loser_goldEarned += get_field_values(player, 'goldEarned')[0]

    records.append([os.path.splitext(filename)[0], winner_goldEarned, "Yes"])
    records.append([os.path.splitext(filename)[0], loser_goldEarned, "No"])

df = pd.DataFrame(records,columns=['match_id','goldEarned','win'])


df = df.sort_values(by=['goldEarned'], ascending=True)
print(df)
df['goldEarned'] = df['goldEarned'] // 1000

# filter dataframe by goldEarned >= 30
df = df[df['goldEarned'] >= 30]

print(df)
# group by goldEarned and sum wins and losses
df = df.groupby('goldEarned')['win'].value_counts().unstack(fill_value=0)

print(df)
# add percentage of wins column
df['win_percentage'] = df['Yes'] / (df['Yes'] + df['No'])
print(df)

# filter groups with less than 15 matches
df = df[df.sum(axis=1) >= 3]
print(df)

# # calculate correlation between goldEarned and win_percentage
corr = np.corrcoef(df.index, df['win_percentage'])[0, 1]
print(corr)

# print(grouped_filtered)
# plot data
plt.plot(df.index, df['win_percentage'], 'o-')
plt.xlabel('Gold Earned')
plt.ylabel('Win Percentage')
plt.title('Win Percentage by Gold Earned')
plt.show()


df.to_csv("goldEarned_to_win.csv")