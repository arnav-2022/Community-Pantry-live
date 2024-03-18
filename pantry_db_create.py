import sqlite3

conn = sqlite3.connect("community_pantry")
print("Opened Successfully")

conn.execute('''CREATE TABLE Pantry (
    FoodName TEXT NOT NULL,
    Quantity INT NOT NULL,
    Description TEXT NOT NULL,
    PickupAddress TEXT NOT NULL,         
    ContactNumber TEXT NOT NULL
);''')

print("Table created successfully")

conn.execute("INSERT INTO Pantry (FoodName, Quantity, Description,   PickupAddress, ContactNumber) \
      VALUES ('Burger', 2, 'Bacon, Steak, Cheddar, Lettuce, Tomatoes, Onions, Mustard, Ketchup',  '392 Vexford Street','12220939290')")

conn.execute("INSERT INTO Pantry (FoodName, Quantity, Description,  PickupAddress, ContactNumber) \
      VALUES ('Alfredo pasta', 1 , 'Parmesean Cheese, Fettucine Pasta, Garlic', '213, Bronzor Avenue',29283742455)")

conn.execute("INSERT INTO Pantry (FoodName, Quantity, Description, PickupAddress, ContactNumber) \
      VALUES ('Macaroni and cheese', 4,'Cheddar, Mozzarella, Gouda, Monterey Jack',  '100 Charleston Street','55483910222')")

conn.execute("INSERT INTO Pantry (FoodName, Quantity, Description,  PickupAddress, ContactNumber) \
      VALUES ('Vegetable Soup', 2 ,'Green Beans, Onions, Ginger, Spinach, Mushrooms',  '540 Burndell Street','9102389239')")

conn.execute("INSERT INTO Pantry (FoodName, Quantity, Description,  PickupAddress, ContactNumber) \
      VALUES ('Fried Rice', 3 ,'Corn, Onions, Green Onions, Garlic, Soy Sauce, Oyster Sauce',  '2291, Peyter Street' ,'8979237401')")

conn.commit()
print('Items inserted successfully')

info = conn.execute("SELECT * FROM Pantry");  
  
for row in info:  
   print ("FoodName = ", row[0])  
   print ("Quantity = ", row[1])  
   print ("Description = ", row[2])
   print ("PickupAdress = ", row[3])
   print ("ContactNumber = ", row[4],"\n")
   