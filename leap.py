# In this kata you should simply determine, whether a given year is a leap year or not. 
# In case you don't know the rules, here they are:

# years divisible by 4 are leap years
# but years divisible by 100 are not leap years
# but years divisible by 400 are leap years

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("True")
            else:
                print("False")
        else:
            print("True")
    else:
        print("False")
    
is_leap_year(2001)