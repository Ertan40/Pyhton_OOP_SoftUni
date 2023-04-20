from pyhton_OOP.inheritance.shop.project.product import Product
# from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break
        # for i, product in enumerate(self.products):
        #     if product.name == product_name:
        #         self.products.pop(i)

    def __repr__(self):
        output = []
        for product in self.products:
            output.append(f"{product.name}: {product.quantity}")
        return '\n'.join(output)

