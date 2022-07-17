# Automatically generated by Pynguin.
import pytest
import blood_sugar_algorithm as module_0

def test_case_0():
    blood_sugar_algorithm_0 = module_0.BloodSugarAlgorithm()
    assert blood_sugar_algorithm_0.patient is None
    assert blood_sugar_algorithm_0.hypoglycemia is None
    assert blood_sugar_algorithm_0.persistent_hypoglycemia is None
    assert blood_sugar_algorithm_0.abnormal_bs is None
    assert blood_sugar_algorithm_0.emergency_alarm is None
    assert blood_sugar_algorithm_0.bs_type is None
    assert blood_sugar_algorithm_0.new_measurement_required is None
    assert blood_sugar_algorithm_0.new_measurement_duration_min is None
    assert blood_sugar_algorithm_0.graphic_asset is None
    assert blood_sugar_algorithm_0.message_list == []
    assert blood_sugar_algorithm_0.last_bs is None
    assert module_0.SPACE == ' '

@pytest.mark.xfail
def test_case_1():
    int_0 = -2035
    str_0 = ',-x1kM'
    none_type_0 = None
    blood_sugar_0 = module_0.BloodSugar(int_0, int_0, str_0, none_type_0)
    assert blood_sugar_0.blood_sugar == -2035
    assert blood_sugar_0.temperature == -2035
    assert blood_sugar_0.measure_state == ',-x1kM'
    assert blood_sugar_0.measure_time is None
    assert module_0.SPACE == ' '
    blood_sugar_algorithm_0 = module_0.BloodSugarAlgorithm()
    assert blood_sugar_algorithm_0.patient is None
    assert blood_sugar_algorithm_0.hypoglycemia is None
    assert blood_sugar_algorithm_0.persistent_hypoglycemia is None
    assert blood_sugar_algorithm_0.abnormal_bs is None
    assert blood_sugar_algorithm_0.emergency_alarm is None
    assert blood_sugar_algorithm_0.bs_type is None
    assert blood_sugar_algorithm_0.new_measurement_required is None
    assert blood_sugar_algorithm_0.new_measurement_duration_min is None
    assert blood_sugar_algorithm_0.graphic_asset is None
    assert blood_sugar_algorithm_0.message_list == []
    assert blood_sugar_algorithm_0.last_bs is None
    blood_sugar_algorithm_1 = module_0.BloodSugarAlgorithm()
    assert blood_sugar_algorithm_1.patient is None
    assert blood_sugar_algorithm_1.hypoglycemia is None
    assert blood_sugar_algorithm_1.persistent_hypoglycemia is None
    assert blood_sugar_algorithm_1.abnormal_bs is None
    assert blood_sugar_algorithm_1.emergency_alarm is None
    assert blood_sugar_algorithm_1.bs_type is None
    assert blood_sugar_algorithm_1.new_measurement_required is None
    assert blood_sugar_algorithm_1.new_measurement_duration_min is None
    assert blood_sugar_algorithm_1.graphic_asset is None
    assert blood_sugar_algorithm_1.message_list == []
    assert blood_sugar_algorithm_1.last_bs is None
    bool_0 = False
    bool_1 = False
    blood_sugar_algorithm_0.set_patient_medical_record(bool_0, bool_1)

@pytest.mark.xfail
def test_case_2():
    int_0 = -399
    int_1 = 1487
    str_0 = '&\x0be)'
    none_type_0 = None
    blood_sugar_0 = module_0.BloodSugar(int_1, int_0, str_0, none_type_0)
    assert blood_sugar_0.blood_sugar == 1487
    assert blood_sugar_0.temperature == -399
    assert blood_sugar_0.measure_state == '&\x0be)'
    assert blood_sugar_0.measure_time is None
    assert module_0.SPACE == ' '
    blood_sugar_algorithm_0 = module_0.BloodSugarAlgorithm()
    assert blood_sugar_algorithm_0.patient is None
    assert blood_sugar_algorithm_0.hypoglycemia is None
    assert blood_sugar_algorithm_0.persistent_hypoglycemia is None
    assert blood_sugar_algorithm_0.abnormal_bs is None
    assert blood_sugar_algorithm_0.emergency_alarm is None
    assert blood_sugar_algorithm_0.bs_type is None
    assert blood_sugar_algorithm_0.new_measurement_required is None
    assert blood_sugar_algorithm_0.new_measurement_duration_min is None
    assert blood_sugar_algorithm_0.graphic_asset is None
    assert blood_sugar_algorithm_0.message_list == []
    assert blood_sugar_algorithm_0.last_bs is None
    blood_sugar_algorithm_0.init_data(blood_sugar_0)