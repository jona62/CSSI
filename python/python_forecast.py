import random

class ForeCast:
    def __init__ (self,mode ='F'):
        self.mode = mode
        weekly_ForeCast = {"Sun": 64, "Mon": 1, "Tue": -20, "Wed": -59, "Thu": 72, "Fri": 53, "Sat": 34}
        self.weekly_ForeCast = weekly_ForeCast
# From -84 to 150
    def __F2C__ (self, n):
        C = (5.0/9) * (n - 32)
        return C
    def __F2K__ (self, n):
        K = (5.0/9) * (n - 32) + 273.15
        return K
    def __C2K__ (self, n):
        K = n + 273.15
        return K
    def __K2C__ (self, n):
        C = n - 273.15
        return C

    def setMode (self, new_Mode):
        if new_Mode == "F" or new_Mode == "C" or new_Mode == "K":
            self.mode = new_Mode
        else:
            pass

    def getMonTemp (self):
        r= self.weekly_ForeCast["Mon"]
        if self.mode == "C":
            return self.__F2C__(r)
        elif self.mode == "K":
            return self.__F2K__(r)
        else:
            return r


    def getTueTemp (self):
        r= self.weekly_ForeCast["Tue"]
        if self.mode == "C":
            return self.__F2C__(r)
        elif self.mode == "K":
            return self.__F2K__(r)
        else:
            return r

    def getWedTemp (self):
        r= self.weekly_ForeCast["Wed"]
        if self.mode == "C":
            return self.__F2C__(r)
        elif self.mode == "K":
            return self.__F2K__(r)
        else:
            return r

    def getThuTemp (self):
        r= self.weekly_ForeCast["Thu"]
        if self.mode == "C":
            return self.__F2C__(r)
        elif self.mode == "K":
            return self.__F2K__(r)
        else:
            return r

    def getFriTemp (self):
        r= self.weekly_ForeCast["Fri"]
        if self.mode == "C":
            return self.__F2C__(r)
        elif self.mode == "K":
            return self.__F2K__(r)
        else:
            return r

    def getSatTemp (self):
        r= self.weekly_ForeCast["Sat"]
        if self.mode == "C":
            return self.__F2C__(r)
        elif self.mode == "K":
            return self.__F2K__(r)
        else:
            return r

    def getSunTemp (self):
        r= self.weekly_ForeCast["Sun"]
        if self.mode == "C":
            return self.__F2C__(r)
        elif self.mode == "K":
            return self.__F2K__(r)
        else:
            return r

def week_ForeCast(FC):
    S = "Sun: " + str(round(FC.getSunTemp(),2)) +" "+ "Mon: " + str(round(FC.getMonTemp(),2)) +" "+ "Tue: " + str(round(FC.getTueTemp(),2)) +" "+ "Wed: " + str(round(FC.getWedTemp(),2)) +" "+ "Thu: " + str(round(FC.getThuTemp(),2)) +" "+ "Fri: " + str(round(FC.getFriTemp(),2)) +" "+ "Sat: " + str(round(FC.getSatTemp(),2))
    print S
week_ForeCast(ForeCast("F"))

'''
# for the first Conversion
C = ForeCast("")
K = ForeCast("")
K = ForeCast("")
C = ForeCast("")

print C.__F2C__(32)
print K.__F2K__(21)
print K.__C2K__(-273.15)
print C.__K2C__(273.15)

f1 = ForeCast("")

f1.setMode("K")
print f1.getMonTemp()
'''
