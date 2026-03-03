def longest(filename):
    file = open(filename, "r") # opens the file
    text = file.read()  # reads the file and stores it in variable text
    words = text.split() # splits the text into different words using space as a separator
    longest = "" # define the variable longest as a, empty text variable

    for word in words:
        if word[0] == "c": # if the word starts with c
            if len(word) > len(longest): # if the word analyzed is longer than the one we found before
                longest = word # replace the previous word with the analyzed word
    file.close() # closes the file
    return longest

print("The longest word in filename is", longest("filename.txt")) # returns the result