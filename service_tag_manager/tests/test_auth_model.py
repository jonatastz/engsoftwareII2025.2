import os
import sqlite3
import importlib
from service_tag_manager.model.auth_model import AuthModel, _hash

# Importações:
# - os: permite manipular arquivos e caminhos (usado em alguns testes com banco de dados)
# - sqlite3: biblioteca nativa do Python para manipular bancos SQLite
# - importlib: usada para recarregar módulos, útil em testes (embora não seja usada aqui diretamente)
# - AuthModel: classe responsável pelo controle de autenticação (login, validação de usuário)
# - _hash: função interna que gera o hash (criptografia SHA-256) das senhas

def test_hash_function_is_sha256():
    # Esse teste garante que a função _hash está funcionando corretamente.
    # Ela deve gerar o mesmo hash para o mesmo texto
    # e hashes diferentes para textos diferentes (inclusive se apenas mudar maiúscula/minúscula).

    # Garante que a função é determinística: mesmo texto, mesmo hash
    assert _hash("admin") == _hash("admin")

    # Garante que textos diferentes produzem hashes diferentes
    assert _hash("admin") != _hash("Admin")

def test_authmodel_bootstrap_creates_admin(tmp_db_path):
    # Esse teste verifica se o AuthModel cria automaticamente
    # um usuário "admin" padrão ao inicializar o banco de dados.

    # Cria uma instância de AuthModel usando um banco de dados temporário
    m = AuthModel(db_path=tmp_db_path)

    # Tenta autenticar com o usuário padrão: "admin" / "admin"
    ok, user = m.validate("admin", "admin")

    # Deve retornar sucesso (ok == True)
    assert ok is True

    # O nome do usuário retornado deve ser "admin"
    assert user.get("username") == "admin"

    # E o dicionário deve conter a chave "display_name", usada na interface
    assert "display_name" in user

def test_authmodel_invalid_login(tmp_db_path):
    # Esse teste garante que logins inválidos são rejeitados corretamente.

    # Cria o modelo de autenticação com um banco temporário
    m = AuthModel(db_path=tmp_db_path)

    # Tenta validar credenciais incorretas
    ok, user = m.validate("nope", "bad")

    # Deve retornar False (falha de autenticação)
    assert ok is False

    # E o dicionário retornado deve ser vazio
    assert user == {}
