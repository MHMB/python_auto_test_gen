from datetime import timedelta, datetime

LABEL_OPTIONS = [(0, "Sinacare"), (1, "Mamania")]
HTN_STATUS = [
    (0, "No Information"),
    (1, "HTN Suspected"),
    (2, "Poor Controlled HTN Suspected"),
]
BS_MEASURE_TYPE = [(0, "Random"), (1, "Two Hour"), (2, "Fasting")]
MEASUREMENT_SITES = [
    (0, "axillary"),
    (1, "oral"),
    (2, "temporal"),
    (3, "rectal"),
    (4, "tympanic"),
]


class AlgorithmRunInfo():
    def __init__(self, p_name: str, p_id: int, requester: str, label: str) -> None:
        self.patient_id = p_id
        self.patient_name = p_name
        self.requester = requester
        self.label = label
        self.emergency = False
        self.abnormal = False
        self.age = None
        self.message = ""
        self.message_id = ""
        self.request_to_run_time = datetime.now()



class BloodSugarAlgorithmRunInfo(AlgorithmRunInfo):
    def __init__(self, p_name: str, p_id: int, requester: str, label: str, bs: int, m_time: datetime, prev_bs: int, lh_data: bool, prev_m_time: datetime, diab_typ1: bool, diab_typ2: bool, bs_m_typ: str, hypoglycemia: bool, persistant_hypogycemia: bool):
        super().__init__(p_name, p_id, requester, label)
        self.blood_sugar = bs
        self.measure_time = m_time
        self.previous_blood_sugar = prev_bs
        self.has_data_last_hour = lh_data
        self.previous_measure_time = prev_m_time
        self.diabetes_type_1 = diab_typ1
        self.diabetes_type_2 = diab_typ2
        self.blood_sugar_measurement_type = bs_m_typ
        self.hypoglycemia = hypoglycemia
        self.persistant_hypogycemia = persistant_hypogycemia


class BloodSugar():
    def __init__(self, bs: int, temperature: int, m_state: str, m_time: datetime):
        self.blood_sugar = bs
        self.temperature = temperature
        self.measure_state = m_state
        self.measure_time = m_time
        
