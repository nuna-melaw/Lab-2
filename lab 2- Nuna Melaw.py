#Nuna Melaw
#Techid- 14970498

# part 1
num= int(input("Enter a number form 0 to 86,399:"))
hours1= num//3600
min1= (num%3600)//60
sec1= num%60

print(hours1, min1, sec1)

# part 2
day= int(19*86400)
hours= int(12*3600)
min= int(15*60)
seconds= int(20)

total= int(day+hours+min+seconds)

birth= int(total//7)
death= int(total//13)
immigrant= int(total//35)

pop1=int(334205119)

totalb= int(pop1+birth)
totald= int(pop1-death)
totali= int(pop1+immigrant)

pop2= int(totalb+totald+totali)
print(pop2)

# part 3

sec= int(input("Enter seconds since the beginning of year:"))
days= sec//86400
hours= (sec%86400)//3600
minu= (sec%3600)//60
sec= sec%60

b= int(sec//7)
d= int(sec//13)
i= int(sec//35)

population= int(334205119)

population2= int(population+b-d+i)

print(days, "days,", hours, "hours,", minu, "minutes,", sec, "seconds after the start of 2022, the total population was", population2)

#part 4
population= int(334205119)
popf= int((((population+350)**2-12)/50))
popf2 = (popf ** 0.2)//1

print(popf2)




