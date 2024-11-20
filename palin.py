import time
def is_palindrome(l):
    count = 0
    for x in l:
        if isinstance(x, int) or isinstance(x, str):
            s = str(x)  
            if s == s[::-1]:  
                count += 1
    return count

start_time = time.time()
print(is_palindrome(["xyz", 12321, "abcba", 1234321]))
end_time=time.time()
total_time1= start_time - end_time
print(total_time1)

def is_palindrome_with_length_check(l):
    count = 0
    for x in l:
        if isinstance(x, int) or isinstance(x, str):
            s = str(x)  
            if s == s[::-1] and len(s) % 5 == 3:  
                count += 1
    return count

start_time = time.time()
print(is_palindrome_with_length_check(["xyz", 12321, "abcba", 1234321]))  
total_time2= start_time - end_time
print(total_time2)

def is_palindrome2(l):
    count = 0
    for x in l:
        if int == type(x) and str==type(x):
            s = str(x)  
            if s == s[::-1] and len(s) % 5 == 3:  
                count += 1
    return count

start_time = time.time()
print(is_palindrome2(["xyz", 12321, "abcba", 1234321]))  
total_time3= start_time - end_time
print(total_time3)

def is_palindrome3(l):
    count = 0
    for x in l:
        if type(x)==int:
            s = str(x)  
            count+= type(s==str) and len(s)%5==3 and s==s[::-1]
    return count

start_time = time.time()
print(is_palindrome3(["xyz", 12321, "abcba", 1234321]))  
total_time3= start_time - end_time
print(total_time3)

def is_palindro(l):
    count = 0
    for x in l:
        if type(x)==int:
            s = str(x)  
            count+= type(s==str) and len(s)%5==3 and is_palindrome3(s)
    return count

start_time = time.time()
print(is_palindro(["xyz", 12321, "abcba", 1234321]))  
total_time3= start_time - end_time
print(total_time3)

