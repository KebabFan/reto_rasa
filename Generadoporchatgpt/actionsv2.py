import pandas as pd
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAnulacion(Action):
    def name(self) -> Text:
        return "action_anulacion"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_anulacion")
        return []

class ActionCertificados(Action):
    def name(self) -> Text:
        return "action_certificados"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_certificados")
        return []

class ActionHorarioClases(Action):
    def name(self) -> Text:
        return "action_horario_clases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_horario_clases_manana")
        return []

class ActionFamiliasProfesionales(Action):
    def name(self) -> Text:
        return "action_familias_profesionales"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_familias_profesionales")
        return []

class ActionMatricula(Action):
    def name(self) -> Text:
        return "action_matricula"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_matricula")
        return []

class ActionInformacionAdicionalMatricula(Action):
    def name(self) -> Text:
        return "action_informacion_adicional_matricula"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_informacion_adicional_matricula")
        return []

class ActionBecas(Action):
    def name(self) -> Text:
        return "action_becas"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_becas")
        return []

class ActionInformacionAdicionalBecas(Action):
    def name(self) -> Text:
        return "action_informacion_adicional_becas"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_informacion_adicional_becas")
        return []

class ActionRequisitosAcceso(Action):
    def name(self) -> Text:
        return "action_requisitos_acceso"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_requisitos_acceso")
        return []

class ActionInformacionAdicionalRequisitos(Action):
    def name(self) -> Text:
        return "action_informacion_adicional_requisitos"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_informacion_adicional_requisitos")
        return []

class ActionInformacionInformatica(Action):
    def name(self) -> Text:
        return "action_informacion_informatica"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Leer el archivo CSV de grupos
        grupos_df = pd.read_csv("Grupos.csv")

        # Leer el archivo CSV de módulos
        modulos_df = pd.read_csv("Modulos.csv")

        # Combinar la información de grupos y módulos en un mensaje
        informacion = "La oferta de informática es la siguiente:\n"
        for index, row in grupos_df.iterrows():
            informacion += f"Grupo: {row['Grupo']}, Turno: {row['Turno']}, Nombre: {row['Nombre']}\n"
            informacion += "Módulos:\n"
            modulos_grupo = modulos_df[modulos_df['Grupo'] == row['Grupo']]
            for _, mod_row in modulos_grupo.iterrows():
                informacion += f"- {mod_row['Nom_Cas_Modulo']}\n"
        
        dispatcher.utter_message(text=informacion)
        return []

class ActionDetallesCicloInformatica(Action):
    def name(self) -> Text:
        return "action_detalles_ciclo_informatica"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_detalles_ciclo_informatica")
        return []

class ActionAsignaturasCicloInformatica(Action):
    def name(self) -> Text:
        return "action_asignaturas_ciclo_informatica"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any
