year=int(input("Enterthe year"))
if(year%4==0 and year!=0 or year%400==0):
    print("leap year")
else:
    print("not a leap year")
    
cm=int(input("Enter the cm"))
feet=0.328*cm
inch=0.394*cm
print("value in feet",feet)
print("value in inch",inch)
