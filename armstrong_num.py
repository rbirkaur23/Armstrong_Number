n=int(input("Enter a number: "))
store=n
total=0
while n!=0:
    last_digit=n%10
    total=total+(last_digit**3)
    n=n//10
if (total ==store):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

