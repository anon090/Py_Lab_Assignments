-- Create a table called 'countries' with 3 columns: country_id, country_name, and region_id
CREATE TABLE countries (
    country_id INT NOT NULL PRIMARY KEY,  -- country_id is the primary key and cannot be NULL
    country_name VARCHAR(50) NOT NULL,    -- country_name is a VARCHAR type with a maximum length of 50 characters, cannot be NULL
    region_id INT NOT NULL                -- region_id is an INT type and cannot be NULL
) $$;

-- Add a check constraint on country_name to ensure it only contains 'india', 'italy', or 'china'
ALTER TABLE countries 
ADD CONSTRAINT check_country_name 
CHECK (country_name IN ('india', 'italy', 'china')) $$;

-- Insert valid records into the 'countries' table
INSERT INTO countries (country_id, country_name, region_id) 
VALUES 
    (1, 'india', 1), 
    (3, 'italy', 3), 
    (5, 'china', 5), 
    (7, 'India', 7), 
    (9, 'China', 9), 
    (11, 'Italy', 11) $$;

-- This INSERT statement fails because 'france' is not in the allowed values for country_name
INSERT INTO countries (country_id, country_name, region_id) 
VALUES (1, 'france', 1);  -- ERROR: violates the check constraint.

-- This INSERT statement fails because 'India' (with a different case) is already in the table (duplicate country_id).
INSERT INTO countries (country_id, country_name, region_id) 
VALUES (1, 'india', 1);  -- ERROR: Duplicate entry for primary key 'country_id'

-- This INSERT statement fails because 'germany' is not in the allowed values for country_name
INSERT INTO countries (country_id, country_name, region_id) 
VALUES (1, 'germany', 3);  -- ERROR: violates the check constraint.

-- Display the structure of the 'countries' table
DESC countries $$;
