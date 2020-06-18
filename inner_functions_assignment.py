a_list = [2.1, 3.4]
b_list = [3.5]


def measurements(list):
    def area(list):
        area = list[0] * list[1]
        print("Area = " + str(area))

    def perimeter(list):
        perimeter = (list[0]*2) + (list[1]*2)
        print("Perimeter = " + str(perimeter))


    perimeter(a_list)
    area(a_list)


measurements(list)
