-- Define the table for storing food items

CREATE TABLE IF NOT EXISTS Pantry (
    FoodName TEXT NOT NULL,
    Quantity INT NOT NULL,
    Description TEXT NOT NULL,
    PickupAddress TEXT NOT NULL,         
    ContactNumber TEXT NOT NULL
);