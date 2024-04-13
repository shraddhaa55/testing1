class Date:
    def __init__(self,d,m,y):
        self.d=d
        self.m=m 
        self.y=y
        
    def day(self):
        print("day=",self.d)
    def month(self):
        print("day=",self.m)
    def year(self):
        print("day=",self.y)
         
    def month_name(self):
        months=["unknown","jan","feb","march","april","may","june","july"
                ,"sep","oct","nov","dec"]
        print("Month name=",months[self.m])
        
    def is_leap_year(self):
        if(self.y%400==0) or (self.y%4==0 and self.y%100!=0):
            print("its a leap year")
        else:
            print("its not a leap year")
        
dd=int(input("input the day:"))
mm=int(input("input the month:"))
yy=int(input("input the year:"))
d1=Date(dd,mm,yy) 
d1.day()
d1.month()
d1.year()  
d1.month_name()
d1.is_leap_year()    