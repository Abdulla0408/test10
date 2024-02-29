class Triangle:
    def __init__(self,file_path:str):
        self.file = open(f"{file_path}.csv")

    def get_perimetr(self):
        import csv
        reader = csv.reader(self.file)
        for side in reader:
            a,b,c = side
            print(int(a) + int(b) + int(c))
            

    def __dell__(self):
        self.file.close()
        del self.file

triangle1 = Triangle("triangle")
triangle1.get_perimetr()

# ---------------------------------------------------------------------
#  __bool__ method

# print(bool("olma">"behi"))

# class Triangle:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c


#     def get_perimetr(self):
#         return int((self.a + self.b + self.c))

#     def __bool__(self):
#         return int(self.a) == int(self.b) == int(self.c)

# triangle_perimetr = []     
# with open("triangle.csv") as file:
#     import csv
#     reader = csv.reader(file)

    
#     for sides in reader:
#         a, b, c = sides
#         if Triangle(a,b,c):
#             print(a,b,c)
#             triangle_perimetr.append(Triangle(a,b,c).get_perimetr())

# ----------------------------------------------------------------------------------------------------
# __eq__ methods - Tenglikka tekshiradi " "
# __ne__ methods - Teng emaslikka tekshiradi " != "
# __lt__ methods - Kichikka tekshiradi " < "
# __le__ methods - Kichik yoki tenglikka tekshiradi " <= "


# try:
#     print(n)
# except:
#     print("except")

# def test(number):
#     try:
#         return number + 2
#     except:
#         return "Harf"


# class ClcLtion:
    
#     @staticmethod
#     def add(x, y):
#         return x + y
    
# print(ClcLtion)