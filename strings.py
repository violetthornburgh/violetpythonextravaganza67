

def fnc():
  strong = input("string")
  ciph = int(input("number"))
  al = "abcdefghijklmnopqrstuvwxyz"
  result = ""
  for i in range(len(strong)):
    ind = al.find(strong[i])
    result = result + al[ind-ciph]
  print(result)

#fnc()
#-------------------------------------------------------------------------------
#string1 = input("string 1")
#string2 = input("string 2")

def ana(string1, string2):
  al = "0abcdefghijklmnopqrstuvwxyz"
  nu1 = 0
  nu2 = 0
  for i in range (len(string1)):
    stf = al.find(string1[i])
    nu1 = nu1 + stf
  
  for i in range (len(string2)):
    stu = al.find(string2[i])
    nu2 = nu2 + stu
  
  if nu1 == nu2:
    print("those are probably anagrams")
  else:
    print("yeah those are definitely not anagrams")
    
#ana(string1, string2)
  
