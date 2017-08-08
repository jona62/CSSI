#-------------------------------------------
'''
height=int(raw_input("Enter Height: "))
width=int(raw_input("Enter Width: "))
def custombox(width, height):
    box= ''
    for i in range(width):
        box= box + '#'
    for i in range(height):
        print box
custombox(height,width)
'''
#------------------------------------------
'''
height=int(raw_input("Enter Height: "))
width=int(raw_input("Enter Width: "))
def custombox(width, height):
    for i in range(height):
        if i>=2 and i<=(height-3):
            print "##"+" " *(width-4)+"##"
        else:
            x= 0
            while x <= 6:
                print x
            print "#" * (width)

custombox(height,width)
'''
#--------------------------------------------
'''
def custombox():
    tbborder = "  #########"
    lrborder = "#       #"
    print '   123456'
    print tbborder
    for i in range (8):
        print (chr(65 + i) + lrborder)
    print tbborder

custombox()
'''
#--------------------------------------------
'''
def custombox():
    tbborder = "###########################"
    lborder = "#                        "
    rborder = "#"

    print tbborder
    for i in range (8):
        print (lborder + chr(65 + i) + rborder)
    print tbborder

custombox()
'''

#---------------------------------------------
'''
for i in range (8):
    for i in range (1,9):
        if i == 1:
            print chr(65) + str(i)
        elif i == 8:
                print chr(65  + i -1) + str(i)
        else:
            print chr(65 + i) + str(i)
'''
#---------------------------------------------
#print   "{0} and {1} {2} up the {3}".format("jack","jill","ran","hill")
#--------------------------------------------
'''
def drawbox():
    info = ""
    info = ("#" * 27)+ '\n'
    for j in range(8):
        info = info + "# "
        for i in range(1,9):
            info = info + chr(65+j) + str(i)
            if i != 8:
                info = info + " "
        info = info + " #\n"
    info = info + ("#" * 27)
    print info
drawbox()
'''
