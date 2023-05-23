class FiveDigitConverter:
    
    regex = '[0-9]{5}'

    # convert the string parameter into an integer

    def to_python(self, value):
        return int(value)

    def to_url (self, value):
        return '%04d'  % value