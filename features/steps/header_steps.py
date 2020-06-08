from behave import step

from pages.header_page import HeaderPage


@step(u'I navigate to login page')
def step_impl(context):
    HeaderPage(context).open_login_page()


@step('I see user name = "{name}" on home page')
def step_impl(context, name):
    assert HeaderPage(context).get_user_name() == name, "Anasayfadaki isim hatalı"


@step("I open user menu")
def step_impl(context):
    HeaderPage(context).open_user_menu()


@step("I navigate to sign up page")
def step_impl(context):
    HeaderPage(context).open_sign_up_page()


@step('I search "{text}"')
def step_impl(context, text):
    HeaderPage(context).search(text)

