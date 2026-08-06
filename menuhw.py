def menu():
    print("---welcome to banking simulation----:")
    print("1.check balance\n2.deposit balance\n3.withdrabalance \n4.Quit")


balance=0

while True:
    menu()
    choice=int(input("enter your choice "))
    if choice==1:
        print("Balence",balance)
    elif choice==2:
        amount=int(input("enter your's amount !!"))
        balance+=amount
        print("your balane ",balance)
    elif choice==3:
        amount=int(input("enter your withdra amount "))
        balance-=amount
        print("the balance is",balance)
    elif choice==4:
        print("thank you for wisiting ")
        break


cart=[]
while True:
    print("welcome to store ")
    print("1.add a items for cart \n 2.remove item \n 3.view the total prize \n 4.exit ")

    choice=int(input("enter your choice "))

    if choice==1:
        itm=input("enter your item ")
        prize=float(input("enter item amount"))
        cart.append((itm,prize))
        print(f"add the item {cart}")
    elif choice==2:
        itm=input("enter remove itm name")

        for prodoct in cart:
            print(prodoct)
            if prodoct[0].lower()==itm.lower():
                cart.remove(prodoct)
                print(f"remove the prodoct is {itm}")
            else:
                print("not found ")
    elif choice==3:
        total=sum(prize for itm,prize in cart)
        print(f"Total Prise is {total}")
        print(cart)
    elif choice==4:
        print("thank you for wisiting ")
        break
    else:
        print("invalid option try again")


students=[]

while True:
    print("-----student details------")
    print("1.add student detail \n 2.display student details \n 3.exit")

    choice=int(input("enter your choice "))
    if choice==1:
        name=input("enter student name")
        age=int(input(f"eneter{name} age "))
        usn=input(f"enter {name} usn ")
        students.append((name,age,usn))

    elif choice==2:
        print("displaying student details ")
        for stu in students:
            print(stu)
    elif choice==3:
        print("thank you for wisting")
        break
    else:
        print("tray again ather choice ")