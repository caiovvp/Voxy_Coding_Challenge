from behave import *

from features.context.fixtures import *

# -- go to the link indicated
@given('go to {page_name}: <{link}>')
@when('go to {page_name}: <{link}>')
def step_impl(context, page_name, link):
    context.browser.get(link)

# -- type a value in a web_element
@when('type {input}: <{value}>')
def step_impl(context, input, value):
    type(context, input, value)

# -- click on a web_element
@when('click on <{input}>')
@then('click on <{input}>')
def step_impl(context, input):
    click_on_btn(context, input)

# -- try to click on a web_element
@when('try to click on <{input}>')
@then('try to click on <{input}>')
def step_impl(context, input):
    click_on_btn(context, input)


@then('login button is not clickable')
def step_impl(context):
    login_button = find_input(context.browser, "login_form_submit_button")
    button_unclickable(context, 'voxy-button_disabled')

@then('login button is clickable')
def step_impl(context):
    login_button = find_input(context.browser, "login_form_submit_button")
    button_clickable(context, "login_form_submit_button")


@then('show message <{message}> on <{web_ele}>')
def step_impl(context, message, web_ele):
    show_message(context, message, web_ele)

@when('choose <{item_text}> from <{input}>')
def step_impl(context, item_text, input):
    choose_specific_item(context, item_text, input)

# -- clears the value of an input
@when('clear <{input_name}>')
def step_impl(context, input_name):
    find_input(context.browser, input_name).clear()

# -- clears the value of an input and type in it later
@when('clear and type <{input_name}>: <{value}>')
def step_impl(context, input_name, value):
    clear_and_type(context, input_name, value)


@when('wait for <{seconds}> seconds')
@then('wait for <{seconds}> seconds')
def step_impl(context, seconds):
    wait_for(seconds)
