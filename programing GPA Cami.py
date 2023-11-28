# program in puthon that calculates the student's GPA
classno=None
while classno==None:
    try:
        classno=int(input("How many subject you are taking?"))
    except:
        print ("Error,Please enter numbers!\n")
output=0
i=0
while i<classno:
    grade=input("Enter your grade in letter for the %s class." %(str(i+1)))
    grade=grade.upper()
    if grade== 'A' or grade== 'B' or grade== 'C' or grade== 'F':
        i+=1
        if grade== 'A':
            output+=4
        elif grade== 'B':
            output+=3
        elif grade== 'C':
            output+=2
        elif grade== 'D':
            output+=1
        elif grade== 'F':
            output+=0
        print (output)
    else:
         print ("Invalid grade,Please Enter : A, B, C, D or F!\n")
average="%.2f" % (float(output)/float(classno))
print ("Your GPA is: %s" %(str(average)))
