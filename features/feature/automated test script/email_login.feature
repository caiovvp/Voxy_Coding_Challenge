Feature: Try to log in into Voxy website using an invalid email, non-registered email or registered email with expired license

    @autoretry
    Scenario: Go to Voxy website
      Given go to Voxy WebStage: <https://web-stage.voxy.com/v2/#/login/>

    Scenario: Email without @ sign
      When click on <voxy-radio__box>
      And type invalid-gmail.com: <login_form_submit_button>
      And try to click on <login_form_submit_button>
      Then login button is not clickable

    Scenario: Email without extension
      When click on <voxy-radio__box>
      And clear and type <invalid@gmail>: <login_form_submit_button>
      And try to click on <login_form_submit_button>
      Then login button is not clickable
      And 

    Scenario: Email without username
      When click on <voxy-radio__box>
      And clear and type <_@gmail.com>: <login_form_submit_button>
      And try to click on <login_form_submit_button>
      Then login button is not clickable

    Scenario: Email without domain
      When click on <voxy-radio__box>
      And clear and type <invalid@.com>: <login_form_submit_button>
      And try to click on <login_form_submit_button>
      Then login button is not clickable

    Scenario: Non-registered email
      When click on <voxy-radio__box>
      And clear and type <non_registered@gmail.com>: <login_form_submit_button>
      And click on <login_form_submit_button>
      Then show message <Parece que sua conta expirou> on <login-error-message__message>
      And click on <voxy-button__text>

    Scenario: Registered email with expired license
      When click on <voxy-radio__box>
      And clear and type <test@gmail.com>: <login_form_submit_button>
      Then show message <Não foi possível encontrar sua conta desta maneira> on <login-error-message__message>
      And click on <voxy-button__text>


