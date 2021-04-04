name = 'Nuno Moreira'
age = 30 # not a lie
height = 173 # cm
height_inches = int(round(height * 0.393701, 0)) # inches
weight = 80 # kg
weight_inches = int(round(weight * 2.20462, 0)) # pounds
eyes = 'Red'
teeth = 'Black'
hair = 'White'

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {weight} kg heavy.")
print(f"He's {height_inches} inches tall.")
print(f"He's {weight_inches} pounds heavy.")
print("Actually that's not to heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
