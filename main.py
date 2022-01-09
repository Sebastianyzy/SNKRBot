import Bot

site = ["a", "b", "c", "d"]


def main():
    print("running SNKRBot...\n")
    RETAILER = input(
        "choose site to run:\n(a)NRML\n(b)Deadstock\n(c)Capsule Toronto\n(d)size? CA\n\n or enter 'q' to exit\n\n").lower()
    if RETAILER in site:
        print("transfering...\n")
        Bot.bot_configure(RETAILER)
    elif(RETAILER == "q"):
        exit()
    else:
        print("invalid option")
        print("back to main menu...\n")
        main()


if __name__ == '__main__':
    main()
