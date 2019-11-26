# CSCA20 Project Report

## Team

--------

**Team Member A**  
First Name: Jerric
Last Name: Cheng 
Student Number: 1002597059
UofT E-mail Address: jerric.cheng@mail.utoronto.ca

**Team Member B**  
First Name: Roy
Last Name: Ching
Student Number:1002659312
UofT E-mail Address:roy.ching@mail.utoronto.ca

**Team Member C (Optional)**  
First Name: Ji Tai Byron 
Last Name: Chou
Student Number:1004605616
UofT E-mail Address:Chou.byro@mail.utoronto.ca

## Project Plan

--------

### Project Title: Guess Who Game

### Description

We will extend the retrieved Guess Who code to provide a fully functional game of Guess Who. The individual will be randomly chosen by the AI from a list of characters which are retrieved from a CSV file allowing custom data files. The individuals will also be stored in the function 'dictionary' and the player can ask questions about the traits with a limited guesses. We further added in additional code that will display an image of these characters. 

Our final project will give users the abilities to:
- Ask about traits of the individual (ie. hair colour, eye colour, gender, etc.)
- Implement random selection from list of individuals 
- Allow the player to have up to 3 guesses
- Import data from a CSV and store the data in dictionary for increased efficiency
- Display an image with individuals to guess from 
- Additional 'help' command that allows an individual to access all commands and information needed

To initiate the code, the installation of pillow is required. This allows the images of the indiviudals to be displayed. The next tep is to open Wing and click the green arrow

### Weekly Plan

**Before** the first tutorial will have:

- A baseline function for how to run Guess Who 
    - how the computer will interact with the player
- A completed CSV of the individuals for the game 
- Desigination of roles to efficiently complete the game 

**After** the first tutorial will have:

- A displayable picture of the individuals  
- Ability to store data from CSV file into the dictionary 

What is your backup plan if things don’t work out as planned?

- direct storage into the dictionary through written code 
- remove picture idea 

## Weekly Reports

-----------------

### Week 1 Report

This week we had planned to have the data reading from the CSV file before the lab and would spend the lab working on methods to implement random selection from the list of characters in the CSV file. However, it turned out that retrieving data from the file format was more complicated than we thought. This resulted in us spending half of the lab time finding alternative solutions. After receving multiple solutions, we decided that the best solution was to implement the dictionary function so we could store the CSV data. Furthermore, we also decided that we would try to implement an image into our code/ Lastly, we also decided to include a limit to how many guesses are avaliable.

### Final Week Report

We managed to incoroporate in 3 extra functions which:

- Store all the individuals in the dictionary from the CSV file
- Add a random selection from the list of individuals
- Inclusion of picture image of the list of individuals

Since our tutorial is on Tuesday, we had no extra time to work.

## References

-------------

We shamelessly copied the starter code from the internet, found at:
https://repl.it/@kinn5721/Guess-Who-1?fbclid=IwAR13mzIUYC4CSJ5m5Y_VV_tzADb9l-eZ-1zJFXmaSYWskgOqEkC1i3Bmn7c

- Lines 0 - 125 are *not* our work.
- Lines 128 - 197 were implemented by us, but designed by CSCA20's lab8 creator.

## Repo & Video

---------------

Our Python code is uploaded to:
https://github.com/angelazb/CSCA20F19/blob/master/store/store.py

And out video is at:
https://www.youtube.com/watch?v=oHg5SJYRHA0
