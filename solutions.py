def draw_diamond(height): 
  diameter = height // 2    
  if height %2 ==0:                               #fixes the line after the middle line to make it look like a diamond if height is even
    diameter = diameter - 1                         
  for i in range(height):                           #for loop to iterate through the lines I want printed
    if i <= diameter:                               #if statement for the top half of the diamon
      hashtag_number = 2*i + 1
    else:                                          #else for the bottom half of the diamond
      hashtag_number = 2 *(height - i -1) +1
    spaces = (height - hashtag_number) // 2         #spaces before hashes
    line = ' ' * spaces + '#' * hashtag_number 
    print(line)


draw_diamond(5)

def draw_right_triangle(heightdrt):
  for i in range(heightdrt +1):              #for loop to include the whole height
    lines = i * '#'                         #each line is i times the character
    print(lines)

draw_right_triangle(5)

def compound_interest(amount, annual_rate, time):
  for i in range(time):
    amount = amount + amount* annual_rate                  #amount is updated in each loop with its new value
  print(f'Your compound interest rate after {time} years is ${amount:.2f}')  

compound_interest(1000, 0.05, 5)

def draw_hollow_square(size, thickness):
  edges = size - thickness              #edges and center are variables used later in the for loop
  center = size - 2*thickness
  line3 = ' '
  for i in range(size +1):                  #for loop that says that evaluates what the string should be at each i (i representing a line)
    if i >= thickness and i <=edges:
      line3 = '#'*thickness + ' '* center + '#'*thickness
    else:  
      line3 = '#'* size  
    print(line3)  
   
draw_hollow_square(8,2)

#def greet(name: str) -> str:
 # """Function produces a greeting string with. It uses an f-string in the
  #return statement, that inserts the value of parameter {name} to the 
  #produced string."""
 # return f"Hello {name}. How are you?"

# Create a list of friends to use in the next method. It would be nice if your 
# list was not the same as mine -- unless you are into LOTR as much as I am
# and you can prove it by reciting the One Ring's Tengwar in Black Speech.
#my_friends = ["Frodo", "Sam", "Gandalf", "Saruman", "Elrond"]


#def greet_friends(friends: list[str]) -> None:
 # """Function takes a list of strings, parses it one string at a time, and
  #passes the strign to the greet function whose output is then passed to
  #the print statement, for display."""
  #for name in friends:
   # print(greet(name))


# We need the math module to computer square roots
#import math

#def solve_quadratic(a: float, b: float, c: float) -> None:
  #"""Basic solution to the quadratic equation. The equation
  #a*x*x + b*x + c = 0
  #has solutions in the real numbers if its discriminant is not negative.
  #The discriminant is the quantity b*b-4*a*c. The function below computes
  #the discriminant first. It then checks its sign -- if it's negative, the
  #function prints "no real solutions" and stops. If the discriminant is not
  #negative, the function computes the two solutions for the equation and 
  #prints them. """
  # Compute the discriminant -- it's important to determine if the equation 
  # has no real solutions
  #discriminant = b * b - 4 * a * c
  # Check for real solutions
  #if discriminant < 0:
   # print ("no real solutions")
  #else:
    # Group common operations together
   # common_factor = math.sqrt(discriminant)/(2*a)
   # x1 = - b + common_factor # alternative x1 = (-b + math.sqrt(discriminant))/(2*a)
    #x2 = - b - common_factor # alternative x2 = (-b - math.sqrt(discriminant))/(2*a)
    #print(f"{x1=}\n{x2=}")
  
# Basic testing
#solve_quadratic(1,2,3)
#solve_quadratic(1,5,1)
#greet_friends(my_friends)
