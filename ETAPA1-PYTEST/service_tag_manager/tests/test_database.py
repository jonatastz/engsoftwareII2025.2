from service_tag_manager.model.database import Database

# Importa a classe Database, que representa a conexão e manipulação do banco de dados do sistema.
# Essa classe é responsável por criar tabelas, inserir dados e fazer consultas.

def test_database_insert_and_read(tmp_db_path):
    # Esse teste verifica se é possível inserir um equipamento no banco de dados
    # e depois ler esse mesmo dado corretamente.

    # Cria uma instância do banco, usando o caminho temporário gerado pelo pytest.
    # Assim, cada teste usa um banco novo, isolado, que é apagado depois.
    db = Database(db_name=tmp_db_path)

    # Insere um novo equipamento no banco.
    # Parâmetros: tag, nome do equipamento e descrição.
    db.insert_equipment("TAG-9", "Roteador", "Edge device")

    # Busca todos os equipamentos cadastrados até o momento.
    items = db.get_all_equipments()

    # Verifica se há exatamente um registro no banco.
    assert len(items) == 1

    # Pega a primeira (e única) linha retornada da consulta.
    row = items[0]

    # A estrutura da tabela é:
    # (id, service_tag, equipment_name, description, date_added)
    # Então validamos que os campos específicos foram salvos corretamente.

    # A tag do equipamento deve ser "TAG-9"
    assert row[1] == "TAG-9"

    # O nome do equipamento deve ser "Roteador"
    assert row[2] == "Roteador"
