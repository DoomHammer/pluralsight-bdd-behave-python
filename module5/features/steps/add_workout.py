# Click Run icon
# See the error
# Select Scenario
# Open Context menu
# Generate steps
# Remove shit
# Fill in the steps
# Run the test again
# Add a workout class
# Run again
# See 12 passed
# Run from the command line

from workout import Workout

@given("We want to add a new workout")
def step_impl(context):
    pass


@when("We create a new Running workout")
def step_impl(context):
    workout = Workout.from_dict({'kind': "running"})


@then("We should not get an error")
def step_impl(context):
    assert True


@when("We create a new Jumping workout")
def step_impl(context):
    workout = Workout.from_dict({'kind': "jumping"})


@when("We create a new Swimming workout")
def step_impl(context):
    workout = Workout.from_dict({'kind': "swimming"})


@when("We create a new Parkour workout")
def step_impl(context):
    try:
        workout = Workout.from_dict({'kind': "parkour"})
    except ValueError:
        assert True
    else:
        assert False


@then("We should get an error")
def step_impl(context):
    pass