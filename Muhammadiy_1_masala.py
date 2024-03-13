lst = []
for i in input().split():
    lst.append(i)
if len(lst) == 0:
    print("no one likes this")
elif len(lst) == 1:
    print(f"{lst[0]} likes this")
else:
    print(f'{", ".join(lst[:-1])} and {lst[-1]} like this')