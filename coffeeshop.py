#Lister 
CoffeeList = ["Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat White"]

CoffeeSize = ["Small", "Medium", "Large"]

Answer= ["yes", "no"]



print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+            Welcome To         +")
print("+          The coffee store     +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

    
#denne funkjsonen returnerer verdien sin dersom du skriver inn feil 
def invalidCof(coffee):
    if coffee not in CoffeeList:
     print("Please choose something from the Menu, we dont have that here")
     return True
    else:
     return False
    
    #forsetter programmet dersom du skriver inn riktig
while True:
   coffee = input("What type of coffee would you like? ").title()
   if invalidCof(coffee):
      continue
   else:
      break
   
   #verdi for de forskjellige prisene kaffe
price = 0
if coffee==(CoffeeList[0]):
    price = price + 2.5
elif coffee== (CoffeeList[1]):
    price = price + 3
elif coffee==(CoffeeList[2]):
    price = price + 2.5
elif coffee==(CoffeeList[3]):
    price = price + 3
elif coffee== (CoffeeList[4]):
    price = price + 2.5
elif coffee== (CoffeeList[5]):
    price = price + 4
elif coffee== (CoffeeList[6]):
    price = price + 3 
   
#samme funkjson 
def invalidSize(Size):
    if Size not in CoffeeSize:
     print("We dont have that size here")
     return True
    else:
     return False
    
while True:
   if invalidSize():
      continue
   else:
      break

Size = input("What size woukd you like? ").title()
if Size == (CoffeeSize[0]):
    print("----------------------------")
elif Size == (CoffeeSize[1]):
    print("----------------------------")
elif Size == (CoffeeSize[2]):
    print("----------------------------")


#printer takeaway og alt du valgte
Takeaway = input("do u want take away? ")
if Takeaway == (Answer[0]):
   print("----------------------------")
   print(CoffeeList)
   print("")
   print(CoffeeSize)
   print("")
   print("Take away?:")
   print(Answer[0])
   print("----------------------------")
if Takeaway == (Answer[1]):
   print("----------------------------")
   print(CoffeeList)
   print("")
   print(CoffeeSize)
   print("")
   print("Take away?:")
   print(Answer[1])
   print("----------------------------")
   
print("Total Cost: £" + str(price))