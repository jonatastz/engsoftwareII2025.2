import os
import tempfile
import pathlib
import sqlite3
import pytest

# Importações:
# - os: usado para manipular caminhos e arquivos do sistema.
# - tempfile: cria arquivos ou diretórios temporários (úteis em testes).
# - pathlib: facilita o trabalho com caminhos de arquivos usando objetos (em vez de strings).
# - sqlite3: biblioteca padrão do Python para criar e manipular bancos de dados SQLite.
# - pytest: framework de testes automatizados, usado para rodar e gerenciar testes.

@pytest.fixture
def tmp_db_path(tmp_path):
    # Essa função é uma "fixture" do pytest — ou seja, um recurso auxiliar
    # que cria algo antes do teste (nesse caso, um banco temporário) e entrega para o teste usar.

    # Cria um caminho para o banco de dados SQLite dentro do diretório temporário
    db = tmp_path / "test_db.sqlite3"

    # Garante que o arquivo realmente existe.
    # Isso evita erros com caminhos relativos em alguns sistemas operacionais.
    sqlite3.connect(db).close()

    # Retorna o caminho do banco convertido em string, para ser usado em outras funções de teste.
    return str(db)
