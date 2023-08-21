class TwoDVector:
    def __init__(self, x, y): 
        self.__x = x
        self.__y = y

    # Setter and Getter Methods for x & y
    def setX(self, x):
        self.__x = x
    def getX(self):
        return self.__x
    def setY(self, y):
        self.__y = y
    def getY(self):
        return self.__y
    
    def add2DVectors(self, *vectors):
        for i in vectors:
            self.setX(self.getX() + i.getX())
            self.setY(self.getY() + i.getY())

    def print2DVector(self):
        if self.getY() >= 0:
            y = "+ "+str(self.getY())    
        else:
            y = str(self.getY)
        print(f"{self.getX()}i {y}j")

class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    def setZ(self, z):
        self.__z = z
    def getZ(self):
        return self.__z
    
    def add3DVectors(self, *vectors):
        for i in vectors:
            self.setX(self.getX() + i.getX())
            self.setY(self.getY() + i.getY())
            self.setZ(self.getZ() + i.getZ())



TwoDV1 = TwoDVector(5, 6)
TwoDV2 = TwoDVector(3, 7)
TwoDV3 = TwoDVector(1, 8)
print("===============")
TwoDV1.add2DVectors(TwoDV2, TwoDV3)
TwoDV1.print2DVector()
print("===============")
ThreeDV1 = ThreeDVector(5, 6, 1)
ThreeDV2 = ThreeDVector(1, 9, -7)
ThreeDV3 = ThreeDVector(8, 2, 4)
print("===============")
ThreeDV1.add3DVectors(ThreeDV2,ThreeDV3)
ThreeDV1.print3DVector()
print("===============")
ThreeDV1.multiplyScalar(3)
ThreeDV1.print3DVector()
print("===============")
print(ThreeDV1.calculateLength())