from behave import given, when, then
from app import app, disciplinas
import json

@given('que os dados da disciplina são válidos')
def step_impl(context):
    context.dados = {
        "titulo": "Projeto de Software",
        "data_inicio": "2026-02-01",
        "data_termino": "2026-06-30",
        "vagas": 40,
        "eh_verao": False
    }
    context.cliente = app.test_client()

@when('eu solicitar o salvamento')
def step_impl(context):
    context.resposta = context.cliente.post('/disciplinas', 
                                            data=json.dumps(context.dados),
                                            content_type='application/json')

@then('a disciplina deve estar na lista do sistema')
def step_impl(context):
    assert context.resposta.status_code == 201
    assert len(disciplinas) > 0