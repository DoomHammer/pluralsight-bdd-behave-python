from behave import given, when, then

from workoutgateway.score import do_some_work

@given('we have a training of intensity {intensity:d}')
def step_impl(context, intensity):
    context.intensity = intensity

@when('we get the score')
def step_impl(context):
    context.score = do_some_work(context.intensity)

@then('we should receive a score of {score:d}')
def step_impl(context, score):
    assert context.score == score