-- Create the 'products' table with columns: pid, prodname, original_price, and selling_date
CREATE TABLE products (
    pid INT PRIMARY KEY,                -- Product ID (primary key)
    prodname VARCHAR(50) NOT NULL,      -- Product name (cannot be NULL)
    original_price DECIMAL(10, 2) NOT NULL, -- Original price of the product (cannot be NULL)
    selling_date DATE NOT NULL          -- Selling date of the product (cannot be NULL)
);

-- Insert product records into the 'products' table
INSERT INTO products (pid, prodname, original_price, selling_date) 
VALUES 
    (1, 'Smartphone', 6059.90, '2024-10-01'),
    (2, 'Laptop', 14437.34, '2024-10-15'),
    (3, 'Headphones', 2019.90, '2024-11-05'),
    (4, 'Smartwatch', 3029.90, '2024-11-10'),
    (5, 'Wireless Mouse', 29.99, '2024-11-20'),
    (6, 'Bluetooth Speaker', 89.99, '2024-11-25'),
    (7, 'Tablet', 4039.90, '2024-12-01');
