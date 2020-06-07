from behave import given, when, then

from pages.home_page import HomePage
from pages.login_page import LoginPage


@given(u'I navigate to login page')
def step_impl(context):
    HomePage(context).open_login_page()


@given(u'I enter username="{username}" and password="{password}"')
def step_impl(context, username, password):
    login_page = LoginPage(context)
    login_page.enter_username(username)
    login_page.enter_password(password)


@when(u'I click on Submit button')
def step_impl(context):
    LoginPage(context).click_login()


@then(u'login is successful')
def step_impl(context):
    assert context.driver.current_url != 'https://secure.sahibinden.com/giris'
    # assert 'Login successful !!' in context.browser.page_source


@then("login is unsuccessful")
def step_impl(context):
    assert context.driver.current_url == 'https://secure.sahibinden.com/giris'
