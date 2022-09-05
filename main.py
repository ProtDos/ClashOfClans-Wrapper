import requests

headers = {
    'Accept' : 'application/json',
    'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijk5MGY2YWMxLTcxMDgtNGIyNy1hZjAzLTc5ZWUzMWYwNTk1MSIsImlhdCI6MTY2MjAxNTg5MSwic3ViIjoiZGV2ZWxvcGVyLzYyMzc1OTk4LWNiOTEtODU5MS0zZGZlLTQ4ZmI0MDMwNDhmMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjkxLjI0OS4yMzEuOTYiXSwidHlwZSI6ImNsaWVudCJ9XX0.gvuvQmjcVGtwryqeRoY_23zFlbquQMgucyC-DYI9L82xHh63k0onq1Ozal2RnxicVFjOfUD-JOtsPRCTSjdCrg'
}

tag = "%239YQR2LPV"
clanTag = ""
warTag = ""
leagueID = ""
seasonID = ""
locationID = ""

############ Player



def get_userTrophies(tag):
    response = requests.get(f'https://api.clashofclans.com/v1/players/{tag}', headers=headers)
    user_json = response.json()
    return user_json['trophies']

def get_userName(tag):
    response = requests.get(f'https://api.clashofclans.com/v1/players/{tag}', headers=headers)
    return response.json()


############ Leage
def get_leagueRank(leagueId, seasonId):
    response = requests.get(f'https://api.clashofclans.com/v1/leagues/{leagueId}/seasons/{seasonId}', headers=headers)
    return response.json()
def get_leagueInfo(leagueId):
    response = requests.get(f'https://api.clashofclans.com/v1/leagues/{leagueId}', headers=headers)
    return response.json()
def get_leagueSeasons(leagueId):
    response = requests.get(f'https://api.clashofclans.com/v1/leagues/{leagueId}/seasons', headers=headers)
    return response.json()
def get_warLeagueInfo(leagueId):
    response = requests.get(f'https://api.clashofclans.com/v1/warleagues/{leagueId}', headers=headers)
    return response.json()

############ Location
def get_rankLoc(locationID):
    response = requests.get(f'https://api.clashofclans.com/v1/locations/{locationId}/rankings/clans', headers=headers)
    return response.json()
def get_playLoc(locationID):
    response = requests.get(f'https://api.clashofclans.com/v1/locations/{locationId}/rankings/players', headers=headers)
    return response.json()
def get_clanVs(locationID):
    response = requests.get(f'https://api.clashofclans.com/v1/locations/{locationId}/rankings/clans-versus', headers=headers)
    return response.json()
def get_PlayerVS(locationID):
    response = requests.get(f'https://api.clashofclans.com/v1/locations/{locationId}/rankings/players-versus')
    return response.json()
def get_InfoLoc(locationID):
    response = requests.get(f'https://api.clashofclans.com/v1/locations/{locationId}', headers=headers)
    return response.json()


############ Clans

def get_clanInfo(clanTag):
    response = requests.get(f'https://api.clashofclans.com/v1/clans/{clanTag}/currentwar/leaguegroup', headers=headers)
    return response.json()
def get_leagueWarInfo(warTag):
    response = requests.get(f'https://api.clashofclans.com/v1/clanwarleagues/wars/{warTag}', headers=headers)
    return response.json()
def get_warLog(clanTag):
    response = requests.get(f'https://api.clashofclans.com/v1/clans/{clanTag}/warlog', headers=headers)
    return response.json()
def get_currentClanWar(clanTag):
    response = requests.get(f'https://api.clashofclans.com/v1/clans/{clanTag}/currentwar', headers=headers)
    return response.json()
def get_clanInfo2(clanTag):
    response = requests.get(f'https://api.clashofclans.com/v1/clans/{clanTag}', headers=headers)
    return response.json()
def get_clanMembers(clanTag):
    response = requests.get(f'https://api.clashofclans.com/v1/clans/{clanTag}/members', headers=headers)
    return response.json()


if __name__ == '__main__':
    print("Choose your mode:")
    a = int(input("[1] Player \n[2] League \n[3] Location \n[4] Clans\n> "))
    if a == 1:
        b = int(input("[1] Player info \n[2] Player Trophies \n> "))
        c = input("Enter player tag: ")
        if b == 1:
            print(get_userName(c))
        elif b == 2:
            print(get_userTrophies(c))
        else:
            exit("Invalid mode")
    elif a == 2:
        b = int(input("[1] League Rankings \n[2] League Info \n[3] League Seasons \n[4] War League Info \n> "))
        c = input("Enter league ID: ")
        
        if b == 1:
            d = input("Enter season ID: ")
            print(get_leagueRank(c, d))
        elif b == 2:
            print(get_leagueInfo(c))
        elif b == 3:
            print(get_leagueSeasons(c))
        elif b == 4:
            print(get_warLeagueInfo(c))
        else:
            exit("Invalid mode")
    elif a == 3:
        b = int(input("[1] Rank Location \n[2] Player Location \n[3] Clans Versus \n[4] Player Versus \n[5] Location Info \n> "))
        c = input("Enter location ID: ")
        
        if b == 1:
            print(get_rankLoc(c))
        elif b == 2:
            print(get_playLoc(c))
        elif b == 3:
            print(get_clanVS(c))
        elif b == 4:
            print(get_PlayerVS(c))
        elif b == 5:
            print(get_infoLoc(c))       
        else:
            exit("Invalid mode")
    elif a == 4:
        b = int(input("[1] Clan Info \n[2] League War Info \n[3] War Log Info \n[4] Current clan war \n[5] Clan Info 2 \n[6] Clan Members \n > "))
        c = input("Enter clan TAG: ")
        
        if b == 1:
            print(get_clanInfo(c))
        elif b == 2:
            print(get_leagueWarInfo(c))
        elif b == 3:
            print(get_warLog(c))
        elif b == 4:
            print(get_currentClanWar(c))
        elif b == 5:
            print(get_clanInfo2(c))  
        elif b == 6:
            print(get_clanMembers(c))
        else:
            exit("Invalid mode")
    else:
        exit("Invalid mode")
