import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity.Product import Product
from entity.Electronics import Electronics
from entity.Clothing import Clothing
from entity.User import User

from dao.OrderProcessor import OrderProcessor
from exception.UserNotFoundException import UserNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException

def main():
    processor = OrderProcessor()

    while True:
        print("\n===Home page===")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Orders By User")
        print("7. Exit")
        print("---------------")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Create User
            while True:
                username = input("Enter username: ")

                if processor.getUserByUsername(username):
                    print("Username already exists. Please try with another username.")
                else:
                    break  

            password = input("Enter password: ")
            role = input("Enter role (Admin/User): ")  
            user = User(0, username, password, role)
            processor.createUser(user)
            print("User created successfully.")
        
        elif choice == '2':
            # Create Product
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            # Check if the user is admin and password matches
            user = processor.getUserByUsername(username)
            
            if user and user.password == password and user.role == "Admin":
                print("Access granted to create products.")
                
                while True:
                    product_name = input("Enter product name: ")
                    description = input("Enter description: ")
                    price = float(input("Enter price: "))
                    quantity = int(input("Enter quantity in stock: "))
                    product_type = input("Enter product type (Electronics/Clothing): ")

                    # Handle product creation based on type
                    if product_type == "Electronics":
                        brand = input("Enter brand: ")
                        warranty_period = int(input("Enter warranty period: "))
                        product = Electronics(0, product_name, description, price, quantity, brand, warranty_period)
                    
                    elif product_type == "Clothing":
                        size = input("Enter size: ")
                        color = input("Enter color: ")
                        product = Clothing(0, product_name, description, price, quantity, size, color)
                    
                    else:
                        print("Invalid product type. Please enter Electronics or Clothing.")
                        continue  
                    
                    processor.createProduct(user, product)
                    print("Product created successfully.")
                    
                    another = input("Do you want to add another product? (yes/no): ").lower()
                    if another != 'yes':
                        print("Exiting product creation.")
                        break  
            else:
                print("Access Denied. Only Admins can create products.")
  
        elif choice == '3':
          # Create Order
          userId = int(input("Enter your User ID: "))
          product_ids = input("Enter product IDs to order (comma-separated): ").split(',')
          
          products = []
          for pid in product_ids:
              product = processor.getProductById(int(pid.strip()))
              if product:
                  products.append(product)
              else:
                  print(f"Product with ID {pid} not found.")
          
          if products:
              try:
                  processor.createOrder(userId, products)
                  print("Order created successfully.")
              except UserNotFoundException as e:
                  print(f"Error: {e}")
  
        elif choice == '4':
            # Cancel Order
            userId = int(input("Enter your User ID: "))
            orderId = int(input("Enter Order ID to cancel: "))
            
            try:
                processor.cancelOrder(userId, orderId)
                print("Order canceled successfully.")
            except (UserNotFoundException, OrderNotFoundException) as e:
                print(f"Error: {e}")
        
        elif choice == '5':
            # Get All Products
            print("Fetching all products...")
            products = processor.getAllProducts()
            for product in products:
                print(f"Product ID: {product.productId}, Name: {product.productName}, Price: {product.price}, Stock: {product.quantityInStock}, Type: {product.type}")
        
        elif choice == '6':
          # Get Orders By User
          userId = int(input("Enter your User ID: ")) 
          orders = processor.getOrderByUser(userId)
          
          if orders:
              print(f"Orders for User ID {userId}:")
              for order in orders:
                  order_id, product_id = order  
                  print(f"Order ID: {order_id}, Product ID: {product_id}")
          else:
              print(f"No orders found for User ID {userId}.")
        
        elif choice == '7':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
