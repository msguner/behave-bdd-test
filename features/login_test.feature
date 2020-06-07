# Created by Muhammet Safa Güner at 7.06.2020

Feature: Hepsiburada login tests

  Scenario: Success test for login
    Given I navigate to login page
    And I enter username="msguner55@gmail.com" and password="12345"
    When I click on Submit button
    Then login is successful

  Scenario: Failure test for login
    Given I navigate to login page
    And I enter username="msguner55@gmail.com" and password="12345"
    When I click on Submit button
    # Then check login fails
