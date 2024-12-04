def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(name,damage=0, defensePower=0):
    global player
    player = dict(name=name,
              score=0,
              damage=damage,
              health=100,
              defensePower=defensePower,
              defense=False)
    return player

def addPlayer(player):
    PlayerList.append(player)

def removePlayer(name):
    for player in PlayerList:
        if player["name"] == name:
            return PlayerList.remove(player)
    return print("There is no player with that name!")

def setPlayer(player,key,value):
    if key in player:
        player[key] = value

def attackPlayer(attacker:dict, target:dict):
    if target["defense"]:
        damageTaken = attacker["damage"] - target["defensePower"]
    else:
        damageTaken = attacker["damage"]

    newHealth = target["health"] - damageTaken
    setPlayer(target,"health", newHealth)

    score_increase = 1
    if target["defense"]:
        score_increase = 0.8
    setPlayer(attacker, "score", attacker["score"] + score_increase)

    setPlayer(target,"defense", False)

def displayMatchResult():
    sorted_players = sorted(PlayerList, key=lambda x: (x["score"], x["health"]), reverse=True)
    rank = 1
    for player in sorted_players:
        print(f"Rank {rank}: {player['name']} | Score: {player['score']} | Health: {player['health']}")
        rank += 1