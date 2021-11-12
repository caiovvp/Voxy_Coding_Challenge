from behave import *
from selenium.common.exceptions import NoSuchElementException

from features.context.fixtures import find_input

@given('user is logged in <{application_name}> on <{business}>')
def login_admin_panel(context, application_name, business):
    try:
        context.execute_steps(u'''
            Given go to Dashboard Page: <http://192.168.201.15:86/empresas>
        ''')
        find_input(context.browser, '/dashboard')
    except NoSuchElementException:
        # Log in using default/admin user in the application
        context.execute_steps(u'''
            When choose <{}> from <empresa_id>
            And type login: <joaovitor>
            And type senha: <senhas@123>
            And click on <entrar-button>
            And wait for <0.5> seconds
        '''.format(business))

@when('fill new business form')
def fill_business_form(context):
    context.execute_steps(u'''
        When type cadastrar-nome: <Empresa Nova>
        And type cadastrar-cnpj: <19115687000139>
        And type cadastrar-telefone: <65982254687>
        And type cadastrar-email: <emaildeteste@gmail.com>
        And type cadastrar-contato: <Tester>
        And choose <Ativo> from <inserir-status>
    ''')

@then('create a test business')
def create_business(context):
    context.execute_steps(u'''
        When click on <cadastrar-btn>
        And type cadastrar-nome: <Empresa Teste>
        And type cadastrar-cnpj: <69593190000102>
        And type cadastrar-telefone: <65111111111>
        And type cadastrar-email: <email_teste@gmail.com>
        And type cadastrar-contato: <Tester>
        And choose <Ativo> from <inserir-status>
        And click on <cadastrar-button>
        Then show message
        """
          {
            "message": "Empresa cadastrada com sucesso",
            "web_ele": "toast-message"
          }
        """
        And wait for <0.5> seconds
    ''')

@then('create a test branch')
def create_branch(context):
    context.execute_steps(u'''
        When click on <cadastrar-btn>
        And choose <Empresa Teste> from <cadastrar-empresa>
        And type cadastrar-nome: <Filial Teste>
        And click on <cadastrar-button>
        Then show message
        """
            {
              "message": "Unidade cadastrada com sucesso",
              "web_ele": "toast-message"
            }
        """
        And wait for <0.5> seconds
    ''')

@when('create a test research')
def create_research(context):
    context.execute_steps(u'''
        When click on <cadastrar-btn>
        And type cadastrar-titulo: <Pesquisa Teste>
        And type cadastrar-subtitulo: <testando>
        And choose <Geral> from <cadastrar-tipo>
        And choose <Ativo> from <cadastrar-ativo>
        And click on <cadastrar-dh-inicial>
        And type cadastrar-dh-inicial: <10>
        And type cadastrar-dh-inicial: <10>
        And type cadastrar-dh-inicial: <2045>
        And click on <cadastrar-dh-final>
        And type cadastrar-dh-final: <10102048>
        And click on <cadastrar-button>
    ''')