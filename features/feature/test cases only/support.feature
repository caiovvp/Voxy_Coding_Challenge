Feature: Send a support message to Voxy team.

  Background: 
    Given go to Voxy Website
    And wait for the page completes loading
    When click on the support button
    Then wait until support form is shown

    Scenario: Form without message
      When type a valid email address
      And click on 'Send' button
      Then display message under the description box saying to enter a value

    Scenario: Form without email
      When type a message in the description box
      And click on 'Send' button
      Then display message under the email input saying to enter a valid email

    Scenario: Form without name
      When type a valid email address
      And type a message in the description box
      Then show message saying 'Thanks for reaching out'
      When click on the 'Go back' button
      Then close support form

    Scenario: Form attachment limit
      When type a valid email address
      And type a message in the description box
      And click on the 'Attachments' button
      And upload more than 5 files to the form
      Then show a message saying 'Attachment limit reached'

    Scenario: All form inputs filled out
      When type a name in the name input
      And type a valid email address
      And type a message in the description box
      And click on the 'Attachments' button
      And upload one file to the form
      Then show message saying 'Thanks for reaching out'
      When click on the 'Go back' button
      Then close support form