@browser
Feature: Opening a Webapp

  Scenario: Load a Webpage
    Given we have a browser open
    When we enter the website address
    Then we should see the Carved Rock Fitness application with appropriate Call to Action