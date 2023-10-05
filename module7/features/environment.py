import json
import os
import re

from behave import *

@fixture
def load_json(context, **kwargs):
    abs_filename = os.path.join(os.path.dirname(__file__), kwargs["json"])
    json_file = open(abs_filename)
    context.json = json.load(json_file)
    yield context.json
    json_file.close()

def before_tag(context, tag):
    if tag.startswith("fixture.load_json"):
        filename = re.match(r'.*\("(.*)"\)', tag).group(1)
        use_fixture(load_json, context, json=filename)