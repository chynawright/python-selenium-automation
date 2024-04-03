# Created by ChynaWright at 4/3/2024
Feature: Verify Target cart is empty

  Scenario: "Your cart is empty" message
    Given Open main Target page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown