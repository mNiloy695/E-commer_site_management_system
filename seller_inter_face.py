from seller import Seller
from product import Product
from check_validiti import e_s
def seller_interface():
    choice=input("Rigister or login ? l/r : ").lower()
    if choice=='r':
        name=input("Enter your name: ")
        phone=input("Enter your phone number: ")
        email=input("Enter your email Address: ")
        passWord=input("Enter your password : ")
        s=Seller(name=name,phone=phone,email=email,password=passWord)
        print(f"Welcome {name} !")
        while True:
            print("1.Add product")
            print("2.viwe products")
            print("3.Publish for sale")
            print("4.Main Menu")
            print("5.show balance")
            choice=int(input("Enter the option: "))
            if choice==1:
                name=input("Enter product name: ")
                price=int(input("Enter The price of the product: "))
                quantity=int(input("Enter the quantity: "))
                product=Product(name=name,price=price,quantity=quantity)
                s.add_product(product)
            elif choice==2:
                s.viwe_products(e_s)
            elif choice==3:
               s.publish_for_sale(e_s)

            elif choice==4:
                break
            elif  choice==5:
                s.show_balance()
    elif choice=='l':
        email=input("Enter your email Address: ")
        passWord=input("Enter your password : ")
        s=e_s.seller_valid_of_not(email=email,password=passWord)
        if s:
          print(f"Welcome {s.name} !")
 
          while True:
              
              print("1.Add product")
              print("2.view")
              print("3.publish for sale")
              print("4.Main Menu")
              print("5.show balance")
              choice=int(input("Enter the option: "))
              if choice==1:
                 
                 name=input("Enter product name: ")
                 price=int(input("Enter The price of the product: "))
                 quantity=int(input("Enter the quantity: "))
                 product=Product(name=name,price=price,quantity=quantity)
                 s.add_product(product)
              elif choice==2:
                  s.viwe_products(e_s)
              elif choice==3:
                s.publish_for_sale(e_s)

              elif choice==4:
                 
                 break
              elif  choice==5:
                s.show_balance()
              else:
                  print("pleased choce correct option")



        

    

