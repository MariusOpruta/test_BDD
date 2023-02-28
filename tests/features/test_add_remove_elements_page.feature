Feature: Test Add Remove Elements functionality

    Scenario: Check add button works
      Given open login page
      When the user click AddButton 10 times
      When the user click Delete Button
      Then Not all delete button is displayed
      Then title message is displayed