UPCOMING_RELEASES = "https://nrml.ca/blogs/release-calendar"
EARLY_LINK = "https://nrml.ca/products/"
RELEASE_TITLE ="font-heading"




def nrml_bot_configure(calendar, shoes):    
    return 


def nrml_generate_early_link(s, site):
    return 


def nrml_pull_calendar(driver, link, calendar):   
    driver.get(link)
    release_blog = driver.find_elements_by_class_name(RELEASE_TITLE)
    for shoes in release_blog:
        calendar.append(shoes.text)
    return calendar
