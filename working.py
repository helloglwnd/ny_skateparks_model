class Skatepark:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.features = []
    
    def add_feature(self, feature):
        self.features.append(feature)
    
    def visualisation(self):
        print(f"Welcome to {self.name} Skatepark located in {self.location}:")
        print("Features available:")
        for feature in self.features:
            print(f"- {feature}")

# Example usage:
if __name__ == "__main__":
    park = Skatepark("Radical Skatepark", "City Center")
    park.add_feature("Half-pipe")
    park.add_feature("Rails and ramps")
    park.add_feature("Skate bowl")
    
    park.visualisation()