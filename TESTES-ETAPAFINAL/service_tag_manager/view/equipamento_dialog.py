from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import (
    QComboBox,
    QDateEdit,
    QDialog,
    QDoubleSpinBox,
    QLineEdit,
    QSpinBox,
    QTextEdit,
)
from PyQt5.uic import loadUi


class EquipamentoDialog(QDialog):
    fld_id: QLineEdit
    fld_tag: QLineEdit
    fld_nome: QLineEdit
    fld_cliente: QLineEdit
    fld_modelo: QLineEdit
    fld_serial: QLineEdit
    fld_tipo: QComboBox
    fld_status: QComboBox
    fld_prioridade: QComboBox
    fld_proxima: QDateEdit
    fld_custo: QDoubleSpinBox
    fld_garantia: QSpinBox
    fld_descricao: QTextEdit
    fld_obs: QTextEdit

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("view/ui_equipamento_dialog.ui", self)

    def set_data(self, row):
        self.fld_id.setText(str(row.get("id", "")))
        self.fld_tag.setText(row.get("tag", "") or "")
        self.fld_nome.setText(row.get("nome", "") or "")
        self.fld_cliente.setText(row.get("cliente", "") or "")
        self.fld_modelo.setText(row.get("modelo", "") or "")
        self.fld_serial.setText(row.get("serial", "") or "")
        self.fld_tipo.setCurrentText(row.get("tipo_servico", "") or "Diagnóstico")
        self.fld_status.setCurrentText(row.get("status", "") or "Recebido")
        self.fld_prioridade.setCurrentText(row.get("prioridade", "") or "Média")

        data_proxima = row.get("proxima_manutencao")
        if data_proxima:
            try:
                y, m, d = [int(x) for x in data_proxima.split("-")]
                self.fld_proxima.setDate(QDate(y, m, d))
            except Exception:
                pass

        self.fld_custo.setValue(float(row.get("custo") or 0))
        self.fld_garantia.setValue(int(row.get("garantia_meses") or 0))
        self.fld_descricao.setPlainText(row.get("descricao", "") or "")
        self.fld_obs.setPlainText(row.get("observacoes", "") or "")

    def get_data(self):
        return {
            "id": int(self.fld_id.text() or 0),
            "tag": self.fld_tag.text().strip(),
            "nome": self.fld_nome.text().strip(),
            "cliente": self.fld_cliente.text().strip(),
            "modelo": self.fld_modelo.text().strip(),
            "serial": self.fld_serial.text().strip(),
            "tipo_servico": self.fld_tipo.currentText(),
            "status": self.fld_status.currentText(),
            "prioridade": self.fld_prioridade.currentText(),
            "proxima_manutencao": self.fld_proxima.date().toString("yyyy-MM-dd"),
            "custo": float(self.fld_custo.value()),
            "garantia_meses": int(self.fld_garantia.value()),
            "descricao": self.fld_descricao.toPlainText().strip(),
            "observacoes": self.fld_obs.toPlainText().strip(),
        }
    