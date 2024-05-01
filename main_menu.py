from customer_interfaceee import customer_interface
from seller_inter_face import seller_interface
def Mainmenu():
    while True:
        print("1.Join as a Seller !")
        print("2.Join as a Customer !")
        print("3.Exit")
        choice=int(input("Choice the option: "))
        if choice ==1:
            seller_interface()
        elif choice==2:
            customer_interface()

        elif choice==3:
            break
        else:
            print("Choice the correct option")
    
