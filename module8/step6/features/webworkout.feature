@browser
Feature: Opening a Webapp

  Background:
    Given we have a browser open
    When we enter the website address

  Scenario: Load a Webpage
    Then we should see the Carved Rock Fitness application with appropriate Call to Action

  Scenario: Submit data
    When we select the swimming workout
    And we set the parameters
    * start time to 1200
    * end time to 1315
    * intensity to 1
    And we click submit
    Then we should get a confirmation
      """
      You've scored 12 on workout
      """