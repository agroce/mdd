class StringManipulator:  
    def to_lower_case(self, my_string: str):  
        if not my_string:  
            return "String is empty"  
        if not isinstance(my_string, str):  
            return "Invalid input"  
        return my_string.lower()

    def remove_pattern(self, my_string: str, pattern: str):  
        if not my_string:  
            return "String is empty"  
        if not isinstance(my_string, str):  
            return "Invalid input"  
        new_string = my_string.replace(pattern, "")  
        return new_string
