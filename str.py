def Count(str1, sub, boolean):
    count = 0
    r = len(str1)
    p = len(sub)
    
    if r != 0:
        if p != 0:
            i = 0
            while i <= r - p:
                if boolean:
                    # Case-sensitive match without overlapping
                    if str1[i:i + p] == sub:
                        count += 1
                        i += p  # Skip over the matched substring to avoid overlap
                    else:
                        i += 1
                
                else:  # boolean == False
                    # Case-insensitive match with overlapping
                    if str1[i:i + p].lower() == sub.lower():
                        count += 1
                    i += 1  # Move by 1 to allow overlapping

        else:
            print("TypeError: count() takes at least 2 arguments (1 given)")
    else:
        print("TypeError: count() takes at least 2 arguments (0 given)")
    
    return count

# Input from the user
str1 = input("Enter the main string: ")
sub = input("Enter the substring to search: ")
boolean_input = input("Enter True or False for case-sensitive matching: ").strip()

# Convert string input to boolean
if boolean_input == "True":
    boolean = True
elif boolean_input == "False":
    boolean = False
else:
    raise ValueError("Invalid input for boolean. Enter 'True' or 'False'.")

print(Count(str1, sub, boolean))

