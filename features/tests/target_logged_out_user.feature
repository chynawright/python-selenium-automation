# Created by ChynaWright at 4/3/2024
Feature: Logged out user can navigate to Sign In
  # Enter feature description here

  Scenario: Logged out user can sign in
    Given Open Target page
    When Click sign in
    And Click sign in on navigation menu
    Then Verify sign in form is opened