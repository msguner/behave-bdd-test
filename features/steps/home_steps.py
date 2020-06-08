from behave import step


@step('I navigate to Sahibinden home page')
def step_impl(context):
    context.driver.get("https://www.sahibinden.com/")
