from marketing_material import MarketingMaterial

# Concrete class implementing clone_marketing_material method
class Poster(MarketingMaterial):
    def __init__(self, layout, content, color):
        super().__init__(layout, content, color)

    # Implementing the abstract method for Poster
    def clone_marketing_material(self):
        return Poster(self.layout, self.content, self.color)
