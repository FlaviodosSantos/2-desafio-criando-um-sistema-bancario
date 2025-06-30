# Segunda versão do projeto "Criando um Sistema Bancário com Python"

Projeto desenvolvido para o desafio do bootcamp Santander 2025 - backend com python

## Objetivo Geral

- Separar as funções existentes de saque, depósito e extrato em funções.
- Criar duas novas funções:
- Cadastrar usuário (cliente)
- Cadastrar conta bancária (vincular com usuário)

 Separação em funções

## Função Saque

- Deve receber os argumentos apenas por nome (keyword only)
- Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
- Sugestão de retorno: saldo e extrato

## Depósito

- Deve receber os argumentos apenas por posição (positional only)
- Sugestão de argumentos: saldo, valor, extrato
- Sugestão de retorno: saldo e extrato

## Extrato

- Deve receber os argumentos por posição e nome (positional only e keyword only)
- Argumentos posicionais: saldo
- Argumentos nomeados: extrato

## Criar usuário (cliente)

- Deve armazenar os usuários em uma lista
- Um usuário é composto de:
- nome
- data de nascimento
- cpf:
- deve ser cadastrado apenas numeros do cpf
- Não podemos cadastrar dois usuários com o mesmo cpf
- endereço: é uma string com formato logradouro, nro - bairro - cidade/estado

## Criar conta corrente

- Deve armazenar contas em uma lista
- Uma conta é composto de:
- agência
- É um número fixo "0001"
- número da conta
- Deve ser sequencial, iniciando em 1
- usuário
- Um usuário pode ter mais de uma conta, mas uma conta não pode ter mais do que um usuário

## Dica

 Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
