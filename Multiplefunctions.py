class multiplefunctions():
    def oddeven():
        num=int(input("enter the number:"))
        if((num%2==0)):
            print("even number")
            message="even number"
        else:
            print("odd number")
            message="odd number"
        return message    
    
    def percentage():
        sub1=int(input("subject1:"))
        sub2=int(input("subject2:"))
        sub3=int(input("subject3:"))
        sub4=int(input("subject4:")) 
        sub5=int(input("subject5:"))
        total=sub1+sub2+sub3+sub4+sub5
        print("total:",total)
        cate="total"
        percentage=total/5
        print("percentage:",percentage)
        cate="percentage:",percentage
        return cate
    
    def elegiblecategory():
        gender=input("enter your gender\n'm'for male'f' for female:")
        age=int(input("enter your age:"))          
        print("your gender:",gender)
        print("your age:",age)
        print("elegible" if ((age>=18 and gender=='f')or(age>=21 and gender=='m'))else"not elegible")
    

    
    def areaoftriangle():
        height=3
        breadth=4
        area=(height*breadth)/2
        print("area of triangle:",area)
        trianglearea=("area:",area)
        return trianglearea
    def perimeteroftriangle():
        height1=3
        height2=4
        breadth=45
        perimeter=height1+height2+breadth
        print("perimeter of triangle:", perimeter)
        triangleperimeter="perimeter:",perimeter
        return triangleperimeter
  