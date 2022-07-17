import array
from typing import Optional
from datetime import timedelta, datetime
from typing import List

import queue
import abstract_algorithm
from models import BloodSugarAlgorithmRunInfo
import enums

from enums import BS_Scenario_Ids, Algorithm_Category
from exceptions import PropertyUnavailable

SPACE = " "

class BloodSugar():
    def __init__(self, bs: int, temperature: int, m_state: str, m_time: datetime):
        self.blood_sugar = bs
        self.temperature = temperature
        self.measure_state = m_state
        self.measure_time = m_time


class BloodSugarAlgorithm(abstract_algorithm.Algorithm):
    def __init__(self):
        self.patient = None
        self.hypoglycemia = None
        self.persistent_hypoglycemia = None
        self.abnormal_bs = None
        self.emergency_alarm = None
        self.bs_type = None
        self.new_measurement_required = None
        self.new_measurement_duration_min = None
        self.graphic_asset = None
        self.message_list: List[Message] = list()
        self.__messages = None
        self.last_bs = None

    def set_prev_bs_info(prev_bs: int, prev_mtime: datetime, prev_bs_typ: str) -> bool:
        self.prev_bs = BloodSugar(prev_bs, 32, prev_bs_typ, prev_mtime)
        return True

    def set_patient_medical_record(diab_typ1: bool, diab_typ2: bool) -> bool:
        if diab_typ1:
            self.diabetes_type_1 = diab_typ1
        else:
            self.diabetes_type_2 = diab_typ2
        return True

    def init_data(self, input_bs: BloodSugar ) -> bool:
        self.emergency_alarm = False
        self.last_bs = input_bs
        self.bs_type = self.last_bs.measure_state
        self.abnormal_bs = False
        self.__messages = {
            enums.BS_Scenario_Ids.SCBSN001: _(
                "low blood sugar and another measurement required"
            ),
            enums.BS_Scenario_Ids.SCBSN002: _(
                "low blood sugar at second measurment and emergency support may needed"
            ),
            enums.BS_Scenario_Ids.SCBSN003: _("high blood sugar and emergency action needed"),
            enums.BS_Scenario_Ids.SCBSN004: _(
                "high random blood sugar and no emergency action needed"
            ),
            enums.BS_Scenario_Ids.SCBSN005: _("normal random blood sugar"),
            enums.BS_Scenario_Ids.SCBSN006: _(
                "fasten blood sugar is above 125 and no emergency action needed"
            ),
            enums.BS_Scenario_Ids.SCBSN007: _(
                "fasten blood sugar is between 110 and 125 and no emergency action needed"
            ),
            enums.BS_Scenario_Ids.SCBSN008: _("normal fasten blood sugar"),
            enums.BS_Scenario_Ids.SCBSN009: _(
                "high two hours blood sugar and no emergency action needed"
            ),
            enums.BS_Scenario_Ids.SCBSN010: _("normal two hours blood sugar"),
            enums.BS_Scenario_Ids.SCBSN011: _(
                "high random blood sugar for user with diabetes history but no emergency action needed"
            ),
            enums.BS_Scenario_Ids.SCBSN012: _(
                "normal random blood sugar for user with diabetes history"
            ),
            enums.BS_Scenario_Ids.SCBSN013: _(
                "high fasten blood sugar for user with diabetes history but no emergency action needed"
            ),
            enums.BS_Scenario_Ids.SCBSN014: _(
                "normal fasten blood sugar for user with diabetes history"
            ),
            enums.BS_Scenario_Ids.SCBSN015: _(
                "low fasten blood sugar for user with diabetes history but no emergency action needed"
            ),
            enums.BS_Scenario_Ids.SCBSN016: _(
                "high two hours blood sugar for user with diabetes history but no emergency action needed"
            ),
            enums.BS_Scenario_Ids.SCBSN017: _(
                "normal two hours blood sugar for user with diabetes history"
            ),
            enums.BS_Scenario_Ids.SCBSN018: _(
                "low fasten blood sugar for user with diabetes history but no emergency action needed"
            ),
        }
        return True


    def run(self, send_message=False) -> str:
        scenario = BS_Scenario_Ids.SCBSN001
        if self.last_bs.blood_sugar < 60:
            if hasattr(self, "prev_bs"):
                if self.prev_bs.blood_sugar < 60:
                    scenario = BS_Scenario_Ids.SCBSN002
                    self.persistent_hypoglycemia = True
                    self.abnormal_bs = True
                    self.emergency_alarm = True
                    self.graphic_asset = SAD_SINACARE
                    message = self.__messages[scenario]
            else:
                self.emergency_alarm = True
                self.hypoglycemia = True
                self.new_measurement_required = True
                self.new_measurement_duration_min = 20
                self.graphic_asset = POKER_SINACARE
                message = self.__messages[scenario]
        elif self.last_bs.blood_sugar >= 250:
            scenario = BS_Scenario_Ids.SCBSN003
            self.emergency_alarm = True
            self.abnormal_bs = True
            self.graphic_asset = SAD_SINACARE
            message = self.__messages[scenario]
        elif self.diabetes_type_2 or self.diabetes_type_1:
            if self.bs_type == "RBS":
                if self.last_bs.blood_sugar >= 200:
                    scenario = BS_Scenario_Ids.SCBSN011
                    self.abnormal_bs = True
                    self.graphic_asset = POKER_SINACARE
                    message = self.__messages[scenario]
                else:
                    scenario = BS_Scenario_Ids.SCBSN012
                    self.graphic_asset = EXCELLENT_SINACARE
                    message = self.__messages[scenario]
            elif self.bs_type == "FBS":
                if self.last_bs.blood_sugar > 130:
                    scenario = BS_Scenario_Ids.SCBSN013
                    self.abnormal_bs = True
                    self.graphic_asset = POKER_SINACARE
                    message = self.__messages[scenario]
                elif 80 <= self.last_bs.blood_sugar <= 130:
                    scenario = BS_Scenario_Ids.SCBSN014
                    self.graphic_asset = EXCELLENT_SINACARE
                    message = self.__messages[scenario]
                elif 70 <= self.last_bs.blood_sugar < 80:
                    scenario = BS_Scenario_Ids.SCBSN018
                    self.abnormal_bs = True
                    self.graphic_asset = POKER_SINACARE
                    self.hypoglycemia = True
                    message = self.__messages[scenario]
                else:
                    scenario = BS_Scenario_Ids.SCBSN015
                    self.abnormal_bs = True
                    self.hypoglycemia = True
                    self.graphic_asset = POKER_SINACARE
                    message = self.__messages[scenario]
            elif self.bs_type in ["PBS", "PLS", "PDS"]:
                if self.last_bs.blood_sugar >= 180:
                    scenario = BS_Scenario_Ids.SCBSN016
                    self.abnormal_bs = True
                    self.graphic_asset = POKER_SINACARE
                    message = self.__messages[scenario]
                else:
                    scenario = BS_Scenario_Ids.SCBSN017
                    self.graphic_asset = EXCELLENT_SINACARE
                    message = self.__messages[scenario]
            else:
                raise PropertyUnavailable(property=_("bs_type"))
        else:
            if self.bs_type == "RBS":
                if self.last_bs.blood_sugar >= 200:
                    scenario = BS_Scenario_Ids.SCBSN004
                    self.abnormal_bs = True
                    self.graphic_asset = POKER_SINACARE
                    message = self.__messages[scenario]
                else:
                    scenario = BS_Scenario_Ids.SCBSN005
                    self.graphic_asset = EXCELLENT_SINACARE
                    message = self.__messages[scenario]
            elif self.bs_type == "FBS":
                if self.last_bs.blood_sugar >= 125:
                    scenario = BS_Scenario_Ids.SCBSN006
                    self.abnormal_bs = True
                    self.graphic_asset = POKER_SINACARE
                    message = self.__messages[scenario]
                elif 100 <= self.last_bs.blood_sugar < 125:
                    scenario = BS_Scenario_Ids.SCBSN007
                    self.abnormal_bs = True
                    self.graphic_asset = POKER_SINACARE
                    message = self.__messages[scenario]
                else:
                    scenario = BS_Scenario_Ids.SCBSN008
                    self.graphic_asset = EXCELLENT_SINACARE
                    message = self.__messages[scenario]
            elif self.bs_type in ["PBS", "PLS", "PDS"]:
                if self.last_bs.blood_sugar >= 200:
                    scenario = BS_Scenario_Ids.SCBSN009
                    self.abnormal_bs = True
                    self.graphic_asset = POKER_SINACARE
                    message = self.__messages[scenario]
                else:
                    scenario = BS_Scenario_Ids.SCBSN010
                    self.graphic_asset = EXCELLENT_SINACARE
                    message = self.__messages[scenario]
        if send_message:
            self.append_message_to_healthcare_support(scenario)
            self.append_message_to_emergency_contact(scenario)
        return self.patient.user_profile.user.first_name + SPACE + message
            

    

