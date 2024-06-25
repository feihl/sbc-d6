
word = input("Enter a text: ")

for temp in word:
    temp = "".join(reversed(word.replace(" ", "").lower()))
    if temp == word.lower().replace(" ", ""):
        print(f"{word} this is a Palindrome")
        break
    else:
        print(f"{word} this is not a Palindrome")
        break