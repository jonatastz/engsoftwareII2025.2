from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Entrar")
        self.setModal(True)
        self.setMinimumWidth(420)
        self.setObjectName("LoginDialog")

        root = QVBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(16)

        card = QFrame(self)
        card.setObjectName("LoginCard")
        card.setFrameShape(QFrame.StyledPanel)
        card.setProperty("class", "card")
        card_lyt = QVBoxLayout(card)
        card_lyt.setContentsMargins(24, 24, 24, 24)
        card_lyt.setSpacing(14)

        title = QLabel("Service Tag Manager")
        title.setObjectName("LoginTitle")
        subtitle = QLabel("Acesse sua conta para continuar")
        subtitle.setObjectName("LoginSubtitle")
        card_lyt.addWidget(title, 0, Qt.AlignHCenter)
        card_lyt.addWidget(subtitle, 0, Qt.AlignHCenter)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft)
        form.setFormAlignment(Qt.AlignHCenter)
        form.setHorizontalSpacing(10)
        form.setVerticalSpacing(10)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Usuário")
        self.username.setClearButtonEnabled(True)
        self.username.setObjectName("LoginUser")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Senha")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("LoginPass")

        self.btn_toggle = QPushButton("Mostrar")
        self.btn_toggle.setCheckable(True)
        self.btn_toggle.setObjectName("BtnShowPass")
        self.btn_toggle.setCursor(Qt.PointingHandCursor)
        self.btn_toggle.setFixedWidth(84)
        self.btn_toggle.toggled.connect(self._toggle_pass)

        pass_row = QHBoxLayout()
        pass_row.addWidget(self.password, 1)
        pass_row.addWidget(self.btn_toggle, 0, Qt.AlignRight)

        form.addRow("Usuário", self.username)
        form.addRow("Senha", pass_row)

        card_lyt.addLayout(form)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.button(QDialogButtonBox.Ok).setText("Entrar")
        self.buttons.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        card_lyt.addWidget(self.buttons)

        root.addWidget(card, 0, Qt.AlignCenter)

        self.setStyleSheet("""
        #LoginDialog { background-color: transparent; }
        QFrame#LoginCard { 
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 12px;
            padding: 8px;
            background-color: rgba(0,0,0,0.25);
        }
        QLabel#LoginTitle {
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 2px;
        }
        QLabel#LoginSubtitle {
            font-size: 12px;
            color: #cbd5e1;
            margin-bottom: 8px;
        }
        QLineEdit#LoginUser, QLineEdit#LoginPass {
            min-height: 34px;
            border-radius: 8px;
            padding: 6px 10px;
        }
        QPushButton#BtnShowPass {
            min-height: 34px;
            border-radius: 8px;
            padding: 6px 10px;
        }
        """)

        self.password.returnPressed.connect(self._press_ok)
        self.username.setFocus()

    def _toggle_pass(self, checked: bool):
        self.password.setEchoMode(QLineEdit.Normal if checked else QLineEdit.Password)
        self.btn_toggle.setText("Ocultar" if checked else "Mostrar")

    def _press_ok(self):
        ok = self.buttons.button(QDialogButtonBox.Ok)
        if ok.isEnabled():
            ok.click()

    def get_credentials(self):
        return self.username.text().strip(), self.password.text()
