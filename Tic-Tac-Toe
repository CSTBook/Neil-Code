import sys
game=[[2,2,2],[2,2,2],[2,2,2]]

def printboard(tgame):
  board = '\n'
  for row in tgame:
    if row[0] == 2:
      board+='|?|'
    elif row[0] == 0:
      board+='|X|'
    elif row[0] == 1:
      board+='|O|'
    if row[1] == 2:
      board+='?|'
    elif row[1] == 0:
      board+='X|'
    elif row[1] == 1:
      board+='O|'
    if row[2] == 2:
      board+='?|'
    elif row[2] == 0:
      board+='X|'
    elif row[2] == 1:
      board+='O|'
    board+='\n'
  print board
  print "\n\n"
conti = True
def win(contin):
  welp = 0
  if game[0][0] == 0 and game[0][1] == 0 and game[0][2] == 0:
    print "The Computer Wins!"
    sys.exit(0)
  elif game[1][0] == 0 and game[1][1] == 0 and game[1][2] == 0:
    print "The Computer Wins!"
    sys.exit(0)
  elif game[2][0] == 0 and game[2][1] == 0 and game[2][2] == 0:
    print "The Computer Wins!"
    sys.exit(0)
  elif game[0][0] == 0 and game[1][0] == 0 and game[2][0] == 0:
    print "The Computer Wins!"
    sys.exit(0)
  elif game[0][1] == 0 and game[1][1] == 0 and game[2][1] == 0:
    print "The Computer Wins!"
    sys.exit(0)
  elif game[0][2] == 0 and game[1][2] == 0 and game[2][2] == 0:
    print "The Computer Wins!"
    sys.exit(0)
  elif game[0][0] == 0 and game[1][1] == 0 and game[2][2] == 0:
    print "The Computer Wins!"
    sys.exit(0)
  elif game[2][0] == 0 and game[1][1] == 0 and game[0][2] == 0:
    print "The Computer Wins!"
    sys.exit(0)
  if game[0][0] == 1 and game[0][1] == 1 and game[0][2] == 1:
    print "You Win!"
    sys.exit(0)
  elif game[1][0] == 1 and game[1][1] == 1 and game[1][2] == 1:
    print "You Win!"
    sys.exit(0)
  elif game[2][0] == 1 and game[2][1] == 1 and game[2][2] == 1:
    print "You Win!"
    sys.exit(0)
  elif game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 1:
    print "You Win!"
    sys.exit(0)
  elif game[0][1] == 1 and game[1][1] == 1 and game[2][1] == 1:
    print "You Win!"
    sys.exit(0)
  elif game[0][2] == 1 and game[1][2] == 1 and game[2][2] == 1:
    print "You Win!"
    sys.exit(0)
  elif game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1:
    print "You Win!"
    sys.exit(0)
  elif game[2][0] == 1 and game[1][1] == 1 and game[0][2] == 1:
    print "You Win!"
    sys.exit(0)
  else:
    for row in game:
      for value in row:
        if value != 2:
          welp += 1
    if welp == 9:
      sys.exit()

def playerturn(game):
  row = raw_input("\nWhat row do you wish to place an 'O' in (1, 2, or 3)?")
  while row not in ['1', '2', '3']:
    row = raw_input("\nWhat row do you wish to place an 'O' in (1, 2, or 3)?")
  if row == '1':
    position = raw_input("\nWhat position in row 1 do you wish to place an 'O' in (1, 2, or 3)?")
    while position not in ['1', '2', '3']:
      position = raw_input("\nWhat position in row 1 do you wish to place an 'O' in (1, 2, or 3)?")
    if position == '1':
      game[0][0] = 1
    elif position == '2':
      game[0][1] = 1
    if position == '3':
      game[0][2] = 1
  elif row == '2':
    position = raw_input("\nWhat position in row 2 do you wish to place an 'O' in (1, 2, or 3)?")
    while position not in ['1', '2', '3']:
      position = raw_input("\nWhat position in row 2 do you wish to place an 'O' in (1, 2, or 3)?")
    if position == '1':
      game[1][0] = 1
    elif position == '2':
      game[1][1] = 1
    if position == '3':
      game[1][2] = 1
  else:
    position = raw_input("\nWhat position in row 3 do you wish to place an 'O' in (1, 2, or 3)?")
    while position not in ['1', '2', '3']:
      position = raw_input("\nWhat position in row 3 do you wish to place an 'O' in (1, 2, or 3)?")
    if position == '1':
      game[2][0] = 1
    elif position == '2':
      game[2][1] = 1
    if position == '3':
      game[2][2] = 1
def computerturn(game):
  check = []
  checke = 0
  #vertical 1
  for row in game:
    check.append(row[0])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[check.index(value)][0] = 0
        return
  check = []
  checke = 0
  #vertical 2
  for row in game:
    check.append(row[1])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[check.index(value)][1] = 0
        return
  check = []
  checke = 0
  #vertical 3
  for row in game:
    check.append(row[2])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[check.index(value)][2] = 0
        return
  check = []
  checke = 0
  #horizontal 1
  for value in game[0]:
    check.append(value)
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[0][check.index(value)] = 0
        return
  check = []
  checke = 0
  #horizontal 2
  for value in game[1]:
    check.append(row[1])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[1][check.index(value)] = 0
        return
  check = []
  checke = 0
  #horizontal 3
  for value in game[2]:
    check.append(row[2])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[2][check.index(value)] = 0
        return
  check = []
  checke = 0
  #diagonal 1
  check.append(game[0][0])
  check.append(game[1][1])
  check.append(game[2][2])
  for value in check:
    if value == 1:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[check.index(value)][check.index(value)] = 0
        return
  check = []
  checke = 0
  welp = 0
  #diagonal 2
  check.append(game[2][0])
  check.append(game[1][1])
  check.append(game[0][2])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        if welp == 0:
          game[2][0] = 0
        if welp == 1:
          game[1][1] = 0
        else:
          game[0][2] = 0 
        return 
      welp += 1
  #computer attack
  check = []
  checke = 0
  #vertical 1
  for row in game:
    check.append(row[0])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[check.index(value)][0] = 0
        return
  check = []
  checke = 0
  #vertical 2
  for row in game:
    check.append(row[1])
  for value in check:
    if value == 1:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[check.index(value)][1] = 0
        return
  check = []
  checke = 0
  #vertical 3
  for row in game:
    check.append(row[2])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[check.index(value)][2] = 0
        return
  check = []
  checke = 0
  #horizontal 1
  for value in game[0]:
    check.append(value)
  for value in check:
    if value == 1:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[0][check.index(value)] = 0
        return
  check = []
  checke = 0
  #horizontal 2
  for value in game[1]:
    check.append(row[1])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[1][check.index(value)] = 0
        return
  check = []
  checke = 0
  #horizontal 3
  for value in game[2]:
    check.append(row[2])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[2][check.index(value)] = 0
        return
  check = []
  checke = 0
  #diagonal 1
  check.append(game[0][0])
  check.append(game[1][1])
  check.append(game[2][2])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 1:
        game[check.index(value)][check.index(value)] = 0
        return
  check = []
  checke = 0
  welp = 0
  #diagonal 2
  check.append(game[2][0])
  check.append(game[1][1])
  check.append(game[0][2])
  for value in check:
    if value == 0:
      checke += 1
  if checke == 2:
    for value in check:
      if value != 0:
        if welp == 0:
          game[2][0] = 0
        if welp == 1:
          game[1][1] = 0
        else:
          game[0][2] = 0 
        return 
      welp += 1
  for row in game:
    for value in row:
      if value == 2:
        game[game.index(row)][value] = 0
        return
printboard(game)
while True:
  playerturn(game)
  computerturn(game)
  printboard(game)
  win(conti)
