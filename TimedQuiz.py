import time
def timer(nt):
    flag=0
    currt=time.time()
    if (currt-nt)>=8:    #8 secs
        flag=1
        return flag
    
# def score(sc):
#     sc+=1
#     return sc

def opt(a,ol,nt):
    checktime=timer(nt)
    if checktime==1:
       print("Sorry too late")
       return 0
    else:
        answer_list=[2,3,2,2,4,3,3,4,1,1]
        if a==answer_list[ol]:
            print("Correct")
            return 1 
        else:
            print("Wrong")
            return 0  
     
    
def qboard():
   scr=0
   optloop=0
   print("(1) In the Windows XP, what does XP stands for?")
   print("[1] Extra-Powerful\n[2] Experience(.)\n[3] Extended Platform\n[4] Experience Platform")
   nt=time.time()
   ans=int(input("Enter the option as answer: "))
   #opt(ans,optloop,nt)
   s=opt(ans,optloop,nt)
   scr+=s
   optloop+=1 

   print("(2) Which of the given devices is used for counting blood cells?")
   print("[1] Hmelethometer\n[2] Spyscometer\n[3] Hemocytometer\n[4] Hamosytometer")
   nt=time.time()
   ans=int(input("Enter the option as answer: "))
   s=opt(ans,optloop,nt)
   scr+=s
   optloop+=1 

   print("(3) Which of the given compounds is used to make fireproof clothing?")
   print("[1] Aluminum chloride\n[2] Aluminum Sulphate\n[3] Magnesium Chloride\n[4] Magnesium Sulphate")
   nt=time.time()
   ans=int(input("Enter the option as answer: "))
   s=opt(ans,optloop,nt)
   scr+=s
   optloop+=1 

   print("(4) What is the pH value of the human body?")
   print("[1] 9.2 to 9.8\n[2] 7.0 to 7.8\n[3] 6.1 to 6.3\n[4] 5.4 to 5.6")
   nt=time.time()
   ans=int(input("Enter the option as answer: "))
   s=opt(ans,optloop,nt)
   scr+=s
   optloop+=1 

   print("(5) Which of the following is the system bus?")
   print("[1] Bus connecting Keyboard and Motherboard\n[2] Bus connecting Hard Disk and Monitor \n[3] Bus connecting Memory and Monitor\n[4] Bus connecting CPU and Memory")
   nt=time.time()
   ans=int(input("Enter the option as answer: "))
   s=opt(ans,optloop,nt)
   scr+=s
   #optloop+=1 
   print("Final Score: ",scr)

qboard()           
