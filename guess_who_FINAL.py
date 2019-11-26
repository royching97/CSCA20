import csv
import random
from PIL import Image

# The data is stored in an external csv file
f = open('guess_who1.csv', 'r')
# Open the csv file so we can read it
reader = csv.reader(f)

# Create a dictionary to store the file data
# Make it easier to retrieve the data, reduce clutter of code from writing all the data in a dictionary
people = { }

for row in reader:
# We want to store the names of the characters as the keys
    people[row[0]] = {'gender':row[1], 'hair_colour':row[2], 'hat':row[3],'age':row[4],'height':row[5],'glasses':row[6],'eye_colour':row[7]}
    # Inside each name key, we create another dictionary to store their traits
    # When the key is called, the code will retrieve the traits that the user can ask about
    # We assign the rows to labels that are easy to remember so we can recall them later

# Selecting a random person from the list of keys
x = random.choice(list(people.keys()))
# Now we store the randomly selected person into a variable
# It will store the entire dictionary of their traits because we are calling the key
mysteryperson = people[x]
# Name of person is stored in a separate variable so we can compare it to their guess at the end of the game
answer = x

# Setting up the game, we need to indicate when the user is 'playing'
# 'Playing' will be when the user is asking questions and obtaining information, while guessing will come after the playing phase
playing = True
# We want to track the pieces of information the user will obtain
info_count = 0
# The limit of information will add difficulty to the game and tell the code when to proceed to the guessing phase 
info_limit = 3

print("I have chosen a random person, can you guess who it is?\nYou have a maximum of 3 pieces of information (If you need help, ask for 'help')")

# Simple loop using boolean to run the game
while playing:
    # Play phase will continue as long as info limit isn't reached
    if info_count < info_limit:
        question = input('What would you like to know? ')
        if 'help' in (question.lower()):
            # Display the required input strings that will be used to retrieve info from the dictionary
            print("You can ask about the their '[gender, hair colour, hat, age, height, glasses, eye colour]'\nYou can 'guess' at any point in the game, but you MUST guess after 3 pieces of information")
            img = Image.open('the_family.png')
            img.show()
            '''
            The list of possible people will display
            '''
        elif 'gender' in (question.lower()):
            '''  
            'gender' in (question.lower()) - The lower argument will ensure that the user input will be read by the code and not crash based on case sensitivity. 
            
            The user input will be converted into lowercase and compared with our string label 'gender'
            
            As long as 'gender' is found anywhere in the string of user input, the code will read it and proceed by outputting the gender information of the selected person
            
            REQ: 'gender' must be present in the string and spelt correctly
            
            Example:
            >>> gender
            >>> Gender
            >>> GEndeR
            >>> what is the person's gender
            >>> asdfasdfagkgender
            The person is male
            
            '''
            # Use the dictionary key to retrieve 'gender' label which we assigned to a row earlier
            gender = (mysteryperson['gender'])
            # Output the gender
            print('The person is ' + (gender))
            # Increase the info_count because a piece of information was obtained by the user
            # Progress the game
            info_count += 1
            
        elif 'hair colour' in (question.lower()):
            haircolour = (mysteryperson['hair_colour'])
            print("The person's hair colour is " + (haircolour))
            info_count += 1
            
        elif 'hat' in (question.lower()):
            hat = (mysteryperson['hat'])
            # Read the string found on the data file
            # Determine whether or not the trait is present
            if hat == 'hat':
                print('The person wears a hat')
                info_count += 1
            else:
                print('The person does not wear a hat')
                info_count += 1
                
        elif 'age' in (question.lower()):
            age = (mysteryperson['age'])
            print('The person is ' + (age) + ' years old')
            info_count += 1
        
        elif 'height' in (question.lower()):
            height = (mysteryperson['height'])
            print('The person is ' +(height))
            info_count += 1
            
        elif 'glasses' in (question.lower()):
            glasses = (mysteryperson['glasses'])
            if glasses == 'glasses':
                print('The person wears glasses')
                info_count += 1
            else:
                print('The person does not wear glasses')
                info_count += 1
                
        elif 'eye colour' in (question.lower()):
            eye_colour = mysteryperson['eye_colour']
            if eye_colour == 'brown_eyes':
                print('The person has brown eyes')
                info_count += 1
            else:
                print('The person has blue eyes')
                info_count += 1
        
        # If the user wants to guess before they obtain the maximum amount of info pieces, they have the option
        elif 'guess' in (question.lower()):
            # We have to switch the state of the game from playing to guessing
            playing = False
            # Exit the loop
        
        # Should the user fail to correctly input a string that will trigger information, there is a catch all statement   
        else:
            # Prompt the user to ask for help
            # Don't increase the info_count because user failed to obtain any information
            print("Sorry, that is not an option. Type 'help' for a list of commands.")
    
    # When info_count reaches the limit, we have to switch the game from playing to guessing
    else:
        playing = False
        # Exit the loop of playing

if playing == False:
    # If maximum information was obtained, user is prompted to guess because they cannot ask any more questions
    if info_count == info_limit:
        print('***You are out of info pieces, you must guess*** ')
    guess = input('Who is the mystery person? ')
    if (answer.lower()) in (guess.lower()):
        # Eliminate case sensitivity bugs and crashing
        # Make both the answer string and input string all lower case
        # As long as the name is correctly spelt anywhere in the string, user will win
        print("That's correct, you win!")
    else:
        # If user incorrectly guesses, will output the mystery person
        print('Sorry, that is incorrect. The mystery person was ' + (answer.capitalize()))
