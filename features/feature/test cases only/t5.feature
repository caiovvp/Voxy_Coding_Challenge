Feature: Log in into the website using a non-registered email

  Background: 
    Given go to Voxy WebStage: <https://web-stage.voxy.com/v2/#/login/>

    Scenario: Email without @ sign
      When click on <voxy-radio__box>
      And type test-gmail.com: <login_form_submit_button>
      And click on <login_form_submit_button>
      Then login button is not clickable