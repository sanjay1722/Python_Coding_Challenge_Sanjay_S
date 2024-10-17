from entity.Product import Product

class Clothing(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, size, color):
        super().__init__(productId, productName, description, price, quantityInStock, 'Clothing')
        self.size = size
        self.color = color

    # Getters and setters for Clothing-specific fields
    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return f"Clothing [ID={self.productId}, Name={self.productName}, Size={self.size}, Color={self.color}, Price={self.price}, Stock={self.quantityInStock}]"

