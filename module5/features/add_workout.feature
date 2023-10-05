Feature: Adding a new workout

Scenario: Adding a new running workout
	Given We want to add a new workout
	When We create a new Running workout
	Then We should not get an error

Scenario: Adding a new jumping workout
	Given We want to add a new workout
	When We create a new Jumping workout
	Then We should not get an error

Scenario: Adding a new swimming workout
	Given We want to add a new workout
	When We create a new Swimming workout
	Then We should not get an error

Scenario: Adding a non-existing workout
	Given We want to add a new workout
	When We create a new Parkour workout
	Then We should get an error
