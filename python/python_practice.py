'''
name1= ["Reid"]
name2= ["Zavala"]

def swap (name1, name2):
    change = name1[0]
    name1[0]=name2[0]
    name2[0]=change

swap(name1,name2)

print "Reid has: ",name1[0]
print "Zavala has: ",name2[0]
'''
'''
#print ("Hello world")

Elvis = 10
def addOne(x, Elvis):
    Elvis = Elvis +1
    return x+1
print 'print results: ',addOne(5, Elvis)
print 'outside the function', Elvis

i=float(raw_input("Enter Temperature in Celsius: "))

def convertC_to_F(C):
    C=C*(1.8)+32
    return C
C=convertC_to_F(i)
print 'Celsius to Fahrenheit = ', convertC_to_F(i)


def convertF_to_K(F):
    K=5/9*(F + 32)+273
    return K
F=convertF_to_K(K)
print 'Fahrenheit to Kelvin = ', convertF_to_K(K)


def convertK_to_C(K):
    C=K-273
    return C
K=convertK_to_C(C)
print 'Kelvin to Celcius = ', convertK_to_C()

user_input=int(raw_input("Enter a number: "))
def isEven(x):
    if (user_input % 2) == 0:
        return True
    elif (user_input % 2) == 1:
        return False
    isEven(x)
print isEven(user_input)

user_input=int(raw_input("Enter a number: "))
def isEvenShort(x):
    return (x % 2) == 0

print isEvenShort(user_input)

def isEvenVerbose(x,verbose):
    i = x % 2 == 0

    if verbose == True:
        if i:
            print "number ",x , "is even"
        else:
            print "number ", x, "is odd"
    return i

isEvenVerbose(7, True)
isEvenVerbose(8, True)
isEvenVerbose(6, True)


def countDown():
    i=10
    while(i>0):
        print(i)
        i=i-1
    return "Launch"
print countDown()

dessert= 'cheesecake'
groceries = ['Eggs', 'Milk', 'Butter', dessert]
print groceries[3]'''
