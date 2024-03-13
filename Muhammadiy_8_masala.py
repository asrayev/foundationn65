ot = input("Ot     -> ")
pe = input("Peshka -> ")
if len(ot) != 2 or (ot[1] < 'A' or ot[1] > 'H') or (ot[0] < '1' or ot[0] > '8'):
    print("ERROR")
elif len(pe) != 2 or (pe[1] < 'A' or pe[1] > 'H') or (pe[0] < '1' or pe[0] > '8'):
    print("ERROR")
elif (ord(ot[0]) - ord(pe[0]) == 2 or ord(pe[0]) - ord(ot[0]) == 2) and (ord(ot[1]) - ord(pe[1]) == 1 or ord(pe[1]) - ord(ot[1]) == 1):
    print("YES")
elif (ord(ot[0]) - ord(pe[0]) == 1 or ord(pe[0]) - ord(ot[0]) == 1) and (ord(ot[1]) - ord(pe[1]) == 2 or ord(pe[1]) - ord(ot[1]) == 2):
    print("YES")
else:
    print("NO")