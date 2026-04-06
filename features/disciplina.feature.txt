# language: pt

Funcionalidade: Gerenciar Disciplinas

  Cenário: Cadastro de disciplina com sucesso
    Dado que os dados da disciplina são válidos
    Quando eu solicitar o salvamento
    Então a disciplina deve estar na lista do sistema