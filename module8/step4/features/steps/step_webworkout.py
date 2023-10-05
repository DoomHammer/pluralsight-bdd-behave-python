from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given('we have a browser open')
def step_impl(context):
    assert context.browser is not None


@when('we enter the website address')
def step_impl(context):
    context.browser.get('http://host.docker.internal:3000/')


@then('we should see the Carved Rock Fitness application with appropriate Call to Action')
def step_impl(context):
    h1 = context.browser.find_element(By.CSS_SELECTOR, "div.jumbotron > div > h1")
    assert h1.text.lower() == "ADD YOUR WORKOUT".lower()
