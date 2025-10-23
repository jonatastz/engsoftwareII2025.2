import sys, types
# Criar stubs mínimos para PyQt5 antes de importar o controller
fake_pyqt5 = types.ModuleType("PyQt5")
fake_qtw = types.ModuleType("PyQt5.QtWidgets")
class DummyMsg:
    Yes = 1
    No = 0
    @staticmethod
    def question(*a, **k):
        return DummyMsg.Yes
setattr(fake_qtw, "QApplication", object)
setattr(fake_qtw, "QTableWidgetItem", object)
setattr(fake_qtw, "QMessageBox", DummyMsg)
fake_qtc = types.ModuleType("PyQt5.QtCore")
setattr(fake_qtc, "Qt", object)
setattr(fake_qtc, "QDate", object)
sys.modules["PyQt5"] = fake_pyqt5
sys.modules["PyQt5.QtWidgets"] = fake_qtw
sys.modules["PyQt5.QtCore"] = fake_qtc

from controller.main_controller import MainController

class FakeDate:
    def __init__(self, valid=True, s="2025-10-23"):
        self._valid = valid
        self._s = s
    def isValid(self):
        return self._valid
    def toString(self, fmt):
        return self._s

class FakeDateEdit:
    def __init__(self, date):
        self._date = date
    def date(self):
        return self._date

def test_date_str_safe_valid():
    mc = MainController(None, None, None, None, None, None)
    d = FakeDate(valid=True, s="2025-10-23")
    de = FakeDateEdit(d)
    assert mc._date_str_safe(de) == "2025-10-23"

def test_date_str_safe_invalid():
    mc = MainController(None, None, None, None, None, None)
    d = FakeDate(valid=False, s="invalid date")
    de = FakeDateEdit(d)
    assert mc._date_str_safe(de) is None

# Test _linha_para_id and _selected_equipment_from_table with a fake table
class FakeItem:
    def __init__(self, txt): self._t = txt
    def text(self): return str(self._t)

class FakeTable:
    def __init__(self, data, current=0):
        self._data = data
        self._current = current
    def currentRow(self): return self._current
    def item(self, row, col):
        try:
            return FakeItem(self._data[row][col])
        except Exception:
            return None

def test_linha_para_id_and_selection():
    mc = MainController(None, None, None, None, None, None)
    # table with one row: [id, tag, nome]
    table = FakeTable([[5, "TAG-1", "Nome A"]], current=0)
    assert mc._linha_para_id(table, 0) == 5
    equip_id, nome = mc._selected_equipment_from_table(table)
    assert equip_id == 5
    assert "Nome" in nome or isinstance(nome, str)
