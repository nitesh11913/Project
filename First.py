def palindrome():
    word = input("Enter a word: ")
    word = word.casefold()
    rev_word = reversed(word)
    if list(word) == list(rev_word):
        print("The word ", word, "is a palindrome.")
    else:
        print("The word ", word, "is not a palindrome.")


palindrome()
