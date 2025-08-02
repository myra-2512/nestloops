word=str(input("Enter your own choice of word:"))
char=str(input("Enter your own choice of letter:"))

i=0
count=0

while i < len(word):
   
    if (word[i] == char):
        count =count+ 1
    i=i+1

print("The total no. of times ",char,"has occurred in the word",word,"is:",count)

#Activity2

lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))

print("Prime numbers between,",lower,"and",upper,"are:")

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

#Activity3

num=int(input("Enter a number:"))
t=num
numlen=0

while t>0:
    numlen=numlen+1 
    t=int(t/10)

if numlen>=4:
    numlen=int(numlen/2)
    chk=0
    while num>0:
        rem=num%10
        if chk==numlen:
            midone=rem
        elif chk==(numlen-1):
            midTwo=rem
        num=int(num/10)
        chk=chk+1
    prod=midone*midTwo
    print("\nThe product of mid digits ",midone, " and ", midTwo, " is: ", prod)
else:
    print("\nThe number is not a 4 digit number or more than 4 digits")
        