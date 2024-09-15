def DTB(n):
   if n > 1:
       DTB(n//2)
   print(n % 2,end = '')

dec = int(input("Enter a Decimal No. Between 10 to 100 : "))
DTB(dec)