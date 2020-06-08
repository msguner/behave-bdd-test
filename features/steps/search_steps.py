from behave import step

from pages.search_page import SearchPage


@step("I see the no result page")
def step_impl(context):
    assert 'ilan bulunamadı.' in context.driver.page_source


@step('I open main category = "{category_name}" on search result page')
def step_impl(context, category_name):
    SearchPage(context).open_main_category(category_name)
