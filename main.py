import random
name = ""
bag = []
fatigue = 0

def Start():
  global name 
  print ("welcome to the most intense adventure game of your life")
  print ("adventurer, to continue please enter what you want me to call you")
  name = input ("enter your name here ")
  print ("welcome",name,"you are being obducted and you will be taken off planet Earth to a land far away. to make it back alive you must complete chalenges")
  forest()

def forest():
  print ('you are at the forest')
  print ("the path you are on now goes two ways left goes to the beach and right to a cave")
  choice = input ("type 1 to go left and 2 to go right?")
  if choice.upper() == '1':
    beach()
  elif choice.upper() =="2":
    cave()
  else:
    print("invalid selection")
    forest()

def beach():
  print ("you are now at the beach you walk from the path at the beach huts to the water edge")
  choice = input ("do you want to go 1 into the water or go 2 to the beach house?")
  if choice.upper() == '2':
    huts()
  elif choice.upper() =='1':
    sea()
  else:
    print("invalid selection")
    beach()

def sea():
  print ('as you are swimming in the water a shark comes up from the depths of the sea bites you legs and starts to drown you')
  choice = input ("do you want to hit the shark to sea if it will let go beware this may just anger it further? type 1 to hit the shark type 2  to not hit the shark")
  if choice.upper() == '1':
    hitshark()
  elif choice.upper() =="2":
    nohitshark()
  else:
    print("invalid selection")
    sea()

def hitshark():
  randomnumber = random.randint(1,4)
  if randomnumber >= 3:
    print ("the shark dragged you under the water and killed you. Better luck next time.")
    Start()
  else:
    fatigue = 78
    print ("the shark let you go however your fatigue has gone up you need to find something to eat")
    print (fatigue)
    choice = input ("do you want to go into the forest or go to the beach huts")
  if choice.upper() == 'HUTS':
    huts()
  elif choice.upper() =="forest":
    forestedge()
  else:
    print("invalid selection")

def forestedge():
  print ("you are now in at the forest edge there is an apple tree to your left or some berries to your right")
  choice = input ("type left to go to the apple tree and right for the berries")
  if choice.upper() == 'LEFT':
    appletree()
  elif choice.upper() =="RIGHT":
    berrybush()
  else:
    print("invalid selection")

def berrybush():
  choice = input ('do you want to eat some berries of this bush yes or no')
  if choice.upper() == 'YES':
    berries()
    notebook()
  elif choice.upper() =='NO':
    notebook()
  else:
    print ("invalide selection")

def berries():
  randomnumber = random.randint(1,4)
  if randomnumber <= 3:
    print ("unlucky the berry you picked was poisenous you died.")
    Start()
  else:
    print ("")
    choice = input ("")
  if choice.upper() == '':
    ()
  elif choice.upper() =="":
    ()
  else:
    print("invalid selection")

def notebook():
  choice = input ('do you want to open the notebook or save it for later')
  if choice.upper() == 'OPEN IT':
    ()
  elif choice.upper() == 'SAVE IT':
    ()
  else:
    print ("invalide selection")

def appletree():
  choice = input ('you are at the apple tree do you wish to eat an apple yes or no')
  if choice.upper() == 'YES':
    eatapple ()
  elif choice.upper() =="NO":
    ()
  else:
    print("invalid selection")

def eatapple():
  randomnumber = random.randint(1,100)
  if randomnumber >= 99:
    print ('this apple was has made you ill. a poisenous bug was inside and you ate it. better luck next time')
    Start()
  else:
    print ('that apple has given you lots more energy fom that fight with the shark')
    print ('do you want to go back to the beach or continue going through the forest')
    choice = input ('type 1 to continue going into the forest and 2 to go to the beach')
    if choice.upper() == '1':
      ()
    elif choice.upper() == '2':
      ()
    else:
      print ('invalid selection')

def nohitshark():
  randomnumber = random.randint(1,4)
  if randomnumber <= 3:
    print ("the shark dragged you under the water and killed you. Better luck next time.")
    Start()
  else:
     choice = input ("type 1 to go to the beach huts or type 2 to go to the edge of the forest")
  if choice.upper() == '1':
    huts()
  elif choice.upper() =="2":
    forestedge()
  else:
    print("invalid selection")

def huts():
  print ("you are back at the beach huts")
  choice = input ("do you want to go into your beach hut or bak into the forest. type 1 to go into the beach hut and 2 to go into the forest")
  if choice.upper() == '1':
    beachhuts()
  elif choice.upper() =="2":
    forest()
  else:
    print("invalid selection")

def beachhuts():
  choice = input ("inside the beach huts is a trap door and some stairs. type 1 to go up stairs and 2 to go through the trap door")
  if choice.upper() == '2':
    ()
  elif choice.upper() =="1":
    ()
  else:
    print("invalid selection")

def cave():
  print ('you are now at the cave, a bear comes out and eats you.')
  Start()
 