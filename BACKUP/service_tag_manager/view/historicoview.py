from PyQt5.QtCore import QDate

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, QComboBox, QDateEdit

class HistoricoView(QWidget):
    def __init__(self):
        super().__init__()
        root = QVBoxLayout(self)
        self.setObjectName("HistoricoPage")

        title = QLabel("Histórico - Equipamentos"); 
        root.addWidget(title)
        title.setObjectName("pageTitle")
        # Filtros (Histórico)
        fl = QHBoxLayout()
        root.addLayout(fl)

        fl.addWidget(QLabel("Termo"))
        self.input_termo_h = QLineEdit(); self.input_termo_h.setPlaceholderText("tag, nome, cliente, modelo...")
        fl.addWidget(self.input_termo_h)

        fl.addWidget(QLabel("Status"))
        self.combo_status_h = QComboBox(); self.combo_status_h.addItems(["", "Recebido", "Em análise", "Em execução", "Pronto", "Entregue"])
        fl.addWidget(self.combo_status_h)

        fl.addWidget(QLabel("Prioridade"))
        self.combo_prioridade_h = QComboBox(); self.combo_prioridade_h.addItems(["", "Baixa", "Média", "Alta", "Urgente"])
        fl.addWidget(self.combo_prioridade_h)

        fl.addWidget(QLabel("Próx. Manut. de"))
        self.date_ini_h = QDateEdit(); self.date_ini_h.setCalendarPopup(True)
        self.date_ini_h.setDisplayFormat('yyyy-MM-dd')
        self.date_ini_h.setDate(QDate.currentDate().addMonths(-1))
        fl.addWidget(self.date_ini_h)

        fl.addWidget(QLabel("até"))
        self.date_fim_h = QDateEdit(); self.date_fim_h.setCalendarPopup(True)
        self.date_fim_h.setDisplayFormat('yyyy-MM-dd')
        self.date_fim_h.setDate(QDate.currentDate())
        fl.addWidget(self.date_fim_h)

        self.btn_buscar_h = QPushButton("Buscar")
        self.btn_limpar_h = QPushButton("Limpar")
        fl.addWidget(self.btn_buscar_h); fl.addWidget(self.btn_limpar_h)


        self.table_historico = QTableWidget(0, 9)
        self.table_historico.setHorizontalHeaderLabels([
            "ID","Tag","Nome","Cliente","Modelo","Status","Prioridade","Próx. Manut.","Data Cad."
        ])
        h = self.table_historico.horizontalHeader()
        h.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        h.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        h.setSectionResizeMode(2, QHeaderView.Stretch)
        h.setSectionResizeMode(3, QHeaderView.Stretch)
        h.setSectionResizeMode(4, QHeaderView.Stretch)
        h.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        h.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        h.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        h.setSectionResizeMode(8, QHeaderView.ResizeToContents)
        self.table_historico.setSelectionBehavior(self.table_historico.SelectRows)
        self.table_historico.setSelectionMode(self.table_historico.SingleSelection)
        self.table_historico.setEditTriggers(self.table_historico.NoEditTriggers)
        self.table_historico.setColumnHidden(0, True)
        root.addWidget(self.table_historico, 1)

        bar = QHBoxLayout()
        self.lbl_count_h = QLabel("0 resultados")
        self.btn_ver_historico_h = QPushButton("Ver Histórico")
        self.btn_editar_h = QPushButton("Editar")
        self.btn_excluir_h = QPushButton("Excluir")
        self.btn_novo_servico_h = QPushButton("Novo Serviço")
        self.btn_voltar_historico = QPushButton("Voltar")
        bar.addWidget(self.lbl_count_h); bar.addStretch(1)
        for b in [self.btn_ver_historico_h, self.btn_novo_servico_h, self.btn_editar_h, self.btn_excluir_h, self.btn_voltar_historico]:
            bar.addWidget(b)
        self.btn_sair = QPushButton("Sair")
        bar.addWidget(self.btn_sair)
        root.addLayout(bar)
