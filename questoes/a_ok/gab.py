
a = list(input())

if a.count("O")>1 or a.count("X")>2:
    print("?")
else:
    if a[1]=="X":
        print("Alice")
    elif a[1]=="O":
        print("*")