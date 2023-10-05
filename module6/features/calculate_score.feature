Feature: Calculating the score

  Scenario Outline: Check if the score is correct
    Given we have a training of intensity <intensity>
    When we get the score
    Then we should receive a score of <score>
    Examples:
      | intensity | score |
      | 1         | 12    |
      | 64        | 16581 |