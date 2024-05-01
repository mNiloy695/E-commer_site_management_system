from person import Person
from E_Shop import E_com_site
from product import Product
from seller import Seller
class Customer(Person):
    def __init__(self,name,phone,email,password):
        super().__init__(name=name,phone=phone,email=email,password=password)
        self.cart={}
        # self.Bank_account=Account("Niloy","islami Bank","Credit card")
        E_com_site.customer_list.append(self)
    def viwe_products(self,e_shop):
        e_shop.viwe_products()
    def view_cart(self):
       
       print("****************************************\n")
       print("Name\tprice\tQuantity\n")
       for item_list in self.cart.values():

        for item in item_list:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
    print("\n****************************************")


    def find_product(self,item_name):
        product=E_com_site.find_product(item_name)
        return product
    def add_to_cart(self,item_name,quantity):
        s_item=self.find_product(item_name)
        if s_item:
            if s_item[1].quantity>=quantity:
                s=s_item[0]
                p=Product(s_item[1].name,s_item[1].price,quantity)
                if s in self.cart.keys():
                    self.cart[s].append(p)
                else:
                    self.cart[s]=[p]
                
                #s_item[1].quantity=quantity
                print(f"The item {item_name} is added ")

                
                    


    def Total_Bill(self):
        sum=0
        for i in self.cart.values():
            for item in i:
                sum+=item.price*item.quantity
        return sum
    def remove_from_cart(self,item_name):
        for seller,item_list in self.cart.items():
            for item in item_list:
                if item.name==item_name:
                    self.cart[seller].remove(item)
                    return
    def pay_bill(self,e_shop):
        money_sum_total=self.Total_Bill()
        for seller ,items in self.cart.items():
            money=0
            for i in items:
                money+=i.price*i.quantity
                e_shop.update_products(seller,i)
            seller.sell(money)
        self.cart={}
        print(f"{money_sum_total} tk successfully payment done !")


    

        


        



    


        
