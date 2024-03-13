def My_sort(lst: list=[5, 31, 123, 80, 11]):
    lst.sort(key=lambda x: eval("+".join(str(x))))
    print(lst)

lst = []
for i in input().split():
    lst.append(int(i))
# lst = [14, 30, 103]
# lst = [5, 31, 123, 80, 11]
My_sort(lst)