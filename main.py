from os import initgroups
from posixpath import ismount
import Bot
import time

site = ["a", "b", "c", "d", "e", "f"]

def main():
    print("\n\nrunning SNKRBot...\n")
    time.sleep(1)
    RETAILER = input(
        "choose site to run:\n(a)NRML\n(b)Deadstock\n(c)Capsule Toronto\n(d)Size? CA\n(e)CourtSide Sneakers\n(f)NOMAD\n\n or enter 'q' to exit\n\n").lower()
    if RETAILER in site:
        print("\ntransfering...\n")
        time.sleep(1)
        Bot.bot_configure(RETAILER)
    elif(RETAILER == "q"):
        print("\nshuting down...\n")
        time.sleep(0.5)
        exit()
    else:
        print("\ninvalid option!")
        time.sleep(0.5)
        print("back to main menu...\n")
        time.sleep(1)
        main()


if __name__ == '__main__':
    main()



