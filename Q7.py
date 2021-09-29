templ = []


def remove_dup(x):
    s = set(x)
    for i in s:
        templ.append(i)
    print(templ)


x = input("Enter the list").split()
remove_dup(x)
