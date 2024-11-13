CREATE TABLE IF NOT EXISTS TREE_SPECIES (
    id INT PRIMARY KEY,
    tree_name VARCHAR(100),
    scientific_name VARCHAR(255),
    description VARCHAR(100)
);

INSERT INTO TREE_SPECIES (id,tree_name,scientific_name,description) VALUES (0,'example', 'something_long', 'good for environment'),(1,'example2', 'something_long_again', 'really good for environment');