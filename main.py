import pandas as pd
import os
import matplotlib.pyplot as plt


# Gets the data from the indicated league
def analyzeLeague(leagueCountry):
    dfs = []
    filenames = os.listdir('data' + '/' + leagueCountry)
    for file in filenames:
        df = pd.read_csv('data/' + leagueCountry + "/" + file)
        dfs.append(df)
    return dfs

# gets the top 10 Teams by Points ever in the specific league
def getTop5TeamsByPoint(dfs):
    topTeams = []
    years = list(range(2006,2024))
    for i in range(len(dfs)):

        temp = {
            'Team': dfs[i].iloc[0]['Squad'],
            'Points': dfs[i].iloc[0]['Pts'],
            'Year': years[i]
        }
        topTeams.append(temp)
    
    top10Teams = sorted(topTeams, key=lambda d: d['Points'], reverse=True)[:10]

    return top10Teams

# Gets the golden boot analysis from all the seasons for the specified league
def goldenBoot(dfs):
    topData = []
    numberGoldenBoots = {}
    years = list(range(2006,2024))

    for i in range(len(dfs)):
        topScorer = dfs[i]['Top Team Scorer'].to_list()
        maxVal = 0
        playerName = 'name'
        for scorer in topScorer:
            temp = scorer.split(' - ')
            if int(temp[1]) > maxVal:
                maxVal = int(temp[1])
                playerName = temp[0]
        topData.append(
            {
                'Name': playerName,
                'Goals': maxVal,
                'Year': years[i]
            }
        )
        if playerName in numberGoldenBoots:
            numberGoldenBoots[playerName] += 1
        else:
            numberGoldenBoots[playerName] = 1

        top10GoalScorers = sorted(topData, key=lambda d: d['Goals'], reverse=True)[:10]

        
    return top10GoalScorers, numberGoldenBoots

def plotGoldenBoots(country, data):
    players = list(data.keys())
    goals = list(data.values())

    # Create the bar plot
    plt.figure(figsize=(12, 8))
    plt.bar(players, goals)
    plt.xlabel('Players')
    plt.ylabel('Golden Boots')
    plt.title('Golden Boots by Players')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(range(0, max(goals) + 1))
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    countries = ['Germany', 'England', 'France', 'Spain', 'Italy']
    #dfs = (analyzeLeague(countries[1]))
    #topTeams = getTop5TeamsByPoint(dfs)
    #top10scorers, goldenBoots = goldenBoot(dfs)
    #plotGoldenBoots(countries[1], goldenBoots)
    for country in countries:
        dfs = (analyzeLeague(country))
        topTeams = getTop5TeamsByPoint(dfs)
        top10scorers, goldenBoots = goldenBoot(dfs)
        plotGoldenBoots(country, goldenBoots)


    
