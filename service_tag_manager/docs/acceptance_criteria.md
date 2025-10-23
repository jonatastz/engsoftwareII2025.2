# Critérios de Aceitação e Plano de Testes (Service Tag Manager)

## Visão Geral
O sistema **Service Tag Manager** deve permitir gerenciar tags de serviço, cadastro, edição, busca e exportação.

## Critérios de Aceitação (formato BDD)
- **Cadastrar tag com dados válidos**
  - Dado que o usuário preenche os campos obrigatórios,
  - Quando ele confirmar o cadastro,
  - Então a tag é salva e aparece na lista com um ID único.

- **Editar tag existente**
  - Dado que exista uma tag cadastrada,
  - Quando o usuário alterar e salvar,
  - Então as mudanças são persistidas.

- **Remover tag**
  - Dado que exista uma tag cadastrada,
  - Quando o usuário pedir remoção e confirmar,
  - Então a tag não aparece mais na lista.

- **Busca por filtros**
  - Dado que várias tags existem,
  - Quando o usuário aplicar filtros (nome, status),
  - Então a lista exibe apenas registros que batem com os filtros.

## Testes de Defeitos e Validação
- Testes funcionais com pytest (unitários)
- Testes de integração (simular camada de persistência)
- Testes de GUI (pytest-qt ou testes manuais documentados)
- Testes de borda: strings vazias, entrada nula, valores duplicados, limites numéricos
- Testes de concorrência: simular acessos simultâneos à base (se aplicável)

## Critérios de Aceitação Quantitativos
- Tempo de resposta (operação CRUD) < 500ms em dataset de 1k registros (ambiente de testes)
- Taxa de sucesso de execução de operações críticas = 100% em testes automatizados (sem falha)

## Plano de Testes (resumo)
1. Unit tests: cobrir serviços e validações (mock DAOs)
2. Integration tests: testar repositório + banco (usar sqlite em memória)
3. GUI tests: pytest-qt para interações básicas
4. Acceptance: executar cenários BDD via pytest-bdd ou behave