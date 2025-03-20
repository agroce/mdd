class StringManipulator:  
    def to_lower_case(self, my_string: str):  
        if not my_string:  
            return "String is empty"  
        if not isinstance(my_string, str):  
            return "Invalid input"  
        return my_string.lower()
