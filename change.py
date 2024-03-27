class Change:
    current_number = 1

    def __init__(self, content):
        self.number = Change.current_number
        self.content = content
        Change.current_number += 1
        self.validate_content()

    def validate_content(self):
        raise NotImplementedError("")

class add(Change):
    def __init__(self, content):
        super().__init__(content) #ovo ne treba jer nasledjuje i ne menja nista
    def validate_content(self):
        if not isinstance(self.content, str):
            raise ValueError("mora da bude string")             #ne mogu ti karakteri?

class delete(Change):
    def __init__(self):
        super().__init__( None)
    def validate_content(self):
        if self.content is not None:
            raise ValueError("kontent mora da bude None")

class modifikacija(Change):
    def __init__(self, content):
        super().__init__(content)
    def validate_content(self):
        if not isinstance(self.content, str):
            raise ValueError("kontent mora da bude string")

#apply change?