
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class HomeView(QWidget):
    def __init__(self):
        super().__init__()
        root = QVBoxLayout(self)

        # Image banner
        self.banner = QLabel()
        self.banner.setAlignment(Qt.AlignCenter)
        root.addStretch(1)
        root.addWidget(self.banner, alignment=Qt.AlignCenter)
        root.addStretch(1)

        # Buttons row
        row = QHBoxLayout()
        root.addLayout(row)

        self.btn_ir_cadastro = QPushButton("Cadastro")
        self.btn_ir_consulta = QPushButton("Consulta")
        self.btn_ir_historico = QPushButton("Histórico")

        row.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        for b in (self.btn_ir_cadastro, self.btn_ir_consulta, self.btn_ir_historico):
            b.setMinimumHeight(48)
            b.setMinimumWidth(180)
            row.addWidget(b)
        row.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Load banner image
        img_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "resources", "home_banner.png"))
        if os.path.exists(img_path):
            self._pix = QPixmap(img_path)
            self._apply_banner_scale()
        else:
            self._pix = None

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._apply_banner_scale()

    def _apply_banner_scale(self):
        if not getattr(self, "_pix", None):
            return
        # Limit banner size proportional to window
        max_w = max(300, int(self.width() * 0.8))
        max_h = max(150, int(self.height() * 0.5))
        scaled = self._pix.scaled(max_w, max_h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.banner.setPixmap(scaled)
