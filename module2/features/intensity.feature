Feature: Calculating workout score

Scenario: Check if a score is fine
    Given we have a training of intensity 64
    When we get the score
    Then we should receive a score of 16581
