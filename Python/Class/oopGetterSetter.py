class Lecturer:
    def __init__(self, name, staff_id):
        # Assign through the property setters so any validation logic added
        # later will still run during object creation.
        self.name= name
        self.staff_id= staff_id
         
    # Expose _name like a normal attribute while keeping control internally.
    @property
    def name(self):
        return self._name
    
    # The setter updates the protected storage attribute used by the property.
    @name.setter
    def name(self, value):
        self._name = value
        
    # Same pattern for staff_id: public access, controlled internal storage.
    @property
    def staff_id(self):
        return self._staff_id
    
    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value
        
# Create two Lecturer objects.
lecturer1=Lecturer("Okesola", "001")
lecturer2=Lecturer("Adebanjo", "002")

# Accessing the property calls the getter behind the scenes.
print(lecturer1.name)
        
# Updating the property calls the setter, not the internal attribute directly.
lecturer1.name="Ade"
print(lecturer1.name)
print(lecturer2.name)
    
