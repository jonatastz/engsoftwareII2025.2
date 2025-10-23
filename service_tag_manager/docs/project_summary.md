# Análise do projeto

Gerado em: 2025-10-23T20:08:21.603573Z


## SERVICE TAG PRONTO/service_tag_manager/main.py

- Classes: []

- Functions: []

- Imports: ['PyQt5.QtWidgets.QApplication', 'PyQt5.QtWidgets.QStackedWidget', 'controller.main_controller.MainController', 'model.auth_model.AuthModel', 'model.equipment_model.EquipmentModel', 'sys', 'view.consultaview.ConsultaView', 'view.historicoview.HistoricoView', 'view.home_view.HomeView', 'view.login_view.LoginDialog', 'view.main_view.MainView']


## SERVICE TAG PRONTO/service_tag_manager/controller/main_controller.py

- Classes: ['MainController']

- Functions: []

- Imports: ['PyQt5.QtCore.QDate', 'PyQt5.QtCore.Qt', 'PyQt5.QtWidgets.QApplication', 'PyQt5.QtWidgets.QMessageBox', 'PyQt5.QtWidgets.QTableWidgetItem', 'view.detalheview.DetalheView', 'view.service_dialog.ServiceDialog', 'view.service_history_dialog.ServiceHistoryDialog']


## SERVICE TAG PRONTO/service_tag_manager/model/auth_model.py

- Classes: ['AuthModel']

- Functions: ['_hash']

- Imports: ['hashlib', 'sqlite3']


## SERVICE TAG PRONTO/service_tag_manager/model/database.py

- Classes: ['Database']

- Functions: []

- Imports: ['sqlite3']


## SERVICE TAG PRONTO/service_tag_manager/model/equipment_model.py

- Classes: ['EquipmentModel']

- Functions: []

- Imports: ['os', 'sqlite3']


## SERVICE TAG PRONTO/service_tag_manager/view/consultaview.py

- Classes: ['ConsultaView']

- Functions: []

- Imports: ['PyQt5.QtCore.QDate', 'PyQt5.QtWidgets.QComboBox', 'PyQt5.QtWidgets.QDateEdit', 'PyQt5.QtWidgets.QHBoxLayout', 'PyQt5.QtWidgets.QHeaderView', 'PyQt5.QtWidgets.QLabel', 'PyQt5.QtWidgets.QLineEdit', 'PyQt5.QtWidgets.QPushButton', 'PyQt5.QtWidgets.QTableWidget', 'PyQt5.QtWidgets.QTableWidgetItem', 'PyQt5.QtWidgets.QVBoxLayout', 'PyQt5.QtWidgets.QWidget']


## SERVICE TAG PRONTO/service_tag_manager/view/detalheview.py

- Classes: ['DetalheView']

- Functions: []

- Imports: ['PyQt5.QtCore.QDate', 'PyQt5.QtWidgets.QComboBox', 'PyQt5.QtWidgets.QDateEdit', 'PyQt5.QtWidgets.QDialog', 'PyQt5.QtWidgets.QDialogButtonBox', 'PyQt5.QtWidgets.QDoubleSpinBox', 'PyQt5.QtWidgets.QFormLayout', 'PyQt5.QtWidgets.QLabel', 'PyQt5.QtWidgets.QLineEdit', 'PyQt5.QtWidgets.QSpinBox', 'PyQt5.QtWidgets.QTextEdit']


## SERVICE TAG PRONTO/service_tag_manager/view/equipamento_dialog.py

- Classes: ['EquipamentoDialog']

- Functions: []

- Imports: ['PyQt5.QtCore.QDate', 'PyQt5.QtWidgets.QDialog', 'PyQt5.uic']


## SERVICE TAG PRONTO/service_tag_manager/view/historicoview.py

- Classes: ['HistoricoView']

- Functions: []

- Imports: ['PyQt5.QtCore.QDate', 'PyQt5.QtWidgets.QComboBox', 'PyQt5.QtWidgets.QDateEdit', 'PyQt5.QtWidgets.QHBoxLayout', 'PyQt5.QtWidgets.QHeaderView', 'PyQt5.QtWidgets.QLabel', 'PyQt5.QtWidgets.QLineEdit', 'PyQt5.QtWidgets.QPushButton', 'PyQt5.QtWidgets.QTableWidget', 'PyQt5.QtWidgets.QTableWidgetItem', 'PyQt5.QtWidgets.QVBoxLayout', 'PyQt5.QtWidgets.QWidget']


## SERVICE TAG PRONTO/service_tag_manager/view/home_view.py

- Classes: ['HomeView']

- Functions: []

- Imports: ['PyQt5.QtCore.Qt', 'PyQt5.QtGui.QPixmap', 'PyQt5.QtWidgets.QHBoxLayout', 'PyQt5.QtWidgets.QLabel', 'PyQt5.QtWidgets.QPushButton', 'PyQt5.QtWidgets.QSizePolicy', 'PyQt5.QtWidgets.QSpacerItem', 'PyQt5.QtWidgets.QVBoxLayout', 'PyQt5.QtWidgets.QWidget', 'os']


## SERVICE TAG PRONTO/service_tag_manager/view/login_view.py

- Classes: ['LoginDialog']

- Functions: []

- Imports: ['PyQt5.QtCore.Qt', 'PyQt5.QtWidgets.QDialog', 'PyQt5.QtWidgets.QDialogButtonBox', 'PyQt5.QtWidgets.QFormLayout', 'PyQt5.QtWidgets.QFrame', 'PyQt5.QtWidgets.QHBoxLayout', 'PyQt5.QtWidgets.QLabel', 'PyQt5.QtWidgets.QLineEdit', 'PyQt5.QtWidgets.QPushButton', 'PyQt5.QtWidgets.QVBoxLayout']


## SERVICE TAG PRONTO/service_tag_manager/view/main_view.py

- Classes: ['MainView']

- Functions: []

- Imports: ['PyQt5.QtCore.QDate', 'PyQt5.QtWidgets.QComboBox', 'PyQt5.QtWidgets.QDateEdit', 'PyQt5.QtWidgets.QDoubleSpinBox', 'PyQt5.QtWidgets.QGridLayout', 'PyQt5.QtWidgets.QHBoxLayout', 'PyQt5.QtWidgets.QLabel', 'PyQt5.QtWidgets.QLineEdit', 'PyQt5.QtWidgets.QMainWindow', 'PyQt5.QtWidgets.QPushButton', 'PyQt5.QtWidgets.QSizePolicy', 'PyQt5.QtWidgets.QSpinBox', 'PyQt5.QtWidgets.QTextEdit', 'PyQt5.QtWidgets.QVBoxLayout', 'PyQt5.QtWidgets.QWidget']


## SERVICE TAG PRONTO/service_tag_manager/view/service_dialog.py

- Classes: ['ServiceDialog']

- Functions: []

- Imports: ['PyQt5.QtCore.QDate', 'PyQt5.QtWidgets.QDateEdit', 'PyQt5.QtWidgets.QDialog', 'PyQt5.QtWidgets.QDialogButtonBox', 'PyQt5.QtWidgets.QDoubleSpinBox', 'PyQt5.QtWidgets.QFormLayout', 'PyQt5.QtWidgets.QLabel', 'PyQt5.QtWidgets.QLineEdit', 'PyQt5.QtWidgets.QSpinBox', 'PyQt5.QtWidgets.QTextEdit']


## SERVICE TAG PRONTO/service_tag_manager/view/service_history_dialog.py

- Classes: ['ServiceHistoryDialog']

- Functions: []

- Imports: ['PyQt5.QtWidgets.QDialog', 'PyQt5.QtWidgets.QHeaderView', 'PyQt5.QtWidgets.QLabel', 'PyQt5.QtWidgets.QTableWidget', 'PyQt5.QtWidgets.QTableWidgetItem', 'PyQt5.QtWidgets.QVBoxLayout']

