# circle challenge

class Circle:
    def __init__(self, radius = 1.0):
        
        self.radius = radius
        self.name = f'Circle radius: {self.radius}'
        self.perimeter = 2 * 3.1415926 * radius
        self.area = 3.1415926 * radius * radius
        self.definitions = 'perimeter = ' + str(self.perimeter) +' area = ' + str(self.area)


    # def perimeter(self):
    #     self.perimeter = 

    def area(self):
        print(self.area)
    
    def print_circles(self):
        print_thing = int(self.radius) * ' Circles are in the eye of the beholder \n Oval\'s are ovalrated. \n'
        #What is meant by something nice srs?
        #  
        print(print_thing)
    def add_circles(self,other):
        
        #super circle... 
        new_circle_radius = self.radius + other.radius
        new_circle = Circle(new_circle_radius)
        print(f'New circle info: {new_circle.definitions}')
        return new_circle

    def compare_circles(self, other):
        if self.radius > other.radius:
            print(f'{self} is bigger than {other} by {self.radius - other.radius}square meter(s)')
        elif self.radius < other.radius:
            print(f'{self.name} is smaller than {other.name} by {other.radius - self.radius}square meter(s)')
        else:
            print (f'{self.name} and {other.name} are are of equal size')

    def list_sort(self, *args):
        circle_list = [self]
        for circle in args:
            circle_list.append(circle)
        # circle_list.sort()
        circle_bank = []
        for circle in circle_list:
            circle_bank.append(repr(circle))
        
        # print(circle_bank)
        circle_bank.sort()
        print(circle_bank)
        # print(type(circle_bank[0]))
        # how are we supposed to sort this?

        

        # print(circle_list)
# need to tell it what to return when trying to print the object as a string
    def __repr__(self):
        return self.definitions
  


circle1 = Circle(10.0)
circle2 = Circle(10.0)
circle3 = Circle(15.0)
# print(circle1.area)
# print(circle2.area)

# circle2.print_circles()
# circle1.add_circles(circle2)
# circle1.compare_circles(circle2)
# circle2.compare_circles(circle3)

circle1.list_sort(circle3,circle2)
