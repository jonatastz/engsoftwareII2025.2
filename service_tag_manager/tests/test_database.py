import os
import sqlite3
from model.database import Database

def test_database_create_and_insert(tmp_path):
    db_file = tmp_path / "test.db"
    db = Database(str(db_file))
    # inserir um equipamento
    db.insert_equipment("ST-001", "Impressora X", "Descrição teste")
    rows = db.get_all_equipments()
    assert len(rows) == 1
    service_tag = rows[0][1]
    assert service_tag == "ST-001"
