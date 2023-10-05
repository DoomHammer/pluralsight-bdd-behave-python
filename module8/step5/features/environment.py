import os
import time
from datetime import datetime
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

def before_step(context, step):
    if step.keyword != 'Given':
        time.sleep(10)

def before_scenario(context, scenario):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H-%M-%S")
    screenshots_path = os.path.join(os.path.dirname(__file__), "Screenshots")
    try:
        os.mkdir(screenshots_path)
    except:
        pass
    scenario_screenshots_path = os.path.join(screenshots_path, scenario.name)
    try:
        os.mkdir(scenario_screenshots_path)
    except:
        pass
    context.step_screenshots_path = os.path.join(scenario_screenshots_path, dt_string)
    try:
        os.mkdir(context.step_screenshots_path)
    except:
        pass

def after_step(context, step):
    try:
        step_screenshot_file_path = os.path.join(context.step_screenshots_path, f'After {step.name}.png')
        context.browser.save_screenshot(step_screenshot_file_path)
    except:
        pass