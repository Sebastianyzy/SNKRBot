import Bot
import nrml
import capsule_toronto
import deadstock


def main():
    print("running SNKRBot...\n")
    print("---------\nmain menu---------\n")
    RETAILER = input("choose site to run:\n(A)NRML\n(B)Deadstock\n(C)Capsul Toronto\n\n or enter 'q' to exit\n\n").lower()
    if(RETAILER == "a" or RETAILER == "b" or RETAILER == "c"):
        calendar = []
        print("transfering...\n")
        if(RETAILER == "a"):
            calendar = Bot.pull_calendar(nrml.UPCOMING_RELEASES)
        elif(RETAILER == "b"):
            calendar = Bot.pull_calendar(deadstock.UPCOMING_RELEASES)     
        elif(RETAILER == "c"):   
            calendar = Bot.pull_calendar(capsule_toronto.UPCOMING_RELEASES)       
        #link_to_run = Bot.bot_configure(calendar, RETAILER)
        
            
        

                    

            
        
    elif(RETAILER == "q"):
        exit()
    else:
        print("invalid option")
        print("back to main menu...\n")
        main()  


if __name__ == '__main__':
    main()