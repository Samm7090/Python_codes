class Bottel:
    material=""
    volume=0
    capType=""
    shape=""
    height=0.0
    size=0.0

    def assignBottelProperties(self):
        self.material=input("Enter the material name ")
        self.shape=input("Enter the shape: ")
        self.height=float(input("Enter the shape: "))
        self.size = float(input("Enter the size: "))
        self.capType = input("Enter the captype: ")

    def veiwBottelProperties(self):
        print("Bottle material is",self.material)
        print("Bottle shape is", self.shape)
        print("Bottle height is", self.height)
        print("Bottle size is", self.size)
        print("Bottle capType is", self.capType)
    def holdTheWater(self):
        print("This operation is to hold the water ")

    def maintainWaterTemperature(self):
        print("This operation is to maintain water temperature ")

