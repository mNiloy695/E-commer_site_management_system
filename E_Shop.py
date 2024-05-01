class E_com_site:
    seller_list=[]
    customer_list=[]
    
    products={}
    def __init__(self,name):
        self.name=name
        
    @classmethod
    def find_seller(cls,seller_name):
        for seller in cls.seller_list:
            if seller.name.lower()==seller_name.lower():
                return seller
        return None
    @classmethod
    def find_product(self,item_name):
        for key,item_lsit in self.products.items():
           for item in item_lsit:
               if item.name.lower()==item_name:
                   return [key,item]
        return None
    def update_products(self,seller,items):
        if seller in self.products.keys():
            for itm in self.products[seller]:
                if itm.name.lower()==items.name.lower():
                    itm.quantity-=items.quantity
                    break        
        return None
    # def add_product(self,itm):
    #     item=self.find_product(itm.name)
    #     if item:
    #         item.quantity+=itm.quantity
    #         self.items[item]+=itm.quantity
    #     else:
    #         self.items[itm]=itm.quantity
    def viwe_products(self):
        print("Name\tPrice\tQuantity")
        print("\n***************************************\n")
        
        for item  in self.products.values():
            for i in item:
                print(f"{i.name}\t{i.price}\t{i.quantity}")

        print("\n***************************************\n")
    @classmethod
    def remove_product(self,item,quantity):
        item.quantity-=quantity
        self.items[item]-=quantity
        if self.items[item]==0:
            del self.items[item]
    @classmethod
    def add_products_with_saller(self,seller):
        self.products[seller]=seller.products


        
    def seller_valid_of_not(self,email,password):
        for seller in self.seller_list:
            if seller.email==email and seller.password==password:
                print("you successfully loged in !")
                return seller
        print("Sorry you are not valid")
        return None
    def customer_valid_of_not(self,email,password):
        for customer in self.customer_list:
            if customer.email==email and customer.password==password:
                print("you successfully loged in !")
                return customer
        print("Sorry you are not valid")
        return None
        
