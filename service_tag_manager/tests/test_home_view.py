# test_home_view.py
import pytest
from PyQt5.QtGui import QPixmap
from view.home_view import HomeView  # ajuste o import conforme sua estrutura

# --------------------------------------------------------------------
# Fixture: cria a HomeView e adiciona ao qtbot
# --------------------------------------------------------------------
@pytest.fixture
def home_view(qtbot):
    """
    Cria o widget HomeView e adiciona ao qtbot para teste.
    """
    view = HomeView()
    qtbot.addWidget(view)
    view.show()
    return view

# --------------------------------------------------------------------
# Teste dos botões
# --------------------------------------------------------------------
def test_buttons_exist(home_view):
    """
    Verifica se os botões existem, têm o texto correto e tamanho mínimo.
    """
    for text, btn in [("Cadastro", home_view.btn_ir_cadastro),
                      ("Consulta", home_view.btn_ir_consulta),
                      ("Histórico", home_view.btn_ir_historico)]:
        assert btn.text() == text
        assert btn.minimumWidth() >= 180
        assert btn.minimumHeight() >= 48

# --------------------------------------------------------------------
# Teste do banner com imagem existente
# --------------------------------------------------------------------
def test_banner_with_image(home_view, qtbot):
    """
    Testa se o banner tenta carregar a imagem corretamente.
    Se a imagem existir, _pix deve ser um QPixmap válido.
    """
    if home_view._pix is None:
        pytest.skip("Imagem de banner não existe, teste ignora")
    assert isinstance(home_view._pix, QPixmap)
    # Redimensionamento do banner deve ocorrer sem erros
    home_view.resize(800, 600)
    qtbot.wait(50)
    pixmap = home_view.banner.pixmap()
    assert pixmap.width() <= int(home_view.width() * 0.8) + 1
    assert pixmap.height() <= int(home_view.height() * 0.5) + 1

# --------------------------------------------------------------------
# Teste do banner quando a imagem não existe
# --------------------------------------------------------------------
def test_banner_no_image(monkeypatch, qtbot):
    """
    Simula que a imagem não existe, garantindo que o else (_pix = None) seja executado.
    Também garante que _apply_banner_scale retorna sem erro quando _pix é None.
    """
    # Monkeypatch para forçar inexistência do arquivo
    monkeypatch.setattr("os.path.exists", lambda path: False)

    view = HomeView()
    qtbot.addWidget(view)

    # Deve ter executado: self._pix = None
    assert view._pix is None

    # Chama _apply_banner_scale, deve executar o "return" sem erro
    view._apply_banner_scale()
    assert True  # chegou aqui sem erro significa que o return foi executado

# --------------------------------------------------------------------
# Teste direto de _apply_banner_scale sem pixmap
# --------------------------------------------------------------------
def test_apply_banner_scale_no_pix(qtbot):
    """
    Garante que o return em _apply_banner_scale seja executado quando _pix é None.
    """
    view = HomeView()
    qtbot.addWidget(view)

    # Força _pix ser None
    view._pix = None

    # Chama o método, deve retornar imediatamente sem erro
    view._apply_banner_scale()
    assert True
