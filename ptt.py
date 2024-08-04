def print_patterns(n):

 for i in range(n):
   for j in range(i, n):
      print(' ', end=' ')
   for j in range(i):
      print('*', end=' ')
   for j in range(i +1):
     print('*', end=' ')
   print()
   
 for i in range(n-1):
   for j in range(i+1):
     print(' ', end=' ')
   for j in range(i, n-1):
     print('*', end=' ')
   for j in range(i, n):
    print('*', end=' ')
   print()
   
 for i in range(n):
   for j in range(n *3):
     print('*', end=' ')
   print()
n = int(input())
if n in [1, 2, 3]:
    print_patterns(n)
else:
    print("Invalid input.")
