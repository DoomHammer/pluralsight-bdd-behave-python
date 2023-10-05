Feature: Adding a workout
  As a user, I'd like to be able to add a Running, Jumping, or Swimming workout. All the other workout types should result in an error.

  Scenario Outline: Adding a workout
    Given we want to add a new workout
    When we set the workout type to <workout_type>
    Then we should <expected_result> an error
    Examples:
    | workout_type | expected_result  |
    | running      | not get |
    | jumping      | not get |
    | swimming     | not get |
    | parkour      | get     |