UPCOMING_RELEASES = "https://www.deadstock.ca/blogs/coming-soon"
EARLY_LINK = "https://www.deadstock.ca/products/"
RELEASE_TITLE = "blog_release_title"



def deadstock_pull_calendar(driver, link, calendar):
    driver.get(link)
    release_blog = driver.find_elements_by_class_name(RELEASE_TITLE)
    for shoes in release_blog:
        calendar.append(shoes.text)
    return calendar