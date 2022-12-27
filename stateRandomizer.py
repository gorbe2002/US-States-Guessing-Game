import random

# List of US States and their regions:
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# Chooses a random state in "states" list:
randomizedState = random.choice(states)

# Hint 1 (gives the user the first letter of the state):
hint1 = randomizedState[0] 

# Hint 2 (gives the user the region that the state is in):
westRegion = ['Alaska', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming']
midwestRegion = ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin']
southwestRegion = ['Arizona', 'New Mexico', 'Oklahoma', 'Texas']
southeastRegion = ['Alabama', 'Arkansas', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Mississippi', 'North Carolina', 'South Carolina', 'Tennessee', 'Virginia', 'West Virginia']
northeastRegion = ['Connecticut', 'Delaware', 'Maine', 'Maryland', 'Massachusetts', 'New Hampshire', 'New Jersey', 'New York', 'Pennsylvania', 'Rhode Island', 'Vermont']

guess = input("I'm thinking of a state in the United States, can you guess which one I'm thinking about?\n")
guessCounter = 1

while guess != randomizedState:
    print("Nope, guess again!")

    if guessCounter == 1:
        print("Hint 1: this state begins with the letter {}".format(hint1))

    if guessCounter == 2:
        if randomizedState in westRegion:
            print("Hint 2: this state is in the Western region of the United States")

        elif randomizedState in midwestRegion:
            print("Hint 2: this state is in the Midwest region of the United States")

        elif randomizedState in southwestRegion:
            print("Hint 2: this state is in the Southwest region of the United States")

        elif randomizedState in southeastRegion:
            print("Hint 2: this state is in the Southeast region of the United States")

        else:
            print("Hint 2: this state is in the Northeast region of the United States")

    guess = input()
    guessCounter += 1

# Unique output if state is guessed in one attempt:
if guess == randomizedState and guessCounter == 1:
    print("Wow! You guessed it with 1 attempt, congrats!")
    
# Outputs amount of guesses made in total:
else:
    print("You guessed it! It took you {} guesses.".format(guessCounter))
