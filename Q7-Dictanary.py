def all(dict):
    print('We know the birthdays of:')
    for key in dict:
        print(key)


def search(who, dict):
    if who in dict:
        return dict[who]
    else:
        return None


def main():
    Birthdays = {"Albert Einstein": "14/3/1889",
                 "Bill Gates": "28/10/1955",
                 "Steve Jobs": "24/2/1955"}
    print('Welcome to the birthday dictionary.')
    all(Birthdays)
    who = input("Who's birthday do you want to look up?")
    result = search(who,Birthdays)
    if result == None:
        print('No Data')
    else:
        print(f"{who}'s birthday is {result}")


main()
