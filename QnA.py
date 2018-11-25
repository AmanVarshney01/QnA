print "let's play a game."

print """1 = Male
2 = Female"""
print ""
num = (input("Are you male or female?: "))
if num == 1:                                                        #Male part
    age = (input("what's your age?: "))
    if age > 20:
        print("App Admi ban chuke hai!")
        print ""
        print "1 = Yes\n2 = No"
        marrige = (input("Are You married?: "))
        if marrige == 1:
            print("App Pati ban chuke hai!")
            print ""
            child = (input("Kitne bache hai apke?: "))
            if child < 1:
                print("Arre! ek bhi nhi ")
            elif child == 1:
                print("sirf ek hi ek aur ker li jiye")
            else:
                print("Zabardast! Itne toh hone chahiye!")
        else:
            print("Toh ker liye jiye umar ho gayi hai!")
    else:
        print("Abhi toh app bache hai!")
else:                                                                #Female part
    agee = (input("what's your age?: "))
    if agee > 20:
        print("App aurat ban chuki hai!")
        print "                                                       "
        print "1 = Yes\n2 = No"
        marrigee = (input("Are You married? "))
        if marrigee == 1:
            print("App Patni ban chuki hai!")
            child = (input("Kitne bache hai apke?: "))
            if child < 1:
                print("Arre! ek bhi nhi ")
            elif child == 1:
                print("sirf ek hi ek aur ker li jiye")
            else:
                print("Zabardast! Itne toh hone chahiye!")
        else:
            print("Toh ker liye jiye umar ho gayi hai!")
    else:
        print("Abhi toh app bachi hai!")
print("")
print "1 = Yes\n2 = Hadddddddd se jyada!"
like = (input("Did you liked this game?: "))
print ""
import os
os.system("pause")

