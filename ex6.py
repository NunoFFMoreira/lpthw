types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}" # {} is the place holder

print(joke_evaluation.format(hilarious)) # The format() method formats the specified value(s) and insert them inside the string's placeholder.

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) # sum of 2 var
