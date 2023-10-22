TASK-4
import random
print("0.Rock")
print("1.paper")
print("2.Scissors")
values=0,1,2

while True:

  yourchoice=int(input("enter a number:"))
  computerchoice=random.choice(values)
  print("yourchoice:",yourchoice)
  print("computerchoice:",computerchoice)

  if(yourchoice and computerchoice in values):

   if(computerchoice>yourchoice):
    print("you lose!!!")
   elif(yourchoice>computerchoice):
    print("you win!!!")
   elif(yourchoice==computerchoice):
    print("ohh!! it's draw")
   elif(yourchoice==0):
    print("you win!!!")
   elif(computerchoice==0):
    print("you lose!!!")
  elif((yourchoice  not in values)):
   print("entered the invalid number")
