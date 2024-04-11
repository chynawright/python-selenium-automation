# Created by ChynaWright at 4/2/2024
Feature: Search Tests


  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for '<item>'
    Then Verify search results are shown for <expected_item>git
    Examples:
    |item |expected_item  |
    |mug  |mug            |
    |tea  |tea            |
    |spoon|spoon          |


