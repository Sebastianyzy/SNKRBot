import capsule_toronto
import deadstock
import nrml
import size_ca
import nomad
import bypass_selenium_log_in


def botchrome_set_up(PATH, PROFILE_PATH):
    bypass_selenium_log_in.selenium_log_in(PATH,PROFILE_PATH)

def bot_configure(PATH, PROFILE_PATH, RETAILER, KEYWORDS, SIZE, SAFE_MODE):
    if(RETAILER == "nrml"):
        nrml.nrml_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE)
    elif(RETAILER == "deadstock"):
        deadstock.deadstock_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE)
    elif(RETAILER == "capsule_toronto"):
        capsule_toronto.capsule_toronto_main(
            PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE)
    elif(RETAILER == "size_ca"):
        size_ca.size_ca_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE)
    elif(RETAILER == "nomad"):
        nomad.nomad_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE)


