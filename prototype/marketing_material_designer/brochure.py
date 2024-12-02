from marketing_material import MarketingMaterial

# Concrete class implementing clone_marketing_material method
class Brochure(MarketingMaterial):
    def __init__(self, layout, content, color):
        super().__init__(layout, content, color)

    # Implementing the abstract method for Brochure
    def clone_marketing_material(self):
        return Brochure(self.layout, self.content, self.color)