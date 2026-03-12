import types
import pytest
from service_tag_manager.controller.main_controller import MainController

# Importações:
# - "types" é uma biblioteca padrão do Python (não é usada aqui, mas pode ser usada para manipular tipos dinamicamente).
# - "pytest" é a ferramenta usada para executar testes automatizados.
# - "MainController" é a classe principal do sistema que contém o método que queremos testar (_date_str_safe).

class FakeDate:
    # Essa classe serve para simular um objeto de data real (como o QDate do PyQt5),
    # sem precisar abrir a interface gráfica durante o teste.

    def __init__(self, text, valid=True):
        # Quando criamos um FakeDate, passamos:
        # - "text": o texto da data (exemplo: "2025-11-06")
        # - "valid": um valor booleano dizendo se a data é válida (True) ou não (False)
        self._text = text
        self._valid = valid

    def toString(self, fmt):
        # Esse método imita o método real "toString()" de um objeto QDate.
        # No PyQt, esse método formata a data em texto (ex: "2025-11-06").
        # Aqui, simplesmente retornamos o texto guardado em _text.
        return self._text

    def isValid(self):
        # Esse método retorna se a data é válida ou não.
        # No código real, isso seria usado para verificar se o campo de data foi preenchido corretamente.
        return self._valid

class FakeDateEdit:
    # Essa classe simula um campo de data da interface (como QDateEdit do PyQt5).
    # Ela contém internamente um objeto FakeDate, representando a data selecionada pelo usuário.

    def __init__(self, text, valid=True):
        # Quando criamos um FakeDateEdit, ele cria internamente um FakeDate com os mesmos valores.
        self._d = FakeDate(text, valid)

    def date(self):
        # Esse método retorna o objeto FakeDate armazenado.
        # Isso imita o comportamento real do método QDateEdit.date() no PyQt.
        return self._d

def test_date_str_safe_valid():
    # Esse teste verifica o comportamento do método _date_str_safe quando a data é VÁLIDA.

    # Aqui, criamos um objeto de MainController "vazio" sem chamar o __init__.
    # Fazemos isso apenas para poder usar o método interno _date_str_safe diretamente.
    mc = MainController.__new__(MainController)

    # Agora chamamos o método que queremos testar, passando uma data válida.
    s = MainController._date_str_safe(mc, FakeDateEdit("2025-11-06"))

    # O método deve retornar a string "2025-11-06" se tudo estiver certo.
    assert s == "2025-11-06"

def test_date_str_safe_invalid():
    # Esse teste verifica o comportamento do mesmo método, mas com uma data INVÁLIDA.

    # Criamos novamente um objeto "vazio" de MainController.
    mc = MainController.__new__(MainController)

    # Teste 1: passamos uma data marcada como inválida (valid=False).
    # O método deve retornar None, indicando que a data não é válida.
    s1 = MainController._date_str_safe(mc, FakeDateEdit("invalid", valid=False))
    assert s1 is None

    # Teste 2: passamos uma data com texto inválido ("Invalid"), mas sem marcar o campo como inválido explicitamente.
    # Mesmo assim, o método deve detectar o erro e retornar None.
    s2 = MainController._date_str_safe(mc, FakeDateEdit("Invalid"))
    assert s2 is None
