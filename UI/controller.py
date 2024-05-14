import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCalcola(self, e):
        anno =  int(self._view._txtAnno.value)
        if 1816 <= anno <= 2016 :
            self._model.creaGrafo(self._view._txtAnno.value)
        else:
            self._view.create_alert("L'anno inserito è scorretto.")
            return
        num = self._model.contaConnessioni()
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {num} componenti connesse."))
        for country in self._model.grafo.nodes:
            self._view._txt_result.controls.append(ft.Text(f"{country.StateNme}"
                                                           f"{self._model.contaViciniNodo(country)} vicini."))
        self._view.update_page()
