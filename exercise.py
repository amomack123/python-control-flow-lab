# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
# print_greeting()






# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    letter = input('Enter a letter: ').lower()
    vowels = "aeiou"
    if len(letter) > 1:
        print('Not a valid input!')
    elif type(letter) != str:
        print('Not a valid input!')
    elif letter in vowels:
        print('The letter ' + letter + ' is a vowel.')
    else:
        print('The letter ' + letter + ' is a consonant.')

# Call the function
# check_letter()





# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    age = input('Please enter your age: ')
    try:
        int(age)
    except:
        print("Not an integer!")
        return
    if int(age) > 18:
        print('Old enough to vote.')
    else:
        print('Not old enough to vote.')

# Call the function
# check_voting_eligibility()




# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_years = input("Input a dog's age: ")
    if not dog_years.isdigit() or int(dog_years) <0 :
        print ('Enter valid age')
    else:
        if int(dog_years) > 2:
            dog_years = 10 + 10 + ((int(dog_years) - 2) * 7)
            print(f'The dogs age in dog years is {dog_years}')
        elif int(dog_years) <= 2:
            dog_years = int(dog_years) * 10
            print(f'The dogs age in dog years is {dog_years}')
          
    

# Call the function
# calculate_dog_years()



# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    while True:
      # Your control flow logic goes here
      is_it_cold = input('Is It Cold (Y/N): '.lower())

      if is_it_cold not in ['y', 'n']:
        print('Please select Y or N')
        continue
      
      if is_it_cold :
        is_it_raining = input('Is It Raining (Y/N): '.lower())
        if is_it_raining not in ['y', 'n']:
          print('Please select Y or N')
          continue
        if is_it_cold == is_it_raining== 'y':
          print('Wear a waterproof coat.')
        elif is_it_cold == 'y' and is_it_raining== 'n':
          print('Wear a warm coat.')
        elif is_it_cold == 'n' and is_it_raining== 'y':
          print('Carry an umbrella.') 
        elif is_it_cold == is_it_raining== 'n':
          print('Wear light clothing.') 

# Call the function
# weather_advice()



# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
  while True:
    # Your control flow logic goes here
    month = input('Enter the month of the year (Jan-Dec) 3 character max: ').lower()
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    if month in months :
      day = input('Enter the day of the month (1-31): ')
      if not day.isdigit():
        print('Enter a numerical value')
      elif int(day) > 31:
        print('Enter a value between 1-31')
        continue
      if (month == 'dec' and int(day) >20) or month in ['jan', 'feb'] or (month == 'mar' and int(day) <=19):
        season = 'winter'
      elif(month == 'mar' and int(day) > 19) or month in ['apr', 'may'] or (month == 'jun' and int(day) <=20):
        season = 'spring'
      elif(month =='jun' and int(day) >20) or month in ['jul', 'aug'] or (month == 'sep' and int(day) <=21) :
        season = 'summer'
      elif(month=='sep' and int(day) >21) or month in ['oct', 'nov'] or (month == 'dec' and int(day) <=20) :
        season = 'fall'
      print(f'{month.capitalize()} {day} is in {season}')
    else:
      print('enter valid month with 3 characters')
      continue

# Call the function
# determine_season()



# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
  target_num = 87
  
  for attempt in range(5, -1, -1):
    guess = input(f'Pick a number between 1-100. You have {attempt} guesses: ')
    
    if not guess.isdigit():
      print('Please enter a valid numerical value')
      continue
    
    if not (1<= int(guess) <=100):
      print('Value is out of range, try again')
      continue
    elif int(guess) == target_num :
      print('Congratulations, you guessed correctly!')
      break
    else:
      if int(guess) < target_num :
        print('Guess is too low')
      else:
        print('Guess is too high')
      
      if attempt == 0:
        print('Sorry, you failed to guess the number in five attempts')
      elif attempt == 1:
        print('Last Chance!')
  
  
# Call the function
guess_number()