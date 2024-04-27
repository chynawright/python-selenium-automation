# Created by ChynaWright at 4/26/2024
Feature: Create a window handling test case from the class
  # Enter feature description here

  Scenario: User can open and Close Terms and Conditions from sign in page
    Given Open main Target page
    When Click sign in
    And Click sign in on navigation menu
    And Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
