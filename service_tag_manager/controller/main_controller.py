
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt, QDate
from view.service_dialog import ServiceDialog
from view.service_history_dialog import ServiceHistoryDialog
from view.detalheview import DetalheView

class MainController:
    def _date_str_safe(self, date_edit):
        try:
            d = date_edit.date()
            if hasattr(d, 'isValid') and not d.isValid():
                return None
            s = d.toString('yyyy-MM-dd')
            if not s or s.lower().startswith('invalid'):
                return None
            return s
        except Exception:
            return None

    def __init__(self, stacked_widget, home_view, main_view, consulta_view, historico_view, model):
        self.stacked_widget = stacked_widget
        self.home_view = home_view
        self.main_view = main_view
        self.consulta_view = consulta_view
        self.historico_view = historico_view
        self.model = model

        # ===== Home =====
        self.home_view.btn_ir_cadastro.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.home_view.btn_ir_consulta.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.home_view.btn_ir_historico.clicked.connect(self.mostrar_historico)

        # ===== Cadastro (Main) =====
        self.main_view.btn_add.clicked.connect(self.adicionar_equipamento)
        if hasattr(self.main_view, 'btn_voltar_main'):
            self.main_view.btn_voltar_main.clicked.connect(self.voltar)
        if hasattr(self.main_view, 'btn_sair'):
            self.main_view.btn_sair.clicked.connect(self.sair)

        # ===== Consulta =====
        v = self.consulta_view
        v.btn_voltar_consulta.clicked.connect(self.voltar)
        v.btn_editar.clicked.connect(self._abrir_detalhe_selecionado)
        v.btn_excluir.clicked.connect(self._excluir_selecionado)
        v.btn_limpar.clicked.connect(self._consulta_limpar)
        v.btn_buscar.clicked.connect(self._consulta_buscar)
        v.btn_novo_servico.clicked.connect(self._novo_servico_consulta)
        v.table_resultados.itemDoubleClicked.connect(lambda *_: self._mostrar_historico_do_selecionado('consulta'))
        if hasattr(v, 'btn_sair'):
            v.btn_sair.clicked.connect(self.sair)

        # ===== Histórico =====
        h = self.historico_view
        h.btn_voltar_historico.clicked.connect(self.voltar)
        h.btn_editar_h.clicked.connect(self._abrir_detalhe_selecionado_hist)
        h.btn_excluir_h.clicked.connect(self._excluir_selecionado_hist)
        try:
            h.btn_ver_historico_h.clicked.connect(lambda: self._mostrar_historico_do_selecionado('historico'))
        except Exception:
            pass
        h.btn_novo_servico_h.clicked.connect(self._novo_servico_historico)
        if hasattr(h, 'btn_buscar_h'):
            h.btn_buscar_h.clicked.connect(self._historico_buscar)
        if hasattr(h, 'btn_limpar_h'):
            h.btn_limpar_h.clicked.connect(self._historico_limpar)
        h.table_historico.itemDoubleClicked.connect(lambda *_: self._mostrar_historico_do_selecionado('historico'))
        if hasattr(h, 'btn_sair'):
            h.btn_sair.clicked.connect(self.sair)

    # ============================ UTIL ============================
    def _msg_info(self, title, text):
        QMessageBox.information(self.stacked_widget, title, text)

    def _msg_erro(self, title, text):
        QMessageBox.critical(self.stacked_widget, title, text)

    def _linha_para_id(self, table, row):
        item = table.item(row, 0)
        if not item:
            return None
        try:
            return int(item.text())
        except Exception:
            return None

    def _selected_equipment_from_table(self, table):
        row = table.currentRow()
        if row < 0:
            return None, None
        equip_id = self._linha_para_id(table, row)
        tag = table.item(row, 1).text() if table.item(row, 1) else ""
        nome = table.item(row, 2).text() if table.item(row, 2) else ""
        label = f"{tag} - {nome}".strip(" - ")
        return equip_id, label

    # ============================ CADASTRO ============================
    def _clear_main_fields(self):
        mv = self.main_view
        try: mv.input_tag.clear()
        except: pass
        try: mv.input_name.clear()
        except: pass
        try: mv.input_desc.clear()
        except: pass
        try: mv.input_cliente.clear()
        except: pass
        try: mv.input_modelo.clear()
        except: pass
        try: mv.input_serial.clear()
        except: pass
        try: mv.input_observacoes.clear()
        except: pass
        try: mv.combo_tipo_servico.setCurrentIndex(0)
        except: pass
        try: mv.combo_status.setCurrentIndex(0)
        except: pass
        try: mv.combo_prioridade.setCurrentIndex(0)
        except: pass
        try: mv.input_custo.setValue(0.0)
        except: pass
        try: mv.input_garantia_meses.setValue(0)
        except: pass
        try: mv.date_proxima.setDate(QDate.currentDate())
        except: pass

    def adicionar_equipamento(self):
        mv = self.main_view
        tag = (mv.input_tag.text() or '').strip()
        nome = (mv.input_name.text() or '').strip()
        if not tag or not nome:
            self._msg_erro("Campos obrigatórios", "Informe ao menos Tag e Nome.")
            return
        try:
            equip_id = self.model.adicionar_equipamento(
                tag=tag, nome=nome,
                descricao=(mv.input_desc.toPlainText() or ""),
                cliente=(mv.input_cliente.text() or ""),
                modelo=(mv.input_modelo.text() or ""),
                serial=(mv.input_serial.text() or ""),
                tipo_servico=mv.combo_tipo_servico.currentText(),
                status=mv.combo_status.currentText(),
                prioridade=mv.combo_prioridade.currentText(),
                proxima_manutencao=mv.date_proxima.date().toString("yyyy-MM-dd"),
                custo=float(mv.input_custo.value()),
                garantia_meses=int(mv.input_garantia_meses.value()),
                observacoes=(mv.input_observacoes.toPlainText() or ""),
            )
            self._msg_info("Sucesso", f"Equipamento cadastrado (ID {equip_id}).")
            self._clear_main_fields()
        except Exception as e:
            self._msg_erro("Erro", f"Falha ao cadastrar: {e}")

    # ============================ CONSULTA ============================
    def mostrar_consulta(self):
        
        self.stacked_widget.setCurrentIndex(2)
        try:
            t = self.consulta_view.table_resultados
            t.setRowCount(0)
        except Exception:
            pass
        try:
            self.consulta_view.lbl_count.setText('0 resultados')
        except Exception:
            pass


    def _consulta_limpar(self):
        
        v = self.consulta_view
        try:
            v.input_termo.clear()
            v.combo_status.setCurrentIndex(0)
            v.combo_prioridade.setCurrentIndex(0)
            from PyQt5.QtCore import QDate
            if hasattr(v, 'date_ini'):
                v.date_ini.setDate(QDate.currentDate().addMonths(-1))
            if hasattr(v, 'date_fim'):
                v.date_fim.setDate(QDate.currentDate())
        except Exception:
            pass
        # Não buscar automaticamente: apenas limpar a tabela e contador
        try:
            t = v.table_resultados
            t.setRowCount(0)
        except Exception:
            pass
        try:
            v.lbl_count.setText('0 resultados')
        except Exception:
            pass


    def _consulta_buscar(self):
        v = self.consulta_view
        rows = self.model.consultar(
            termo=(v.input_termo.text() or '').strip(),
            status=v.combo_status.currentText(),
            prioridade=v.combo_prioridade.currentText(),
            prox_ini=v.date_ini.date().toString('yyyy-MM-dd') if hasattr(v,'date_ini') else None,
            prox_fim=v.date_fim.date().toString('yyyy-MM-dd') if hasattr(v,'date_fim') else None,
        )
        t = v.table_resultados
        t.setRowCount(0)
        for r in rows:
            i = t.rowCount(); t.insertRow(i)
            # Consulta tem 11 colunas: 0..10
            for col, val in enumerate([r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]]):
                t.setItem(i, col, QTableWidgetItem(str(val or '')))
        try:
            v.lbl_count.setText(f"{t.rowCount()} resultados")
        except:
            pass

    def _abrir_detalhe_selecionado(self):
        t = self.consulta_view.table_resultados
        row = t.currentRow()
        if row < 0:
            return
        equip_id = self._linha_para_id(t, row)
        rec = self.model.obter_por_id(equip_id)
        if not rec:
            return
        dlg = DetalheView(self.stacked_widget)
        dlg.load_from_record(rec)
        if dlg.exec_():
            vals = dlg.values()
            self.model.atualizar(equip_id, **vals)
            self._consulta_buscar()

    def _excluir_selecionado(self):
        t = self.consulta_view.table_resultados
        row = t.currentRow()
        if row < 0: return
        equip_id = self._linha_para_id(t, row)
        if not equip_id: return
        if QMessageBox.question(self.stacked_widget, "Confirmar", "Excluir este equipamento?") == QMessageBox.Yes:
            if self.model.excluir_equipamento(equip_id):
                self._consulta_buscar()

    def _novo_servico_consulta(self):
        t = self.consulta_view.table_resultados
        equip_id, label = self._selected_equipment_from_table(t)
        if not equip_id:
            self._msg_erro("Seleção necessária", "Selecione um equipamento na lista.")
            return
        dlg = ServiceDialog(self.stacked_widget, equip_label=label)
        if dlg.exec_():
            vals = dlg.values()
            self.model.adicionar_servico(equip_id, **vals)
            self._msg_info("Registrado", "Serviço adicionado ao histórico.")

    # ============================ HISTÓRICO ============================
    def mostrar_historico(self):
        
        self.stacked_widget.setCurrentIndex(3)
        try:
            t = self.historico_view.table_historico
            t.setRowCount(0)
        except Exception:
            pass
        try:
            self.historico_view.lbl_count_h.setText('0 resultados')
        except Exception:
            pass


    def _abrir_detalhe_selecionado_hist(self):
        t = self.historico_view.table_historico
        row = t.currentRow()
        if row < 0: return
        equip_id = self._linha_para_id(t, row)
        if not equip_id: return
        rec = self.model.obter_por_id(equip_id)
        if not rec: return
        dlg = DetalheView(self.stacked_widget)
        dlg.load_from_record(rec)
        if dlg.exec_():
            vals = dlg.values()
            self.model.atualizar(equip_id, **vals)
            self.mostrar_historico()

    def _excluir_selecionado_hist(self):
        t = self.historico_view.table_historico
        row = t.currentRow()
        if row < 0: return
        equip_id = self._linha_para_id(t, row)
        if not equip_id: return
        if QMessageBox.question(self.stacked_widget, "Confirmar", "Excluir este equipamento?") == QMessageBox.Yes:
            if self.model.excluir_equipamento(equip_id):
                self.mostrar_historico()

    def _novo_servico_historico(self):
        t = self.historico_view.table_historico
        equip_id, label = self._selected_equipment_from_table(t)
        if not equip_id:
            self._msg_erro("Seleção necessária", "Selecione um equipamento na lista.")
            return
        dlg = ServiceDialog(self.stacked_widget, equip_label=label)
        if dlg.exec_():
            vals = dlg.values()
            self.model.adicionar_servico(equip_id, **vals)
            self._msg_info("Registrado", "Serviço adicionado ao histórico.")

    def _mostrar_historico_do_selecionado(self, origem='consulta'):
        t = self.consulta_view.table_resultados if origem == 'consulta' else self.historico_view.table_historico
        equip_id, label = self._selected_equipment_from_table(t)
        if not equip_id:
            self._msg_erro("Seleção necessária", "Selecione um equipamento.")
            return
        rows = self.model.listar_servicos_por_equipamento(equip_id)
        dlg = ServiceHistoryDialog(self.stacked_widget, equip_label=label, rows=rows)
        dlg.exec_()

    def _historico_limpar(self):
        
        try:
            self.historico_view.input_termo_h.clear()
            self.historico_view.combo_status_h.setCurrentIndex(0)
            self.historico_view.combo_prioridade_h.setCurrentIndex(0)
            from PyQt5.QtCore import QDate
            if hasattr(self.historico_view, 'date_ini_h'):
                self.historico_view.date_ini_h.setDate(QDate.currentDate().addMonths(-1))
            if hasattr(self.historico_view, 'date_fim_h'):
                self.historico_view.date_fim_h.setDate(QDate.currentDate())
        except Exception:
            pass
        # Não buscar automaticamente: apenas limpar a tabela e contador
        try:
            t = self.historico_view.table_historico
            t.setRowCount(0)
        except Exception:
            pass
        try:
            self.historico_view.lbl_count_h.setText('0 resultados')
        except Exception:
            pass


    def _historico_buscar(self):
        h = self.historico_view
        rows = self.model.consultar(
            termo=(h.input_termo_h.text() or '').strip() if hasattr(h, 'input_termo_h') else None,
            status=h.combo_status_h.currentText() if hasattr(h, 'combo_status_h') else None,
            prioridade=h.combo_prioridade_h.currentText() if hasattr(h, 'combo_prioridade_h') else None,
            prox_ini=self._date_str_safe(h.date_ini_h) if hasattr(h, 'date_ini_h') else None,
            prox_fim=self._date_str_safe(h.date_fim_h) if hasattr(h, 'date_fim_h') else None,
        )
        t = h.table_historico
        t.setRowCount(0)
        for r in rows:
            i = t.rowCount(); t.insertRow(i)
            for col, val in enumerate([r[0], r[1], r[2], r[3], r[4], r[7], r[8], r[9], r[10]]):
                t.setItem(i, col, QTableWidgetItem(str(val or '')))
        try:
            h.lbl_count_h.setText(f"{t.rowCount()} resultados")
        except Exception:
            pass

    # ============================ NAVEGAÇÃO ============================
    def voltar(self):
        self.stacked_widget.setCurrentIndex(0)

    def sair(self):
        res = QMessageBox.question(self.main_view, "Sair", "Deseja realmente sair?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if res == QMessageBox.Yes:
            QApplication.instance().quit()
