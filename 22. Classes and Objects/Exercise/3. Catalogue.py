class Catalogue:
    products = []
    def __init__(self,name):
        self.name = name
    def add_product(self,name):
        Catalogue.products.append(name)
    def get_by_letter(self,first_letter: str):
        list_of_products = []
        for product in Catalogue.products:
            if product.startswith(first_letter):
                list_of_products.append(product)
        return list_of_products
    def __repr__(self):
        message = f'Items in the {self.name} catalogue:\n'
        for item in Catalogue.products:
            message += item + '\n'
        return message


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

