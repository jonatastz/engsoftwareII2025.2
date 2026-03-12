import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QResizeEvent
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class HomeView(QWidget):
    """
    HomeView é um QWidget que representa a tela inicial da aplicação,
    com um banner de imagem central e três botões de navegação.
    """

    def __init__(self):
        super().__init__()

        root = QVBoxLayout(self)

        self.banner = QLabel()
        self.banner.setAlignment(Qt.AlignmentFlag.AlignCenter)

        root.addStretch(1)
        root.addWidget(self.banner, alignment=Qt.AlignmentFlag.AlignCenter)
        root.addStretch(1)

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

        img_path = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "..", "resources", "home_banner.png")
        )

        self._pix = QPixmap(img_path) if os.path.exists(img_path) else None
        self._apply_banner_scale()

    def resizeEvent(self, a0: QResizeEvent) -> None:
        super().resizeEvent(a0)
        self._apply_banner_scale()

    def _apply_banner_scale(self):
        pixmap = getattr(self, "_pix", None)
        if pixmap is None:
            self.banner.clear()
            return

        if pixmap.isNull():
            self.banner.clear()
            return

        max_w = max(300, int(self.width() * 0.8))
        max_h = max(150, int(self.height() * 0.5))

        scaled = pixmap.scaled(
            max_w,
            max_h,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.banner.setPixmap(scaled)
