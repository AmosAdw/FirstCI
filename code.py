print("Hello world")
name = input("Entrez votre nom : ")
print("Bonjour,", name)
print("Let's play a game")
choice= input("Enter y to accept and n to decline")
choice=str(choice)
if choice=="y":
    print("yes! Let's play")
elif choice=="n":
    print("Sh**t!")
else:
    print("Enter y or n")
