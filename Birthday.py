from datetime import datetime

from Field import Field
DATE_FORMAT = "%d.%m.%Y"


class Birthday(Field):
    
    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
        return f'{self.value.strftime(DATE_FORMAT)}'
