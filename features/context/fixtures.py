import datetime
import random
import time
from json import loads

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# -- function that instances that the browser is chrome and that it quits once the test is over
def browser_firefox(context):
    # -- set test suite to run on local machine firefox (PLACE THE PATH OF YOUR GECKODRIVER.EXE DOWN BELOW)
    context.browser = Firefox(executable_path='C:\Users\caio_\Selenium Webdriver\geckodriver.exe')

    yield context.browser
    context.browser.quit()


# -- function to timeout the test, if necessary
def timeout_for_page_load(context):
    context.browser.set_page_load_timeout(5)


# -- Note: change False for True if you want ipdb debugger running when an error happens
BEHAVE_DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


# -- returns a web element that contains the href "link" in its properties
def find_by_href(context, link):
    anchors_list = context.browser.find_elements_by_tag_name('a')
    for element in anchors_list:
        if link in element.get_attribute('href'):
            return element


# -- type a single value in an input
def type(context, input, value):
    find_input(context.browser, input).send_keys(value)


# -- save the input value and clear it later
def save_and_clear(input):
    input_value = input.get_attribute('value')
    input.clear()
    return input_value


# -- find an input on the page and clear it
def clear_input(context, input):
    web_ele = find_input(context.browser, input)
    web_ele.clear()
    return web_ele


# -- clears the value of an input and type in it later
def clear_and_type(context, input_name, value):
    web_ele = find_input(context.browser, input_name)
    web_ele.clear()
    web_ele.send_keys(value)


# -- find input by xpath, id, name, class name, tag name
def find_input(general_context, input):
    try:
        web_ele = general_context.find_element_by_xpath(input)
        return web_ele
    except NoSuchElementException:
        try:
            web_ele = general_context.find_element_by_id(input)
            return web_ele
        except NoSuchElementException:
            try:
                web_ele = general_context.find_element_by_class_name(input)
                return web_ele
            except NoSuchElementException:
                try:
                    web_ele = general_context.find_element_by_name(input)
                    return web_ele
                except NoSuchElementException:
                    try:
                        web_ele = general_context.find_element_by_tag_name(input)
                        return web_ele
                    except NoSuchElementException:
                        anchors_list = general_context.find_elements_by_tag_name('a')
                        for web_ele in anchors_list:
                            if input in web_ele.get_attribute('href'):
                                return web_ele
                            else:
                                raise NoSuchElementException


# -- confirms if message box is shown and assert the message is right
def show_message(context, message, input):
    WebDriverWait(context.browser, 8).until(EC.text_to_be_present_in_element((By.CLASS_NAME, input), message))
    web_ele = find_input(context.browser, input)
    assert message in web_ele.text


# -- close the current window of a browser and switches to the window beside it
def close_window(context, number):
    context.browser.close()
    context.browser.switch_to_window(context.browser.window_handles[(len(number) - 2)])


# -- click on a generic web_element with 'input' as the name to locate it
def click_on_btn(context, input):
    try:
        context.browser.find_element_by_xpath(input).click()
    except NoSuchElementException:
        try:
            context.browser.find_element_by_id(input).click()
        except NoSuchElementException:
            try:
                context.browser.find_element_by_class_name(input).click()
            except NoSuchElementException:
                try:
                    link_button = find_by_href(context, input)
                    if link_button is not None:
                        link_button.click()
                except NoSuchElementException as e:
                    raise e


# -- select a specific option of a select list
def choose_specific_item(context, item_text, input):
    list_ele = find_input(context.browser, input)
    list_options = list_ele.find_elements_by_tag_name('option')
    for item in list_options:
        if item.text == item_text:
            item.click()
            break


# -- verifies if a specific window of the browser goes to the link indicated
def redirect_to_link(context, page_name, link, window_handle_number):
    window = context.browser.window_handles[int(window_handle_number) - 1]
    context.browser.switch_to_window(window)
    assert link in context.browser.current_url


# -- stops the execution thread for "x" amount of seconds
def wait_for(seconds):
    time.sleep(float(seconds))


# -- change the attribute of a web_ele
def change_attr(context, input, attr_name, attr_value):
    web_ele = find_input(context.browser, input)
    context.browser.execute_script("""arguments[0].setAttribute({}, {})""".format(attr_name, attr_value), web_ele)


def button_unclickable(context, input):
    try:
        time.sleep(0.5)
        context.browser.find_element_by_class_name(input)
    except NoSuchElementException as e:
        raise e


def button_clickable(context, input):
    try:
        time.sleep(0.5)
        context.browser.find_element_by_id(input)
    except NoSuchElementException as e:
        raise e
