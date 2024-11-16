import random #slot machine generates values randomly.
MAX_LINES = 3 #this is a global constraint so the value will be constant throughout the program.
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {   # made a dictionary here.
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {   # made a dictionary here.
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [] #creating a list to select values randomly
    for symbol, symbol_count in symbols.items(): #we get keys and values in the dictionary.
        for _ in range(symbol_count): #_ is an anonymous variable.
            all_symbols.append(symbol)

    columns = [] # we define a column list.
    for _ in range(cols): #we generate a column for every single column we have.
        column = [] #we created an empty list
        current_symbols = all_symbols[:] #: is a slice operator and it copies the symbols of all symbols list.
        for _ in range(rows): 
            value = random.choice(all_symbols)
            current_symbols.remove(value) #removes the values before the next selection.
            column.append(value) #add the value to the column.
        columns.append(column) #add the column to the columns list. 
    return columns      


def print_slot_machine(columns):
    for row in range(len(columns[0])): #row depends upon column length.
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end = " | ") #we dont need this pipe for last column, so we did these above steps.
            else:
                print(column[row], end = "")
        print()        


def deposit(): #made a function used to access input from the user.
    while True: #if its true
        amount = input("What amount are you depositing? $") 
        if amount.isdigit(): #checking whether the user has entered a number.
            amount = int(amount) #converting that number to an integer.
            if amount > 0:
                break #while loop breaks here
            else:
                print("The amount must be greater than 0.")
        else:
             print("Please enter the amount in numbers.")  #this is executed when the user has not typed in a number, so after isdigit part, it jumps here.
    return amount      
  

def get_number_of_lines(): #made a function used to get input about lines to bet from the user.
    while True:
        lines = input("Enter the number of lines you wanna bet on (1-" + str(MAX_LINES) + ")? ") #a concatenation is done here for a range to select from.
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number to bet on")
        else:
          print("Please enter a number")
    return lines


def get_bet():
    while True: #if its true
        amount = input("What amount are you betting on each line? $") 
        if amount.isdigit(): #checking whether the user has entered a number.
            amount = int(amount) #converting that number to an integer.
            if MIN_BET <= amount <= MAX_BET:
                break #while loop breaks here
            else:
                print(f"The amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
             print("Please enter the amount in numbers.")  #this is executed when the user has not typed in a number, so after isdigit part, it jumps here.
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
          print(f"You do not have enough balance to bet that amount, your current balance is {balance}")
        else:
          break
    print(f"You are betting ${bet} on {lines} lines. Total Bet = ${total_bet}")    

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet
    

def main(): # when the user wants to play again, this function is called again.
  
    balance = deposit()
    while True:
        print(f"Your current balance = ${balance}.")
        answer = ("Press enter to play and q to quit")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Your left with ${balance}.")

main()










