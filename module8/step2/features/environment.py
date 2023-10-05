from selenium import webdriver

from behave import *
@fixture
def prepare_browser(context, **kwargs):
    options = webdriver.FirefoxOptions()
    context.browser = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
    context.browser.maximize_window()
    yield context.browser
    context.browser.quit()

def before_tag(context, tag):
    if tag.startswith("browser"):
        use_fixture(prepare_browser, context)