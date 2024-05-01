from person import Person
from  E_Shop import E_com_site
class Seller(Person):
    def __init__(self,name,phone,email,password):
        super().__init__(name=name,phone=phone,email=email,password=password)
        self.products=[]
        self.balance=0
        E_com_site.seller_list.append(self)
    def viwe_products(self,e_shop):
        print("*******************************\n")
        print("Name\tPrice\tQuantity")
        for item in self.products:
            print(f"{item.name} {item.price} {item.quantity}")
        print("\n*******************************\n")
        
    def add_product(self,product):
        f=0
        for i,p in enumerate(self.products):
            if p.name.lower()==product.name.lower():
                self.products[i].quantity+=product.quantity
                f=1
                break
        if f==0:
            self.products.append(product)

    def publish_for_sale(self,e_shop):
        e_shop.add_products_with_saller(self)
    def sell(self,value):
        if value>0:
            self.balance+=value
            print("The item sell successfully and your current balance is: !",self.balance)

   
    def show_balance(self):
        print(self.name,"->",self.balance)
    




