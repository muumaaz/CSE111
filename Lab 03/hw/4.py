#4
import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(f'Vector <{self.x}, {self.y}, {self.z}> has been created.')

        self.magnitude = math.sqrt(self.x**2 + self.y**2 + self.z**2)
# Write your driver code here
v1 = Vector3D(2, -3, 1)
v2 = Vector3D(-1, 4, 0)
v1.magnitude = math.sqrt(v1.x**2 + v1.y**2 + v1.z**2)
v2.magnitude = math.sqrt(v2.x**2 + v2.y**2 + v2.z**2)
print(f"Magnitude of the first vector = {v1.magnitude}")
print(f"Magnitude of the second vector = {v2.magnitude}")
dot = v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
print(f"Dot product of the two vectors = {dot}")
cross = {'x' : v1.y*v2.z - v1.z*v2.y,
         'y' : v1.z*v2.x - v1.x*v2.z,
         'z' : v1.x*v2.y - v1.y*v2.x}
v3 = Vector3D(cross['x'], cross['y'], cross['z'])
print(f"Cross product of the two vectors = <{cross['x']}, {cross['y']}, {cross['z']}>")