num1=int(input('enter a number: '))
temp=num1
sum=0
count = len(str(num1))
while num1>0:
    rem=num1%10
    num1=num1 // 10
    sum += rem**count  # or  sum += rem**(len(str(temp)))

print ('armstrong number') if sum == temp else print('not a armstrong number')

def check_armstrong(num1):
    temp=num1
    sum=0
    while num1>0:
        rem=num1%10
        num1=num1 // 10
        sum += rem**(len(str(temp)))

    if sum == temp:
        return temp 
    else:
        return None
    
n=int(input('enter a number: '))
for i in range(1,n):
    result = check_armstrong(i)
    if result is not None:
        print(result)


num1=int(input('enter a number: '))
count=len(str(num1))
sum = 0
temp=num1
for i in str(num1):
    sum += int(i)**count
print("armstrong number") if sum == temp else print('not an armstrong number')
    
def check_armstrong(i):
    temp=i
    count = len(str(i))
    sum=0
    for j in str(i):
        sum += int(j) ** count
    if temp == sum:
        return temp
    
num1=int(input('enter a number: '))
for i in range(1,num1+1):
    result = check_armstrong(i)
    if result:
        print(result)