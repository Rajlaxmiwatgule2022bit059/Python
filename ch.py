def Change_Case(text, style):
    if style == 'c':
        l = list(text)
        return Capital(l)
    elif style == 's':
        return Small(text)
    elif style == 'r':
        return Reverse(text)
    elif style == 'u':
        return Ultered(text)

def Capital(l):
    formated_text = ''.join([char.capitalize() for char in l])
    return formated_text

def Small(text):
    formated_text = text.casefold()
    return formated_text

def Reverse(text):
    formated_text = ''
    for i, char in enumerate(text):
        if i % 2 == 0: 
            if 'a' <= char <= 'z':
                formated_text += chr(ord(char) - 32)
            else:
                formated_text += char
        else: 
            if 'A' <= char <= 'Z':
                formated_text += chr(ord(char) + 32)
            else:
                formated_text += char
    return formated_text
   

def Ultered(text): 
    formated_text = ''
    for i, char in enumerate(text):
        if i % 2 == 0: 
            if 'A' <= char <= 'Z':
                formated_text += chr(ord(char) + 32)
            else:
                formated_text += char
        else: 
            if 'a' <= char <= 'z':
                formated_text += chr(ord(char) - 32)
            else:
                formated_text += char
    return formated_text


text = input()
style = input("Enter 'c/C' for Capitalization, 's/S' for small, 'r/R' for reverse, 'u/U' for Ultered: ").casefold()
print(Change_Case(text, style))

