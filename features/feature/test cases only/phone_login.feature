Feature: Log in into the website using the phone number login type.

  Background: 
    Given go to Voxy Website
    And wait for the page completes loading
    When click on phone number login option
    And choose a country for the number input
    Then phone input box should display a mask for the country selected

    Scenario: Larger phone number
      When type more numbers than the mask is showing
      Then 'Continue' button should stay disabled
      And phone number input should display red 'x' sign

    Scenario: Shorter phone number
      When type less numbers than the mask is showing
      Then 'Continue' button should stay disabled
      And phone number input should display red 'x' sign

    Scenario: Invalid phone number
      When type characters other than numbers in the input box
      Then 'Continue' button should stay disabled
      And phone number input should display red 'x' sign

    Scenario: Unregistered valid phone number
      When type a valid number for the country selected
      Then 'Continue' button should become clickable
      When click on 'Continue' button
      Then show message saying the account was not found

    Scenario: Registered valid phone number
      When type a valid number for the country selected
      Then 'Continue' button should become clickable
      When click on 'Continue' button
      Then password input is shown to the user
      When user types password correctly
      And click on 'Login' button
      Then user gets redirect to home page


