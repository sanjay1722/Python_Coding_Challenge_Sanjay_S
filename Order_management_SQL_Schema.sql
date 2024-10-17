CREATE DATABASE OrderManagementDB;

USE OrderManagementDB;

CREATE TABLE Users (
    userId INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(100) NOT NULL,
    password NVARCHAR(100) NOT NULL,
    role NVARCHAR(50) NOT NULL
);

ALTER TABLE Users
ADD CONSTRAINT UQ_Username UNIQUE (username);


CREATE TABLE Products (
    productId INT PRIMARY KEY IDENTITY(1,1),
    productName NVARCHAR(100) NOT NULL,
    description NVARCHAR(255),
    price FLOAT NOT NULL,
    quantityInStock INT NOT NULL,
    type NVARCHAR(50) NOT NULL,
    brand NVARCHAR(100) NULL,
    warrantyPeriod INT NULL,
    size NVARCHAR(10) NULL,
    color NVARCHAR(50) NULL
);


CREATE TABLE Orders (
    orderId INT PRIMARY KEY IDENTITY(1,1),
    userId INT,
    productId INT,
    FOREIGN KEY (userId) REFERENCES Users(userId),
    FOREIGN KEY (productId) REFERENCES Products(productId)
);

select * from users;
select * from products;
select * from orders;



