def line():
    print()

def title(num : int):
    print("-=" * num, end="")
    print("TERMO", end="")
    print("-=" * num)

def underlines(lista):
    for item in lista:
        print(item, end=" ")
