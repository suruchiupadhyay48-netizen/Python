# PY2 Railway System - Type Casting and Comments
print("Welcome to Indian Railways")

# Train Details
train_name = "Rajdhani Express"
train_number = 12951
print("Train:", train_name,train_number)

# Passenger Info - Type Casting
age = int("20")
price = float("1250.50")
print("Age:",age)
print("Price:",price)

# Ticket Confirmation
print("Ticket Confirmation! Happy Journey!")

print(type(train_name))
print(type(train_number))
print(type(age))
print(type(price))

# Create valid identifiers and literals for passenger information.
passanger_name = "Rahul Sahrma"
seat_number = "B2-45"
is_confirmed = True

# Convert float data into integer data type
Ticket_price_integer = int(price)
print(type(Ticket_price_integer))

#Convert integer data into string format
train_number_string = str(train_number)
print(type(train_number_string))

# Create passenger confirmation variables
#Display ticket confirmation message using formatted output

print("------------Railway Ticket-----------")
print("Passanger Name :", passanger_name)
print("Seat Number :", seat_number)
print("Ticket Status :", is_confirmed)
print("--------------------------------------")
