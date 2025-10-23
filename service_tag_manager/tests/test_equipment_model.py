from model.equipment_model import EquipmentModel
import os

def test_equipment_add_and_get(tmp_path):
    db_file = tmp_path / "equipamentos_test.db"
    em = EquipmentModel(str(db_file))
    eid = em.adicionar_equipamento("TAG-001", "Máquina A", descricao="desc")
    assert isinstance(eid, int)
    rec = em.obter_por_id(eid)
    assert rec is not None
    assert rec[1] == "TAG-001" or rec[1] == "TAG-001"

def test_servico_add_and_list(tmp_path):
    db_file = tmp_path / "equipamentos_test2.db"
    em = EquipmentModel(str(db_file))
    eid = em.adicionar_equipamento("TAG-002", "Máquina B")
    sid = em.adicionar_servico(eid, data_servico="2025-10-23", tipo="Manutenção", descricao="troca")
    assert isinstance(sid, int)
    servs = em.listar_servicos_por_equipamento(eid)
    assert len(servs) == 1
    assert servs[0][1] == eid
