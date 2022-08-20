import capsule_toronto
import nrml
import nomad
import bypass_selenium_log_in
import jdsports


def chrome_set_up(PATH, PROFILE_PATH):
    bypass_selenium_log_in.selenium_log_in(PATH, PROFILE_PATH)


def bot_configure(RETAILER):
    if(RETAILER == "nrml"):
        nrml.nrml_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE)
    elif(RETAILER == "capsule_toronto"):
        capsule_toronto.capsule_toronto_main(
            PATH, PROFILE_PATH, KEYWORDS, SIZE)
    elif(RETAILER == "nomad"):
        nomad.nomad_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE)
    elif(RETAILER == "jdsport"):
        jdsports.jd_sports_main(
            PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE, SAFE_MODE_STYLE_CODE)


PATH = ""
PROFILE_PATH = ""
RETAILER = ""
SHOP_PAY_LOG_IN = ""
KEYWORDS = ""
SIZE = ""
SAFE_MODE = ""
SAFE_MODE_STYLE_CODE = ""
bot_configure(RETAILER)
