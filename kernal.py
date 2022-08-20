import capsule_toronto
import nrml
import nomad
import bypass_selenium_log_in


def chrome_set_up(PATH, PROFILE_PATH):
    bypass_selenium_log_in.selenium_log_in(PATH,PROFILE_PATH)

def bot_configure(PATH, PROFILE_PATH, RETAILER, KEYWORDS, SIZE, SAFE_MODE):
    if(RETAILER == "nrml"):
        nrml.nrml_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE)
    elif(RETAILER == "capsule_toronto"):
        capsule_toronto.capsule_toronto_main(
            PATH, PROFILE_PATH, KEYWORDS, SIZE)
    elif(RETAILER == "nomad"):
        nomad.nomad_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE)


PATH = ""
PROFILE_PATH = ""
RETAILER = ""
KEYWORDS = ""
SIZE = ""
SAFE_MODE = ""