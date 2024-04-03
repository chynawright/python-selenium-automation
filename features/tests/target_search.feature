# Created by ChynaWright at 4/2/2024
Feature: Search Tests

  Scenario: User can search for product
    Given Open Target main page
    When Search for 'coffee'
    Then Verify search results are shown