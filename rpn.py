#!/usr/bin/env python3

import operator
import readline
from gtts import gTTS
import os
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

operator_names = {
    '+': 'plus',
    '-': 'minus',
    '*': 'multiplied by',
    '/': 'divided by',
}

def calculate(myarg):
    stack = list()
    speak = ''
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
            speak = str(arg1) + operator_names[token] + str(arg2)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop(), speak

def main():
    while True:
        result, speak = calculate(input("rpn calc> "))
        print(colored("Result: ", 'red'), colored(result, 'green'))
        tts = gTTS(text=speak + 'is' + str(result), lang='en')
        tts.save("good.mp3")
        os.system("mpg321 -q good.mp3")

if __name__ == '__main__':
    main()
