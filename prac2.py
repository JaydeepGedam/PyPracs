lb = int(input("\nEnter the lower limit : "))
ub = int(input("Enter the upper limit : "))

print("\nAll prime numbers between ",lb," and ",ub," are : ")
for no in range(lb,ub+1):
    count = 0
    for i in range(2,no):
        if no%i == 0:
            count = 1
            break
    if count==0:
        print(no,end="\t")

print("\n")





