#Please write a program which asks the user to type in a sentence. 
# The program then prints out the first letter of each word in the sentence, each letter on a separate line.

sentence = input("Please type in a sentence:")

word = 0
if len(sentence) != 0:
    print(sentence[0])
    while word < len(sentence):
        if sentence[word] == " ":
            print(sentence[word+1])
        word += 1

