from string_manipulator import StringManipulator  
  
  
def test_convert_lower_case():  
    sm = StringManipulator()  
    res = sm.to_lower_case("PYTEST")  
    assert res == "pytest"  
  
  
def test_convert_lower_case_input_type_int():  
    sm = StringManipulator()  
    res = sm.to_lower_case(123)  
    assert res == "Invalid input"

def test_convert_lower_case_input_type_bool():  
    sm = StringManipulator()  
    res = sm.to_lower_case(True)  
    assert res == "Invalid input"

def test_convert_lower_case_empty_string():  
    sm = StringManipulator()  
    res = sm.to_lower_case("")  
    assert res == "String is empty"
