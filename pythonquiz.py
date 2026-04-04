name = input("what's your name")

a = "hello "+ name
print(a)


def questionone():
  score = 0
  q1 = int(input("what is 2 + 2"))

  if (q1 == 4):
    print("ok")
    print("")
    
  else:
    print("no")
    print("")
    questionone()
  
questionone()

def questiontwo():

  q2 = input("what key signature has a b flat")
  
  if (q2.lower() == "f major"):
    print("ok")
    print("")
   
  elif (q2.lower() == "fm"):
    print("ok")
    print("")
   
  else:
    print("no")
    print("")
    questiontwo()

questiontwo()

def questionthree():

  q3 = input("what's your favorite MCR song")
  
  if (q3.lower() == "helena"):
    print("ok")
    print("")
   
  elif (q3.lower() == "famous last words"):
    print("ok")
    print("")
   
  elif (q3.lower() == "welcome to the black parade"):
    print("ok")
    print("")
  
  elif (q3.lower() == "i'm not okay (i promise)"):
    print("ok")
    print("")
    
  else:
    print("wrong")
    print("")
    questionthree()
  
questionthree()  

def questionfour():
  
  q4 = input("six")
  
  if (q4 == "seven"):
    print("ok")
    print("")
    
  else:
    print("no")
    print("")
    questionfour()
    
questionfour()

def questionfive():
  
  print("i'm frightened")
  print("")
  print("as well you should be! freedom is scary. it's a blast of cool wind that burns your face to wake you up.")
  print("")
  q5 = input("literally?")
  
  if (q5.lower() == "yes"):
    print("there's a trickle of sweat")
    print("")
  else:
    print("no")
    questionfive()
    
questionfive()

def questionsix():
  
  q6 = int(input("12-3"))
  
  if (q6 == 9):
    print("ok")
    print("")
    
  else:
    print("no")
    print("")
    questionsix()
    
questionsix()


ending = "that's my quiz. you can go home now, " + name + "."
print(ending)
