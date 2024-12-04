import game as g

g.initPlayers()
player1 = g.createNewPlayer("budiono siregar", 14, 11)
player2 = g.createNewPlayer("anton butar butar", 12, 15)
player3 = g.createNewPlayer("gunawan chandra", 20, 10)
player4 = g.createNewPlayer("roy myers", 13, 12)
player5 = g.createNewPlayer("nobara kugisaki", 15, 8)

g.addPlayer(player1)
g.addPlayer(player2)
g.addPlayer(player3)
g.addPlayer(player4)
g.addPlayer(player5)

g.removePlayer("anton butar butar")

g.setPlayer("budiono siregar", "defensePower", 20)

g.attackPlayer(player1, player5)
g.attackPlayer(player3, player1)
g.attackPlayer(player5, player4)
g.attackPlayer(player4, player3)

g.displayMatchResult()