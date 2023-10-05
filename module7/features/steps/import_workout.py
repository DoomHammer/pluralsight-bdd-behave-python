from behave import *

from workout import Workout


@given('we have an external data file')
def step_impl(context):
    pass


@when("we import workouts from it")
def step_impl(context):
    context.workouts = []
    for workout in context.json:
        context.workouts.append(Workout.from_dict(workout))


@then("we should get a list of workout objects")
def step_impl(context):
    assert len(context.workouts) == len(context.json)