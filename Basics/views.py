from django.shortcuts import render

# Create your views here.
def Collegehome(request):
    return render(request,"Basics/CollegeHome.html")









#Simple Calculator
def Calculation(request):
    if request.method=="POST":
        no1=int(request.POST.get("txtno1"))
        no2=int(request.POST.get("txtno2"))
        btn=request.POST.get("btnSubmit")
        if btn=="+":
            result=no1+no2
        elif btn=="-":
            result=no1-no2
        return render(request,"Basics/Calculator.html",{'res':result})
    else:
        return render(request,"Basics/Calculator.html")


#Aera of a Circle
def circlearea(request):
    if request.method=="POST":
        r=int(request.POST.get("txtradius"))
        btn=request.POST.get("btnSubmit")
        if btn=="Find":
            result=3.14*(r*r)
        return render(request,"Basics/Circle.html",{'res':result})
    else:
        return render(request,"Basics/Circle.html")



#Largest of three Numbers
def Largest(request):
    if request.method=="POST":
        no1=int(request.POST.get("txtno1"))
        no2=int(request.POST.get("txtno2"))
        no3=int(request.POST.get("txtno3"))
        btn=request.POST.get("btnSubmit")
        if (no1 > no2) and (no1 > no3):
            result=no1
        elif (no2 > no1) and (no2 > no3):
            result=no2
        else:
            result=no3
        return render(request,"Basics/Largestof3.html",{'res':result})
    else:
        return render(request,"Basics/Largestof3.html")



# Check whether the number is palindrome or not
def Reverse(request):
    if request.method=="POST":
        no1=int(request.POST.get("txtno1"))
        d=0
        rev=0
        temp=no1
        result=0
        btn=request.POST.get("btnSubmit")
        while (no1>0):
            d=no1%10
            rev=rev*10+d
            no1=no1//10
        if(rev==temp):
            result=1
        if(result==1):
            return render(request,"Basics/Paliandrome.html",{'res':"the Number {0} is palindrome".format(temp)})
        else:
            return render(request,"Basics/Paliandrome.html",{'res':"the Number {0} is not palindrome and reverse of the number is {1}".format(temp,rev)})

    else:
        return render(request,"Basics/Paliandrome.html")





# Palindrome Numbers between two numbners
def Limits(request):
    if request.method=="POST":
        no1=int(request.POST.get("txtno1"))
        no2=int(request.POST.get("txtno2"))
        d=0
        rev=0
        result=0
        btn=request.POST.get("btnSubmit")
        for i in range(no1,no2):
            temp=i
            while (i>0):
                d=i%10
                rev=rev*10+d
                i=i//10
            if(rev==temp):
                return render(request,"Basics/Palinbtwn2limit.html",{'res':temp})
    else:
        return render(request,"Basics/Palinbtwn2limit.html")



# Rank List of a Student

def Student(request):
    if request.method=="POST":
        firstname=request.POST.get("txtfirstname")
        lastname=request.POST.get("txtlastname")
        gender=request.POST.get("radio")
        dept=request.POST.get("ddldepartment")
        mark1=int(request.POST.get("txtmark1"))
        mark2=int(request.POST.get("txtmark2"))
        mark3=int(request.POST.get("txtmark3"))
        btn=request.POST.get("btnSubmit")
        if dept=="BCA":
            result="BCA"
        elif dept=="bCOM":
            result="bCOM"
        elif dept=="BBA":
            result="BBA"
        else:
            result="Select Department"   
        
        total=mark1+mark2+mark3
        per=(total/150)*100
        if gender=="Male":
            gender="Male"
            name="Mr."+firstname+" "+lastname
        else:
            gender="Female"
            name="Miss."+firstname+" "+lastname
        
        if per>80:
            grade="A"
        elif per>60:
            grade="B"
        elif per>40:
            grade="C"
        elif per>30:
            grade="D"
        else:
            grade="Fail"
           
        return render(request,"Basics/RankList.html",{'name':name,'gender':gender,'dept':result,'total':total,'per':per,'grade':grade})
    else:
        return render(request,"Basics/RankList.html")




# Employee Details & Net salary

def Salary(request):
    if request.method=="POST":
        firstname=request.POST.get("txtfirstname")
        lastname=request.POST.get("txtlastname")
        gender=request.POST.get("radio")
        dept=request.POST.get("ddldepartment")
        base=int(request.POST.get("txtsalary")) 
        btn=request.POST.get("btnSubmit")
        if dept=="Sales":
            result="Sales"
        elif dept=="Marketing":
            result="Marketing"
        elif dept=="Finaces":
            result="Finaces"
        elif dept=="Production":
            result="Production"
        else:
            result="Select Department"   
        if gender=="Male":
            gender="Male"
            name="Mr."+firstname+" "+lastname
        else:
            gender="Female"
            name="Miss."+firstname+" "+lastname
        
        if base>=25000:
            TA=base*.4
            DA=base*.35
            HRA=base*.3
            LIC=base*.25
            PF=base*.2
            NET=base+TA+DA+HRA-LIC-PF
        elif base>=15000:
            TA=base*.35
            DA=base*.3
            HRA=base*.25
            LIC=base*.2
            PF=base*.15
            NET=base+TA+DA+HRA-LIC-PF
        else:
            TA=base*.3
            DA=base*.25
            HRA=base*.2
            LIC=base*.15
            PF=base*.1
            NET=base+TA+DA+HRA-LIC-PF
           
        return render(request,"Basics/Employee.html",{'name':name,'gender':gender,'dept':result,'net':NET,'base':base,'PF':PF,'LIC':LIC})
    else:
        return render(request,"Basics/Employee.html")

