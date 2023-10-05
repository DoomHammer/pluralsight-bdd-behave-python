from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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


@step("we select the {workout_type} workout")
def step_impl(context, workout_type):
    workout_selector = Select(context.browser.find_element(By.CSS_SELECTOR, "div.form-group > select"))
    workout_selector.select_by_visible_text(workout_type)


@step("we set the parameters")
def step_impl(context):
    pass


@step("start time to {value}")
def step_impl(context, value):
    input = context.browser.find_element(By.CSS_SELECTOR, "div.form-group > input:nth-of-type(1)")
    input.send_keys(value)


@step("end time to {value}")
def step_impl(context, value):
    input = context.browser.find_element(By.CSS_SELECTOR, "div.form-group > input:nth-of-type(2)")
    input.send_keys(value)


@step("intensity to {value}")
def step_impl(context, value):
    input = context.browser.find_element(By.CSS_SELECTOR, "div.form-group > input:nth-of-type(3)")
    input.send_keys(value)


@step("we click submit")
def step_impl(context):
    submit = context.browser.find_element(By.CSS_SELECTOR, "div.form-group > button")
    submit.click()


@then("we should get a confirmation")
def step_impl(context):
    msg = context.browser.find_element(By.CSS_SELECTOR, "div.msg")
    assert context.text.lower() in msg.text.lower() , f"actual text <{msg.text}> doesn't contain expected text <{context.text}>"