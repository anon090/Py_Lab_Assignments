-- Create the 'employee' table with columns: first_name, last_name, age, role, salary, and city
CREATE TABLE employee (
    first_name VARCHAR(20) NOT NULL,   -- First name of the employee (cannot be NULL)
    last_name VARCHAR(20) NOT NULL,    -- Last name of the employee (cannot be NULL)
    age INT NOT NULL,                  -- Age of the employee (cannot be NULL)
    role VARCHAR(20) NOT NULL,         -- Role/position of the employee (cannot be NULL)
    salary INT NOT NULL,               -- Salary of the employee (cannot be NULL)
    city VARCHAR(20) NOT NULL          -- City where the employee works (cannot be NULL)
);

-- Display the structure (schema) of the 'employee' table
DESC employee;

-- Insert multiple records into the 'employee' table
INSERT INTO employee (first_name, last_name, age, role, salary, city) 
VALUES 
    ('John', 'Doe', 30, 'Manager', 50000, 'New York'), 
    ('Jane', 'Smith', 28, 'Developer', 45000, 'Los Angeles'), 
    ('Emily', 'Jones', 35, 'Designer', 40000, 'Chicago'), 
    ('Michael', 'Brown', 40, 'Team Lead', 60000, 'San Francisco'), 
    ('Jessica', 'Williams', 25, 'Intern', 30000, 'Miami'), 
    ('Daniel', 'Taylor', 32, 'Analyst', 55000, 'Boston'), 
    ('Sophia', 'Davis', 27, 'HR', 38000, 'Seattle');

-- Select all records from the 'employee' table
SELECT * FROM employee;
