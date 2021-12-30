print("Welcome to the rollecoaster")
height=int(input("What is your height in CM? "))
if height >=120:
  print("You can ride the rollecoaster")
  age=int(input("Which is your age? "))
  if age <12:
    print("Pay $5")
  elif age >=18:
      print("Pay $7")
  else:
    print("Pay $12")
else:
  print("You not ride the rollecoaster")


