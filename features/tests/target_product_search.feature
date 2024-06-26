# Created by ChynaWright at 4/2/2024
Feature: Search Tests


  Scenario Outline: User can search for a product
    Given Open main Target page
    When Search for '<item>'
    Then Verify search results are shown for <expected_item>
    Examples:
    |item |expected_item  |
    |mug  |mug            |
    |tea  |tea            |
    |spoon|spoon          |




