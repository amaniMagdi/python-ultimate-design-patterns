from marketing_material import MarketingMaterial

# Concrete class implementing clone_marketing_material method
class Flyer(MarketingMaterial):
    def __init__(self, layout, content, color):
        super().__init__(layout, content, color)

     # Implementing the abstract method for Flyer
    def clone_marketing_material(self):
        print("Cloning Flyer")
        return Flyer(self.layout, self.content, self.color)
