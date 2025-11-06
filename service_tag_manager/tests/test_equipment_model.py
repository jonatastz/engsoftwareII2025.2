import os
import tempfile
import sqlite3
import pytest
from service_tag_manager.model.equipment_model import EquipmentModel

# Importações:
# - os: permite manipular arquivos no sistema (para apagar o banco depois do teste)
# - tempfile: cria arquivos temporários (aqui cria um banco SQLite temporário)
# - sqlite3: biblioteca nativa para trabalhar com bancos SQLite
# - pytest: framework de testes automatizados
# - EquipmentModel: classe do sistema que gerencia os equipamentos (CRUD e consultas)

@pytest.fixture
def tmp_db_path():
    """Cria um banco de dados SQLite temporário para testes."""
    # Cria um arquivo temporário com extensão .sqlite3 (banco de teste)
    fd, path = tempfile.mkstemp(suffix=".sqlite3")
    os.close(fd)  # Fecha o descritor de arquivo temporário

    # Entrega o caminho do banco temporário para o teste usar
    yield path

    # Após o teste, tenta fechar e remover o banco de forma segura
    try:
        sqlite3.connect(path).close()  # Fecha qualquer conexão restante
    except Exception:
        pass
    if os.path.exists(path):
        try:
            os.remove(path)  # Remove o arquivo do banco após o teste
        except PermissionError:
            pass  # Se o arquivo estiver bloqueado, apenas ignora

def test_adicionar_e_consultar_equipamento(tmp_db_path):
    # Testa se é possível adicionar e consultar um equipamento corretamente

    em = EquipmentModel(db_path=tmp_db_path)  # Cria o modelo usando o banco temporário

    # Adiciona um novo equipamento ao banco
    eq_id = em.adicionar_equipamento(
        tag="ST-001",
        nome="Notebook Dell",
        descricao="Equipamento de teste",
        cliente="Jonatas",
        modelo="Inspiron",
        status="Ativo",
        prioridade="Alta",
    )

    # Verifica se o ID retornado é um número inteiro e maior que zero
    assert isinstance(eq_id, int) and eq_id > 0

    # Consulta o equipamento recém-adicionado usando a tag
    resultado = em.consultar(tag="ST-001")

    # Deve haver exatamente um resultado encontrado
    assert len(resultado) == 1

    # O nome do equipamento deve conter "Notebook"
    assert "Notebook" in resultado[0][2]

    # Fecha a conexão com o banco
    em.conn.close()

def test_atualizar_e_excluir_equipamento(tmp_db_path):
    # Testa se é possível atualizar e depois excluir um equipamento

    em = EquipmentModel(db_path=tmp_db_path)

    # Adiciona um equipamento inicial
    eq_id = em.adicionar_equipamento(tag="ST-002", nome="Impressora HP", descricao="Inicial")

    # Atualiza a descrição e o status do equipamento
    atualizado = em.atualizar_equipamento(eq_id, descricao="Atualizado", status="Manutenção")

    # Verifica se a atualização ocorreu com sucesso
    assert atualizado is True

    # Busca o equipamento atualizado pelo ID
    dados = em.obter_por_id(eq_id)

    # Verifica se o equipamento foi encontrado e se os campos estão atualizados
    assert dados is not None
    assert "Atualizado" in dados[6]      # coluna descricao
    assert "Manutenção" in dados[8]      # coluna status

    # Agora exclui o equipamento
    excluido = em.excluir_equipamento(eq_id)
    assert excluido is True

    # Tenta buscar novamente o mesmo ID (deve retornar None)
    dados = em.obter_por_id(eq_id)
    assert dados is None

    em.conn.close()

def test_consultar_com_multiplos_filtros(tmp_db_path):
    # Testa a consulta com diferentes filtros e termos de pesquisa

    em = EquipmentModel(db_path=tmp_db_path)

    # Adiciona dois equipamentos com características diferentes
    em.adicionar_equipamento(tag="A1", nome="Notebook Lenovo", cliente="EmpresaX", status="Ativo", prioridade="Alta")
    em.adicionar_equipamento(tag="B2", nome="Servidor Dell", cliente="EmpresaY", status="Parado", prioridade="Baixa")

    # Faz uma busca genérica por termo "Dell" (deve retornar apenas o Servidor Dell)
    resultado = em.consultar(termo="Dell")
    assert len(resultado) == 1
    assert "Servidor" in resultado[0][2]

    # Faz um filtro por status "Ativo" (deve retornar apenas o Notebook Lenovo)
    ativos = em.consultar(status="Ativo")
    assert len(ativos) == 1
    assert "Lenovo" in ativos[0][2]

    em.conn.close()

def test_adicionar_e_listar_servicos(tmp_db_path):
    # Testa a adição e listagem de serviços associados a um equipamento

    em = EquipmentModel(db_path=tmp_db_path)

    # Adiciona um novo equipamento
    eq_id = em.adicionar_equipamento(tag="ST-SRV1", nome="Servidor HP", descricao="Teste serviço")
    assert eq_id > 0

    # Adiciona dois serviços vinculados ao equipamento criado
    serv1 = em.adicionar_servico(eq_id, tipo="Limpeza", descricao="Limpeza interna", tecnico="Técnico A", custo=150)
    serv2 = em.adicionar_servico(eq_id, tipo="Troca", descricao="Troca de cooler", tecnico="Técnico B", custo=200)

    # Verifica se ambos os serviços foram adicionados com sucesso (IDs maiores que 0)
    assert serv1 > 0 and serv2 > 0

    # Lista todos os serviços associados ao equipamento
    lista = em.listar_servicos_por_equipamento(eq_id)

    # Deve haver exatamente dois serviços cadastrados
    assert len(lista) == 2

    # Verifica se há um serviço de "Limpeza" e outro de "Troca"
    assert any("Limpeza" in s[3] for s in lista)
    assert any("Troca" in s[3] for s in lista)

    em.conn.close()
