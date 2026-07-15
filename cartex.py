# balance=1000
# def display_menu():
#     print("simpale bank system")
#     print("1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit")

# while True:
#     display_menu()
#     choice=int(input("Enter your choice {1,2,3,4}"))

#     if choice==1:
#         print(f"your bank balance is {balance}")
#     elif choice==2:
#         amount=int(input("Enter your Deposit money "))
#         if amount>0:
#             balance+=amount
#             print(f"{amount} is Deposit success fully ")
#             print(f"total amount is {balance}")
#         else:
#             print("transation fail")    

#     elif choice==3:
#         amount=int(input("Enter your Deposit money "))
#         if amount<=0:
#             print("invalid amount")

#         elif amount>balance:
#             print(f"in suffisiant balance ")
#         else:
#             print(f"{amount} is Deposit success fully ")
#             print(f"total amount is {balance}")

#     else:
#         print("Thank you for visiting banking suystem")
#         break
cart={}
total=0

while True:
    print("\n===== GROCERY STORE =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart & Total Price")
    print("4. Exit")


    choice=int(input("enter your choice"))
    
    if choice==1:
        item=input("enter the name :")
        price=int(input("enter price "))
        cart[item]=price
        total+=price
        print(f"{item} added success fully ")
    elif choice==2:
        item=input("enter remove name ")
        if item in cart:
            total-=cart[item]
            del cart[item]
            print(f"{item} Delete the item")
        else:
            print("item is not found ")
    elif choice==3:
        print("------shoping cart --------")
        if len(cart)==0:
            print("your cart is empty ")
        else:
            for item,price in cart.items():
                print(f"{item},${price}")
                print(f"{total}")
    elif choice==4:
        print("thank tou for waching")
        break
    else:
        print("invalid choice")