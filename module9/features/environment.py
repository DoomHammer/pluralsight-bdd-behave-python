import json
import os
import re
import sys
import time
from datetime import datetime
from selenium import webdriver

from behave import *

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


@fixture
def load_json(context, **kwargs):
    abs_filename = os.path.join(os.path.dirname(__file__), kwargs["json"])
    json_file = open(abs_filename)
    context.json = json.load(json_file)
    yield context.json
    json_file.close()

@fixture
def prepare_browser(context, **kwargs):
    options = webdriver.FirefoxOptions()
    context.browser = webdriver.Remote(command_executor='http://host.docker.internal:4444/wd/hub', options=options)
    context.browser.maximize_window()
    yield context.browser
    context.browser.quit()


def before_tag(context, tag):
    if tag.startswith("fixture.load_json"):
        filename = re.match(r'.*\("(.*)"\)', tag).group(1)
        use_fixture(load_json, context, json=filename)
    if tag.startswith("browser"):
        use_fixture(prepare_browser, context)

def before_step(context, step):
    for tag in context.tags:
        if tag.startswith("browser"):
            if step.keyword != 'Given':
                time.sleep(10)
                break

def before_scenario(context, scenario):
    for tag in context.tags:
        if tag.startswith("browser"):
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
            break

def after_step(context, step):
    for tag in context.tags:
        if tag.startswith("browser"):
            try:
                step_screenshot_file_path = os.path.join(context.step_screenshots_path, f'After {step.name}.png')
                context.browser.save_screenshot(step_screenshot_file_path)
            except:
                pass
            break
