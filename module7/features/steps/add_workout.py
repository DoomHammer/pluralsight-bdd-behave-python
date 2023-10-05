from behave import *

from workout import Workout


@given("we want to add a new workout")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("we set the workout type to {workout_type}")
def step_impl(context, workout_type):
    """
    :type context: behave.runner.Context
    """
    context.workout = None
    context.exception = None
    try:
        context.workout = Workout.from_dict({'kind': workout_type})
    except Exception as e:
        context.exception = e


@then("we should {expected_result} an error")
def step_impl(context, expected_result):
    """
    :type context: behave.runner.Context
    """
    if expected_result == "not get":
        assert context.workout is not None
        assert context.exception is None
    else:
        assert context.workout is None
        assert context.exception is not None