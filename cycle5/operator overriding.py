class rectangle:
    __area = 0
    __perimeter = 0
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

        def calc_area(self):
            self.__area = self.__length * self.__width
            print("Area is :", self.__area)

        def __lt__(self, second):
            if self.__area < second.__area:
                return True
            else:
                return False

    length1 = int(input("Enter length of the rectangle 1 : "))
    width1 = int(input("Enter width of the rectangle 1 : "))
    length2 = int(input("Enter length of the rectangle 2 : "))
    width2 = int(input("Enter width of the rectangle 2 : "))


    def __str__(self):
        return "({0},{1})".format(self.__length, self.__width)

        def __lt__(self, other):
            self_mag = (self.__length ** 2) + (self.__width ** 2)
            other_mag = (other.__length ** 2) + (other.width ** 2)
            return self_mag < other_mag

    obj1 = rectangle(1, 1)
    obj2 = rectangle(-2, -3)
    print(obj1 < obj2)
