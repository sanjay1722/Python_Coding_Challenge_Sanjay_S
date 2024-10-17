class Product:
    def __init__(self, productId, productName, description, price, quantityInStock, type):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

    # Getters and setters for Product class
    def get_product_id(self):
        return self.productId

    def set_product_id(self, productId):
        self.productId = productId

    def get_product_name(self):
        return self.productName

    def set_product_name(self, productName):
        self.productName = productName

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_quantity_in_stock(self):
        return self.quantityInStock

    def set_quantity_in_stock(self, quantityInStock):
        self.quantityInStock = quantityInStock

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def __str__(self):
        return f"Product [ID={self.productId}, Name={self.productName}, Description={self.description}, Price={self.price}, Stock={self.quantityInStock}, Type={self.type}]"
