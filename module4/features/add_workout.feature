Feature: Adding a workout
  As a user, I'd like to be able to add a Running, Jumping, or Swimming workout. All the other workout types should result in an error.

  Scenario: Adding a running workout
    Given we want to add a new workout
    When we set the workout type to running
    Then we should not get an error

  Scenario: Adding a jumping workout
    Given we want to add a new workout
    When we set the workout type to jumping
    Then we should not get an error

  Scenario: Adding a swimming workout
    Given we want to add a new workout
    When we set the workout type to swimming
    Then we should not get an error

  Scenario: Adding a non-existing workout
    Given we want to add a new workout
    When we set the workout type to parkour
    Then we should get an error