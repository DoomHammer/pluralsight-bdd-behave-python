@workout
Feature: Importing workouts

@fixture.load_json("example_workouts.json")
Scenario: Importing workouts
	Given we have an external data file
	When we import workouts from it
	Then we should get a list of workout objects