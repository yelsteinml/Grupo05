a=float(input("ingrese nota: "))
b=float(input("ingrese nota: "))
c=float(input("ingrese nota: "))

x=(a+b+c)/3

print x

if(x<=20 and x>16 ):
    print "alumno muy bueno"
else:
    if(x<=16 and x>=14):
        print "alumno bueno"
    else:
        if(x<=13 and x>=11):
         print "alumno regular "
        else:
         print "alumno malo"
            