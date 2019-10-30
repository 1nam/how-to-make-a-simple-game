# python using some logic to make a game.
print("can you guess the magic word to open the doors")
word = "open sesame"
magic_word = ""
magic_word_times = 0 # keeps track of guesses
magic_word_limit = 3  # keeps track of guesses
magic_word_end = False
while magic_word != word and not (magic_word_end):
    if magic_word_times < magic_word_limit:
       magic_word =input("Enter Magic Word: ")
       magic_word_times += 1
    else:
        magic_word_end = True
if magic_word_end:
    print("Sorry you cant enter.")
else:    
    print("the doors have opened")
