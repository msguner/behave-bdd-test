from behave import step

from pages.sign_up_page import SignUpPage


@step("I see the registration page open")
def step_impl(context):
    assert SignUpPage(context).is_initialize() == True, "Kayıt ol sayfası görüntülenemedi"
