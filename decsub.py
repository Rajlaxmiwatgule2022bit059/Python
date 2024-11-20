def str_to_int(num_str):
    result = 0
    for i in range(len(num_str)):
       num = ord(num_str[i]) - 48
       result = result * 10 + num
    return result
num_str = "1234"
converted_value = str_to_int(num_str)
print(converted_value) 

def decimal_subtraction(a, b):
    dec_a = str_to_int(a)
    dec_b = str_to_int(b)
    
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    print(f"Decimal of {a} (Decimal: {dec_a})")
    print(f"Decimal of {b} (Decimal: {dec_b})")
    
    result = ''
    borrow = 0
    
    for i in range(max_len - 1, -1, -1):
        bit_a = int(a[i])
        bit_b = int(b[i])
        
        sub = bit_a - bit_b - borrow
        
        if sub < 0:
            sub += 10  
            borrow = 1  
        else:
            borrow = 0 
        
        result = str(sub) + result  
           
    print(f"Step {max_len - i}: {bit_a} - {bit_b} (borrow {borrow}) -> result bit: {result[0]}")
    
    result = result.lstrip('0')
    if not result:
        result = '0'
    
    
    print(f"Decimal result: {result}")
    
decimal_subtraction('1', '6')

    
    
    
    
    
    

