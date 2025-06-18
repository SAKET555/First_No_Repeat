def first_non_repeating(string):
    freqMap = {}
    for char in string:
        if char in freqMap:
            freqMap[char]+=1
        else:
            freqMap[char]=1
    for i in range(0,len(string) - 1):
        if freqMap[string[i]] == 1:
            return i
    return -1
string = input("Please enter your string: ")
my_solution = first_non_repeating(string)
print("Answer is " , my_solution )