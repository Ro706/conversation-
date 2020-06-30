#conversion program
#NO CODE IS RUN HERE,IT IS TELLING US WHAT WE WILL DO LATER
#HERE WE WILL DEFINE OUR FUNCTIONS
#THIS PRINT THE MAIN MENU AND PROMPTS FOR A CHOICE

def menu():
   #print what options you have
   print "welcome to conversion.py"
   print "your options are:"
   print ""
   print "1)inch into cm"
   print "2)m into inch"
   print "3)cm into inch"
   print "4)inch into m"
   print "5)foot into inch"
   print "6)pound into kg"
   print "7)kg into pound"
   print "8)Quit conversion.py"
   print ""
   return input("choose your option:")
#THIS WILL CONVERT INCH INTO CM
def ic(n):
    print n,"*",2.54,"=",n*2.54,"cm"

#THIS WILL CONVERT METRE INTO INCH
def mi(n):
    print n,"*",39.37,"=",n*39.37,"inch"

#THIS WILL CONVERT CM INTO INCH
def ci(n):
    print n,"*",0.394,"=",n*0.394,"inch"

#THIS WILL CONVERT INCH INTO METRE
def im(n):
    print n,"*",0.0254,"=",n*0.0254,"m"

#THIS WILL CONVERT FOOT INTO INCH
def fi(n):
    print n,"*",12,"=",n*12,"inch"

#THIS WILL CONVERT POUND INTO KG
def pk(n):
    print n,"*",0.4536,"=",n*0.4536,"kg"

#THJS WILL CONVERT KG INTO POUND
def kp(n):
    print n,"*",2.20,"=",n*2.20,"pound"

#NOW THE PROGRAM REALLY STARTS,AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
  choice = menu()
  if choice == 1:
      ic(input("n: "))
  elif choice == 2:
      mi(input("n: "))
  elif choice == 3:
      ci(input("n: "))
  elif choice == 4:
      im(input("n: "))
  elif choice == 5:
      fi(input("n: "))
  elif choice == 6:
      pk(input("n: "))
  elif choice == 7:
      kp(input("n: "))
  elif choice == 8:
      loop = 0
print "thank u for using conversion.py!"
print "made by ----Ro706"

#NOW THE PROGRAM REALLY FINISHES
