Feature: Log in into the website using an activation code.

  Background: 
    Given go to Voxy Website login page
    And wait for the page completes loading
    When click on the 'I have a code' button
    Then redirect to 'activate your account' page

    Scenario: Larger code
      When user tries to copy and paste a larger than 16 characters code
      Then code box should only accept the first 16 first characters
      And add the preset mask to the code

    Scenario: Shorter code
      When type a code shorter than 16 characters
      Then the preset mask should be applied
      But 'Continue' button should stay disabled

    Scenario: Invalid code
      When type a 16-characters-long invalid activation code
      Then 'Continue' button should become enabled
      When click on 'Continue' button
      Then a form should be opened to the user
      When user fills out all the required inputs with valid information
      Then show message saying the code entered isn't working

    Scenario: Valid code
      When type a 16-characters-long invalid activation code
      Then 'Continue' button should become enabled
      When click on 'Continue' button
      Then a form should be opened to the user
      When user fills out all the required inputs with valid information
      Then show message saying the code has been successfully redeemed
      And user account gets created

    Scenario: Login with created account
      When type a 16-characters-long invalid activation code
      Then 'Continue' button should become enabled
      When click on 'Continue' button
      Then a form should be opened to the user
      When user fills out all the required inputs with valid information
      Then show message saying the code has been successfully redeemed
      And user account gets created
      When user goes back to login page
      And user types the email which was put on the create account form
      And click on 'Continue' button
      Then password input box should appear
      When user types password correctly
      And click on 'Login' button
      Then user gets redirect to home page




