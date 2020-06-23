# this program is to get a tambola number
import random
import inflect
import pyttsx3


"""This function breaks down the digit and returns ones and tens digit in words
For example: Number like 76 will be returned as Seven Six
"""


def wordify(N):
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six",
             "Seven", "Eight", "Nine"]
    ones_dig = int(N % 10)
    tens_dig = int(N / 10)
    num_in_words = ""
    if tens_dig is 0:
        num_in_words = "Only number"
    else:
        num_in_words = words[tens_dig] + " " + words[ones_dig]
    return num_in_words


def generate_random():
    return random.randrange(1, 100)


def print_opened_chart(numbers):
    for i in range(1, 91):
        if i in numbers:
            print(i, end='\t')
        else:
            print(".", end='\t')
        if i % 10 == 0:
            print()

# Main program begins from here
numbers = []
eng = inflect.engine()  # inflect module is used to convert the number into words
speakeng = pyttsx3.init()   # pytssx3 engine

print("Press Enter to open next number")
print("Press 1 to get the opened numbers")
print("Press 2 to exit")
while len(numbers) < 90:
    user_choice = input()
    if user_choice is '':
        num = generate_random()
        while num in numbers:   # Keep generating the new random number until we find not opened one
            num = generate_random()
        numbers.append(num)
        print(wordify(num) + " " + eng.number_to_words(num) + " " + str(num))
        speakeng.say(wordify(num) + " " + eng.number_to_words(num))
        speakeng.runAndWait()
    elif user_choice is '1':
        print_opened_chart(numbers)
    elif user_choice is '2':
        exit()
    else:
        print("Invalid Choice")



