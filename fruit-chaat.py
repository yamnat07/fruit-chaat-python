fruits=["Apple","Banana","Mango","Orange","Grapes","Pineapple","Watermelon","Papaya","Strawberry","Kiwi"]
masala=["Chaat masala","Black pepper","Black salt","White salt"]
while True:
    print("#################################")
    print("==WELCOME TO FRUIT CHAAT CENTRE==")
    print("#################################")
    print("1.Make a fruit chaat: \n")
    print("2.Exit:\n")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Available fruits:\n ")
        print(fruits)
        ent_fruits=int(input("Enter total number of fruits you want to select: "))
        sel_fruits=""
        for i in range(1,ent_fruits+1):
            while True:
             pick_fruit=input(f"Enter your fruit number {i}: ")
             if pick_fruit in fruits:
              sel_fruits+=pick_fruit+"+"
              print(sel_fruits)
              break
             else:
              print(fruits)
              print("Please enter from Fruits list!!!")
        while True:
         confirm=input("Confirm this? yes/no:")
         if confirm=="yes":
          print("Fruits confirmed!!!!")       
          break
         elif confirm=="no":
            break
         else:
            print("Please enter only yes or no")
        if confirm=="no":
           continue 
        print("Available Masalas: \n")
        print(masala) 
        while True: 
         ent_masala=input("Select your masala to add: ")
         if ent_masala in masala:
          print("Here is your fruit chaat, ENJOY!!!")
          print(f"Fruit chaat= {sel_fruits}{ent_masala}")
          break
         else:
           print(masala)
           print("Enter masala only from masala list!!") 
    elif choice==2:
        print("No worries, give us one chance to serve you!!!!")
        break
    else:
        print("Invalid choice!!!!!")           


