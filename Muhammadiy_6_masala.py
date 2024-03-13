lst = []
for i in range(10):
    n = input('>>> ')
    if n != '-':
        lst.extend(n.split(','))
# lst = ['1', '4', '3', '2', '1', '10', '2', '3', '6', '4', '5', '6', '0', '0', '0', '4', '6', '5', '2']
for i in range(10, -1, -1):
    n = lst.count(str(i))
    if n == 0:
        print("-")
    else:
        print(",".join([str(i)]*n))