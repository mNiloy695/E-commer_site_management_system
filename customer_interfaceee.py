from Customer import Customer
from product import Product
from check_validiti import e_s
def customer_interface():
    choice=input("Rigister or login ? l/r : ").lower()
    if choice=='r':
        name=input("Enter your name: ")
        phone=input("Enter your phone number: ")
        email=input("Enter your email Address: ")
        passWord=input("Enter your password : ")
        cs=Customer(name=name,phone=phone,email=email,password=passWord)
        print(f"Welcome {cs.name} !")
        while True:
            print("1.Add product to cart")
            print("2.remove product from cart")
            print("3.Pay bill")
            print("4.Main Menu")
            print("5.View cart")
            print("6.View product")

            choice=int(input("Enter the option: "))
            if choice==1:
                name=input("Enter product name: ")
                quantity=int(input("Enter the quantity: "))
                cs.add_to_cart(name,quantity)
            elif choice==2:
                name=input("Enter product name: ")
                cs.remove_from_cart(name)
            elif choice==3:
                x=cs.Total_Bill()
                print("Your total bill is: ",x)
                money=int(input("Enter the amount"))
                if money>=x:
                    cs.pay_bill(e_s)
                    print("here the money: ",x-money)
                else:
                    print("sorry you need to pay more money")

            elif choice==4:
               break
            elif  choice==5:
                cs.view_cart()
            elif choice==6:
                cs.viwe_products(e_s)
    elif choice=='l':
        email=input("Enter your email Address: ")
        passWord=input("Enter your password : ")
        cs=e_s.customer_valid_of_not(email=email,password=passWord)
        if cs:
          print(f"Welcome {cs.name} !")
 
          while True:
              
              print("1.Add product to cart")
              print("2.remove product from cart")
              print("3.Pay bill")
              print("4.Main Menu")
              choice=int(input("Enter the option: "))
              if choice==1:
                 
                 name=input("Enter product name: ")
                 price=int(input("Enter The price of the product: "))
                 quantity=int(input("Enter the quantity: "))
                 product=Product(name=name,price=price,quantity=quantity)
                 cs.add_to_cart(product)
              elif choice==2:
                 name=input("Enter product name: ")
                 cs.remove_from_cart(name)
              elif choice==3:
                 x=cs.Total_Bill()
                 print("Your total bill is: ",x)
                 money=int(input("Enter the amount"))
                 if money>=x:
                     cs.pay_bill(e_s)
                     print("here the money: ",x-money)
                 else:
                     print("sorry you need to pay more money")

              elif choice==4:
                 
                 break
              elif  choice==5:
                break
              else:
                  print("Please choice correct option")



        

    
