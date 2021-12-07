def action():
    print("you encounter a monster while searching the files soon after you run torwards an office")
    answer = input("after locking the door you hear the monster trying to break it down looking around you (search dead security guard,stand your ground, hide in closet)")
    if answer.lower().strip() == "hide in closet":
        print("after breaking down the door the monster looks for you but leaves in anger due to not being able to find you")
    elif answer.lower().strip() == "search dead security guard":
        print("finding a gun on the dead body you are able to shoot the monster after he breaks in stunning him allowing you to escape")
    elif answer.lower().strip() == "stand your ground":
        print("after the monster broke in you swung your fist at it missing and being killed, restart to try again")
        action()
    print("chapter 3 ends")
action()

import chapter4rework