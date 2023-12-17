# Implementing Inheritance Feature

# class Polygon:
#     def __init__(self,sides):
#         self.s=sides
    
#     def get_sides(self):
#         sides=[input(f"Enter the side {i+1}: ") for i in range(self.s)]
#         return sides
    
    
# class triangle(Polygon):
#     def __init__(self):
#         super().__init__(3)
#         asd=super.get_sides()
        
  
#     def perimeter(self):
#         a,b,c=self.asd
#         print(f'Perimter of the triangle is {a+b +c}')
        
        
# a=triangle()
# print(a.perimeter())
    
    
class Polygon:
    def __init__(self, sides):
        self.s = sides
    
    def get_sides(self):
        sides = [float(input(f"Enter the side {i+1}: ")) for i in range(self.s)]
        return sides
    
    def dis_sides(self):
        for i in range (len(self.sides)):
            print(f'Side {i+1} is:',self.sides[i])
     
    

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
        self.sides = super().get_sides()
  
    def perimeter(self):
        a, b, c = self.sides
        return f'Perimeter of the triangle is {a + b + c}'
        
        
a = Triangle()
a.dis_sides()
print(a.perimeter())
    