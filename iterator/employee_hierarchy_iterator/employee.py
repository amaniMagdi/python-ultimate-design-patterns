class Employee:
    def __init__(self, employee_id, name):
        self._id = employee_id
        self._name = name

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, employee_id):
        self._id = employee_id

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        self._name = name
