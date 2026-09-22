import random

subjects = [
    "Imran Khan",
    "Asim Munir",
    "A Dacoit From Karachi",
    "CM Maryam Nawaz",
    "Nawaz Sharif",
    "A Lahori",
    "Pindi Boys",
    "Kashmiri People",
]

actions = [
    "Launches",
    "Dances",
    "Eats Samosa",
    "Declares War",
    "Wants Awam Relief",
    "Commits Theft",
    "Makes a Reel",
    "Slips",
]

places = [
    "Geo",
    "Pakistan",
    "in Ravi River",
    "on Social Media",
    "at Muridke",
    "in the Corner",
    "from Islamabad",
    "at a Football Match",
]

while True:
    user_want = input("Do you want to enter a name? (y/n): ").lower().strip()

    if user_want == "y":
        your_name = input("Enter a name: ").strip()
        subject = your_name
    else:
        subject = random.choice(subjects)

    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want to make another? (y/n): ").lower().strip()

    if user_input == "n":
        print("\nThanks for making fake news!")
        break