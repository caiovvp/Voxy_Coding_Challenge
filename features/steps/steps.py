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

@given('click on <{input}>')
@when('click on <{input}>')
@then('click on <{input}>')
def step_impl(context, input):
    click_on_btn(context, input)

@then('show message <{message}> on <{web_ele}>')
def step_impl(context, message, web_ele):
    show_message(context, message, web_ele)

@when('choose <{item_text}> from <{input}>')
def step_impl(context, item_text, input):
    choose_specific_item(context, item_text, input)

# -- verifies if a specific window of the browser is goes to the link indicated
@then('redirect to {page_name}: <{link}> on window <{window_handle_number}>')
def step_impl(context, page_name, link, window_handle_number):
    redirect_to_link(context, page_name, link, window_handle_number)

# -- find a web_element that is a {input_type} with {input_name} and has {text} in another web_element
@when('find <{text}> [type: <{input_type}>, name: <{input_name}>] in <{web_ele}>')
def step_impl(context, text, input_type, input_name, web_ele):
    web_ele = find_input(context.browser, web_ele)
    if input_type == 'tag':
        item_list = web_ele.find_elements_by_tag_name(input_name)
    if input_type == 'class':
        item_list = web_ele.find_elements_by_class_name(input_name)
    for item in item_list:
        if 'btn' in input_name:
            item.click()
            break
        else:
            if item.text == text:
                find_input(item, 'a').click()
                break

# -- find a web_element that is a {input_type} with {input_name} and has {text} in another web_element that has "trs"
@when('find <{text}> [type: <{input_type}>, name: <{input_name}>] in <{web_ele}> (FOR LISTS)')
def step_impl(context, text, input_type, input_name, web_ele):
    web_ele = find_input(context.browser, web_ele)
    trs_list = web_ele.find_elements_by_tag_name('tr')
    for tr in trs_list:
        if text in tr.text:
            correct_tr = tr
    if input_type == 'tag':
        item_list = web_ele.find_elements_by_tag_name(input_name)
    if input_type == 'class':
        item_list = correct_tr.find_elements_by_class_name(input_name)
    for item in item_list:
        if 'btn' in input_name:
            item.click()
            break
        else:
            if item.text == text:
                find_input(item, 'a').click()
                break
            if len(context.browser.window_handles) < 2:
                raise NoSuchElementException

# -- close the current window of a browser and switches to the window beside it
@then('close browser window <{number}>')
def step_impl(context, number):
    close_window(context, number)

# -- clears the value of an input
@when('clear <{input_name}>')
def clear_input(context, input_name):
    find_input(context.browser, input_name).clear()

# -- clears the value of an input and type in it later
@when('clear and type <{input_name}>: <{value}>')
def step_impl(context, input_name, value):
    clear_and_type(context, input_name, value)

# -- set the value of a web_element directly on HTML
@when('set <{input_id}> value to <{value}>')
def step_impl(context, input_id, value):
    context.browser.execute_script(f"document.getElementById('{input_id}').value = '{value}';")

@then('find <{web_ele}> on page')
def step_impl(context, web_ele):
    find_input(context.browser, web_ele)

@then('show a list of researches created so far')
def show_dashboard_list(context):
    context.execute_steps(u'''
        When find <Pesquisa Teste> [type: <tag_name>, name: <tr>] in <table> (FOR LISTS)
    ''')

@then('find <{text}> in <{web_ele}>')
def step_impl(context, text, web_ele):
    element = find_input(context.browser, web_ele)
    assert text in element.text

@then('dont find <{text}> in <{web_ele}>')
def step_impl(context, text, web_ele):
    element = find_input(context.browser, web_ele)
    assert text not in element.text

@given('check researches and delete them')
def step_impl(context):
    tbody = context.find_input(context.browser, 'tbody')
    trs = tbody.find_elements_by_tag_name(context.browser, 'tr')
    for tr in trs:
        tr.find_element_by_id('excluir-btn').click()

@when('wait for <{seconds}> seconds')
@then('wait for <{seconds}> seconds')
def step_impl(context, seconds):
    wait_for(seconds)

@when('change <{input}> attribute <{attr_name}> to <{attr_value}>')
def step_impl(context, input, attr_name, attr_value):
    change_attr(context, input, attr_name, attr_value)
