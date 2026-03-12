
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class HomeView(QWidget):
    """
    HomeView é um QWidget que representa a tela inicial da aplicação,
    com um banner de imagem central e três botões de navegação.
    """
    def __init__(self):
        super().__init__()
        
        # Layout principal vertical da tela
        root = QVBoxLayout(self)

        # -------------------------
        # Banner de imagem
        # -------------------------
        self.banner = QLabel()             # Cria um QLabel que exibirá a imagem
        self.banner.setAlignment(Qt.AlignCenter)  # Centraliza a imagem dentro do QLabel
        
        root.addStretch(1)                 # Espaço flexível acima do banner
        root.addWidget(self.banner, alignment=Qt.AlignCenter)  # Adiciona o banner ao layout centralizado
        root.addStretch(1)                 # Espaço flexível abaixo do banner

        # -------------------------
        # Linha de botões
        # -------------------------
        row = QHBoxLayout()                # Layout horizontal para os botões
        root.addLayout(row)

        # Criação dos botões
        self.btn_ir_cadastro = QPushButton("Cadastro")
        self.btn_ir_consulta = QPushButton("Consulta")
        self.btn_ir_historico = QPushButton("Histórico")

        # Adiciona espaçamento antes dos botões
        row.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        # Configura tamanho mínimo e adiciona cada botão ao layout horizontal
        for b in (self.btn_ir_cadastro, self.btn_ir_consulta, self.btn_ir_historico):
            b.setMinimumHeight(48)        # Altura mínima dos botões
            b.setMinimumWidth(180)        # Largura mínima dos botões
            row.addWidget(b)
        
        # Adiciona espaçamento depois dos botões
        row.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # -------------------------
        # Carregamento do banner
        # -------------------------
        # Caminho para a imagem (resources/home_banner.png)
        img_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "resources", "home_banner.png"))
        
        if os.path.exists(img_path):
            self._pix = QPixmap(img_path)  # Carrega a imagem em um QPixmap
            self._apply_banner_scale()     # Aplica escala proporcional à janela
        else:
            self._pix = None               # Caso a imagem não exista, define como None

    # -------------------------
    # Evento de redimensionamento
    # -------------------------
    def resizeEvent(self, event):
        """
        Evento chamado automaticamente quando a janela é redimensionada.
        Reaplica a escala da imagem do banner.
        """
        super().resizeEvent(event)
        self._apply_banner_scale()

    # -------------------------
    # Método interno para escalar o banner
    # -------------------------
    def _apply_banner_scale(self):
        """
        Redimensiona a imagem do banner proporcional ao tamanho da janela.
        Se não houver imagem (_pix é None), retorna imediatamente.
        """
        if not getattr(self, "_pix", None):  # Verifica se existe uma imagem carregada
            return  # Nada a fazer se não houver imagem

        # Define tamanho máximo do banner proporcional à janela
        max_w = max(300, int(self.width() * 0.8))  # largura: no mínimo 300, até 80% da largura da janela
        max_h = max(150, int(self.height() * 0.5)) # altura: no mínimo 150, até 50% da altura da janela

        # Redimensiona a imagem mantendo a proporção e suavizando a transformação
        scaled = self._pix.scaled(max_w, max_h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        # Atualiza o QLabel com a imagem escalada
        self.banner.setPixmap(scaled)

