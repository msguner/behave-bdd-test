from behave import given, when, then, step

from pages.login_page import LoginPage


@step(u'I enter username="{username}" and password="{password}"')
def step_impl(context, username, password):
    login_page = LoginPage(context)
    login_page.enter_username(username)
    login_page.enter_password(password)


@step(u'I click on Submit button')
def step_impl(context):
    LoginPage(context).click_login()


@step("login is unsuccessful")
def step_impl(context):
    assert context.driver.current_url == 'https://secure.sahibinden.com/giris'
