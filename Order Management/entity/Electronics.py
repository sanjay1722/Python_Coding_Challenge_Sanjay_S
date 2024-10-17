from entity.Product import Product

class Electronics(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, brand, warrantyPeriod):
        super().__init__(productId, productName, description, price, quantityInStock, 'Electronics')
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod

    # Getters and setters for Electronics-specific fields
    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_warranty_period(self):
        return self.warrantyPeriod

    def set_warranty_period(self, warrantyPeriod):
        self.warrantyPeriod = warrantyPeriod

    def __str__(self):
        return f"Electronics [ID={self.productId}, Name={self.productName}, Brand={self.brand}, Warranty={self.warrantyPeriod} years, Price={self.price}, Stock={self.quantityInStock}]"
