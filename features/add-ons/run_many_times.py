from behave import *

@when('execute many registrations at once')
def step_impl(context):
    for _ in range(0, 40):
        context.execute_steps(u'''
            Given user is on home page
            And go to the registration page
        ''')