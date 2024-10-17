import pyodbc
from dao.IOrderManagementRepository import IOrderManagementRepository
from exception.UserNotFoundException import UserNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException
from util.DBConnUtil import DBConnUtil
from entity.User import User
from entity.Product import Product
from entity.Electronics import Electronics
from entity.Clothing import Clothing

class OrderProcessor(IOrderManagementRepository):

    def __init__(self):
        self.connection = DBConnUtil.get_db_connection()


    def createUser(self, user): #1
        # Code to insert the user into the database
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Users (username, password, role) VALUES (?, ?, ?)", 
                        user.username, user.password, user.role)
        self.connection.commit()  


    def createProduct(self, user, product): #2
        cursor = self.connection.cursor()  
        # If the product is of type Electronics, insert brand and warrantyPeriod
        if product.type == "Electronics":
            cursor.execute("""
                INSERT INTO Products (productName, description, price, quantityInStock, type, brand, warrantyPeriod, size, color)
                VALUES (?, ?, ?, ?, ?, ?, ?, NULL, NULL)
            """, product.productName, product.description, product.price, product.quantityInStock, product.type, product.brand, product.warrantyPeriod)  
        # If the product is of type Clothing, insert size and color
        elif product.type == "Clothing":
            cursor.execute("""
                INSERT INTO Products (productName, description, price, quantityInStock, type, brand, warrantyPeriod, size, color)
                VALUES (?, ?, ?, ?, ?, NULL, NULL, ?, ?)
            """, product.productName, product.description, product.price, product.quantityInStock, product.type, product.size, product.color)
        self.connection.commit()


    def createOrder(self, userId, products): #3
        cursor = self.connection.cursor()
        # Check if the user exists
        cursor.execute("SELECT * FROM Users WHERE userId = ?", userId)
        user = cursor.fetchone()
        if not user:
            raise UserNotFoundException(f"User with ID {userId} not found.")
        # Create an order for each product
        for product in products:
            cursor.execute("INSERT INTO Orders (userId, productId) VALUES (?, ?)", userId, product.get_product_id())
        self.connection.commit()


    def cancelOrder(self, userId, orderId): #4
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Orders WHERE orderId = ? AND userId = ?", orderId, userId)
        if cursor.rowcount == 0:
            raise OrderNotFoundException("Order not found.")
        self.connection.commit()


    def getAllProducts(self): #5
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Products")
        return cursor.fetchall()
    

    def getOrderByUser(self, userId): #6
      cursor = self.connection.cursor()
      cursor.execute("SELECT orderId, productId FROM Orders WHERE userId = ?", userId)
      orders = cursor.fetchall()  
      if orders:
          return orders
      else:
          return []  
      

    def getUserByUsername(self, username):
      cursor = self.connection.cursor()
      cursor.execute("SELECT * FROM Users WHERE username = ?", username)
      row = cursor.fetchone()
      if row:
          return User(row[0], row[1], row[2], row[3])  
      else:
          return None
      

    def getProductById(self, productId):
      cursor = self.connection.cursor()
      cursor.execute("SELECT * FROM Products WHERE productId = ?", productId)
      row = cursor.fetchone()     
      if row:
          if row[5] == "Electronics":
              return Electronics(row[0], row[1], row[2], row[3], row[4], row[6], row[7])  
          elif row[5] == "Clothing":
              return Clothing(row[0], row[1], row[2], row[3], row[4], row[8], row[9])  
          else:
              return Product(row[0], row[1], row[2], row[3], row[4], row[5])  
      else:
          return None  


    


    
