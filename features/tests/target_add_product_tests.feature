# Created by ChynaWright at 4/10/2024
Feature: Add product to Target cart and verify


  Scenario Outline: Add to Target Cart
    Given Open main Target page
    When Search for '<item>'
    Then Verify search results are shown for <expected_item>
    And Add item to cart
    And Add item to cart in side view
    And View cart and checkout
    And Assert '<verified_item>' in cart
Examples:
    |item|expected_item|verified_item|
    |Tillamook Shredded Cheese|Tillamook Shredded Cheese|Tillamook|













