def Check_word(input_string):
    list = input_string.split()
    longest_word = ""
    vowels = set("aeiouAEIOU")
    for word in list:
        if all(char not in vowels for char in word):
            if len(longest_word) < len(word):
                longest_word = word
    if longest_word ==  "":
        return "No word without vowels"
    return longest_word

input_string = input("Sentence : ")
solution = Check_word(input_string)
print("Answer is ", solution)