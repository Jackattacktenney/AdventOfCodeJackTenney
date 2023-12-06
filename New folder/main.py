with open('textdocument.txt', 'r') as f:
    line_list = f.readlines()
    
x = 0
calc = str(0)
sum = 0

def numConcat(num1, num2):
    return int("{}{}".format(num1, num2))
def my_reverse(x):
    return x[::-1]
def isnumberspelled(input):
    while True:
        if input.startswith("one") or (input[0:1].isdigit and input[0:1] == "1") == True:
            return(1)
        elif input.startswith("two") or (input[0:1].isdigit and input[0:1] == "2") == True:
            return(2)
        elif input.startswith("three") or (input[0:1].isdigit and input[0:1] == "3") == True:
            return(3)
        elif input.startswith("four") or (input[0:1].isdigit and input[0:1] == "4") == True:
            return(4)
        elif input.startswith("five") or (input[0:1].isdigit and input[0:1] == "5") == True:
            return(5)
        elif input.startswith("six") or (input[0:1].isdigit and input[0:1] == "6") == True:
            return(6)
        elif input.startswith("seven") or (input[0:1].isdigit and input[0:1] == "7") == True:
            return(7)
        elif input.startswith("eight") or (input[0:1].isdigit and input[0:1] == "8") == True:
            return(8)
        elif input.startswith("nine") or (input[0:1].isdigit and input[0:1] == "9") == True:
            return(9)
        elif input.startswith("zero") or (input[0:1].isdigit and input[0:1] == "0") == True:
            return(0)
        else:
            input = input[1:]
        






def calculate(thing):
    d = 0
    k = 0
    temporaryIndex = 0
    temporaryIndex2 = 0
    reversedd = my_reverse(thing)
    measure = True
    for d in thing:
        if d.isdigit() == True and measure == True:
            temporaryIndex = d
            measure = False
    measure = True
    for k in reversedd:
        if k.isdigit() == True and measure == True:
            temporaryIndex2 = k
            measure = False
            return(numConcat(temporaryIndex, temporaryIndex2))




while x < len(line_list):
    calc = str(line_list[x])
    sum = sum + calculate(calc)
    
    x = x + 1
print(isnumberspelled("1twooeqwgo"))