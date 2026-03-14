number = int(input("How many kills do you have in Roblox Rivals: Round 1?"))

for i in range(1,6):
  
  print("round {} comments".format(i))
  
  if number > 100:
    print("Your HIM!")
  elif number > 75:
    print("Your Good")
  elif number > 50:
    print("Your mid")
  else:
    print("Your Trash")
    
  if i in range(1,5):
    number1 = int(input("How many kills do you have in Roblox Rivals: Round {}?".format(i+1)))
    number = number + number1
    
