import time

from robot.api.deco import keyword

import webtestlib
from webtestlib import driver as webapp


@keyword("OPEN BROWSER")
def open_browser():
    """
    :goal: Opens the browser at the address
    :return: None
    """
    webapp.get("http://automationpractice.com/index.php")
    time.sleep(5)


@keyword("CLOSE BROWSER")
def close_browser():
    """
    :goal: Closes the browser
    :return: None
    """
    webapp.close()


@keyword("SIGN IN")
def sign_in():
    """
    :goal: Clicks on sign in button, enters email address and clicks on submit
    :return: None
    """
    # Click Sign in
    webtestlib.click_button("header_user_info")
    # Enter Email
    webtestlib.write_to_text_box("email_create", "alexas@dks.com")
    # Click Submit
    webtestlib.submit("SubmitCreate")


@keyword("CREATE ACCOUNT")
def create_account():
    """
    :goal: Enters all necessary details on the Sign In page
    :return: None
    """
    time.sleep(2)
    webtestlib.click_radio_button("id_gender2")

    # Create lists with all the textboxes and the information to be entered
    textboxes = ["customer_firstname", "customer_lastname", "passwd", "company", "address1", "city",
                 "postcode", "phone_mobile"]
    text_to_enter = ["Alexa", "Smith", "dksgd765", "Government", "5th Avenue, no. 3423", "New York",
                     "55012", "87354725"]
    # Add the text to the boxes
    for index in range(len(textboxes)):
        webtestlib.write_to_text_box(textboxes[index], text_to_enter[index])

    drop_boxes = ["days", "months", "years", "id_state"]
    value_drop_box = ["1", "8", "1990", "21"]

    for index in range(len(drop_boxes)):
        webtestlib.drop_box_navigate(drop_boxes[index], value_drop_box[index])

    webtestlib.submit("newsletter")
    webtestlib.submit("submitAccount")


@keyword("CHECK ADDRESS")
def check_address():
    """
    :goal: Enters the My Addresses page and verifies the information
    :return: None
    """
    webtestlib.click_span("//span[text()='My addresses']")
    read_address = webtestlib.get_div_table_text('//*[@id="center_column"]/div[1]/div/div')

    address_to_check = ["5th Avenue, no. 3423", "New York, Massachusetts 55012", "United States"]

    for item in address_to_check:
        if item not in read_address:
            raise Exception(f"The addresses were not successfully confirmed!"
                            f"Missing {item} in {read_address}")

@keyword("SIGN OUT")
def sign_out():
    """
    :goal: Clicks on Sign Out button
    :return: None
    """
    webtestlib.click_button("logout")
    time.sleep(5)

