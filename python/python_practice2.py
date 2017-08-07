'''Name=raw_input("Enter a Name: ")
collect = []
n = ""

def alternate(Name):
    for x in range (0,len(Name)):
        if x % 2 == 0:
            n = n + Name[x].upper()
        else:
            n = n + Name[x].lower()

        print (n)
alternate(Name)

Student= {
"10005776":"Abigial",
"10005777":"Egide",
"10005778":"Elvis",
"10005779":"Imran",
"10005780":"Jonathan",
"10005781":"Nusrath",
"10005782":"Rahid",
"10005783":"Rayona",
"10005784":"Olawale",
"10005785":"Olivia",
"10005786":"Zanif"
}

def studentLookUp(dict, name):
    name=name.lower()
    name=name.strip()
    name=name.capitalize()
    for x in dict:
        if name == dict[x]:
            return x
            #print Student[string.capitalize()]
    return "Invalid Student name"

name=raw_input("Enter a name: ")
print name.capitalize()
print studentLookUp(Student,name)

'''
def author()
    Jonathan James
import random
random.randint(1,200)
