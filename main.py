import pandas as pd
import os

# Gets the data from the indicated league
def analyzeLeague(leagueCountry):
    dfs = []
    filenames = os.listdir('data' + '/' + leagueCountry)
    for file in filenames:
        df = pd.read_csv('data/' + leagueCountry + "/" + file)
        dfs.append(df)
    return dfs

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

if __name__ == "__main__":
    dfs = (analyzeLeague('Germany'))
    print(getTop5TeamsByPoint(dfs))