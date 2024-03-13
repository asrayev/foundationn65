x = int(input("--->"))
print(("Tub") if len([i for i in range(1,x+1) if x%i==0])==2 else ("Tub emas"))