import Bot
import time

site = ["a", "b", "c", "d"]


def main():
    print("\n\nrunning SNKRBot...\n")
    time.sleep(3)
    RETAILER = input(
        "choose site to run:\n(a)NRML\n(b)Deadstock\n(c)Capsule Toronto\n(d)Size? CA\n\n or enter 'q' to exit\n\n").lower()
    if RETAILER in site:
        print("\ntransfering...\n")
        time.sleep(3)
        Bot.bot_configure(RETAILER)
    elif(RETAILER == "q"):
        print("\nshuting down...\n")
        time.sleep(3)
        exit()
    else:
        print("\ninvalid option!")
        time.sleep(1)
        print("back to main menu...\n")
        time.sleep(3)
        main()


if __name__ == '__main__':
    main()
