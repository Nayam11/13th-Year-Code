import math

def rect_a(l, b):
    a = l * b
    return a
    
def sq_a(s, d):
    space = s ** d
    return space



print("Hello! Tired of math homework and calculations! Well, worry not, because the Mathulator is finally here!")
print("You can calculate anything from logarithms, to simple additions. Just choose what you want to calculate from the list below,\n and I'll do it for you!")
dec = "---------------------------------------"
calcops = '''
  Addition, Subtraction, Multiplication, Division, Powers,
  Roots, Logarithm, Area, Volume, Force
  Mass, Factorial, Pressure '''


valid_options = ["Addition", "Subtraction", "Multiplication", "Division", "Powers","Power", "Roots",
                 "Root", "Logarithm", "Area", "Volume", "Force", "Mass", "Factorial", "Pressure"]
valid_options = [option.lower() for option in valid_options]

while True:
    usrcalc = input(calcops + "\nEnter your choice: ")
    usrcalc = usrcalc.lower()

    if usrcalc not in valid_options:
        print("Please enter an option from the options given above.")
        continue
    else:
        break

if usrcalc == "addition":
    addops = input("Great! What do you want to add? Two numbers? A whole set of numbers? Two equations?\nType Equations, Sets, or Numbers: ").lower()
    addops = addops.lower()
    if addops == "numbers" or addops == "no.s" or addops == "two numbers":
        nums = int(input("How many numbers do you want to add? "))
        sum = 0
        for i in range(nums):
            a = float(input("Enter a number: "))
            sum += a
        print(f"The sum is: {sum}")
    elif addops == "equations" or addops == "two equations" or addops == "equation" or addops == "some equations":
        eques = int(input("Equations with variables are not added. \nHow may equtions do you want to add?"))
        sum3 = 0
        for i in range(eques):
            eq = eval(input("Enter an equation"))
            sum3 += eq
        print("The sum is: ", sum3)
    elif addops == "number sets" or addops == "sets" or addops == "sets of numbers" or addops == "set of numbers":
        numsets = int(input("How may sets of numbers do you want to add?"))
        sum2 = 0
        for i in range(numsets):
            ns = eval(input("Enter a number set"))
            sum2 += ns
        print(f"The sum of your number set is this: {sum2}")
    else:
        print("Please enter either Equations, Sets, or Numbers! You may have done a typo.")


elif usrcalc == "Subtraction" or usrcalc == "subtraction" or usrcalc  == "minus":
    subopps = input("Amazing! Please remember, variables are not going to get calculated.\nDo you want to subtract a number from another?\nOr one statement from another?\nEnter Number or Statement respectively!")
    subopps = subopps.lower()
    if subopps == "numbers" or subopps == "a number" or subopps == "two numbers" or subopps == "number":
        chc = input("Do you want to subtract many numbers from each other?\nLike 345-45-4-1? Or just one number from one of them?\nLike 5-2? Type Many, or Two respectively:\n")
        chc = chc.lower()
        if chc == "many" or chc == "many numbers":
            print("Remember, 8-4-3 will be evaluated as 8-4 first, then that minus 3.")
            subs = input("Enter the set of numbers that want to subtract:\n")
            diff = eval(subs)
            print(f"{diff} is the difference of all your numbers!")


elif usrcalc == "multiplication" or usrcalc == "Multiplication" or usrcalc == "multiply":
    multops = input("Fantastic! Do you want to multiply two numbers,\n two statements like 2+3 and 5-4, or a whole set of numbers, like 2 * 3 * 4?\nType Numbers, STatements, or Sets respectively: ").lower()
    multops = multops.lower()
    if multops == "numbers" or multops == "two numbers" or multops == "number":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        product = num1 * num2
        print(f"The product is: {product}")
    elif multops == "statements" or multops == "two statements" or multops == "statement":
        stats = int(input("How many statements do you want to multiply?"))
        product1 = 1
        for i in range(stats):
            st = eval(input("Enter a statement"))
            product1 *= st
        print(f"The product of all your statements is this: {product1}")


    elif multops == "sets" or multops == "set of numbers" or multops == "number sets":
        numsets = int(input("How many sets of numbers do you want to multiply?"))
        product2 = 1
        for i in range(numsets):
            multns = eval(input("Enter a number set"))
            product2 *= multns
        print(f"The product of your number set is this: {product2}")
    else:
        print("Please enter either Sets or Numbers! You may have done a typo.")


elif usrcalc == "division" or usrcalc == "Division" or usrcalc == "divide":
    divops = input("Wonderful! Do you want to divide two numbers,\n two statements like 6+4 and 2+3, or a whole set of numbers, like 100 / 5 / 2?\nType Numbers, Statements, or Sets respectively: ").lower()
    divops = divops.lower()
    if divops == "numbers" or divops == "two numbers" or divops == "number":
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        quotient = num1 / num2
        print(f"The quotient is: {quotient}")
    elif divops == "statements" or divops == "two statements" or divops == "statement":
        stats = int(input("How many statements do you want to divide?"))
        quotient1 = None
        for i in range(stats):
            st = eval(input("Enter a statement"))
            if quotient1 is None:
                quotient1 = st
            else:
                quotient1 /= st
        print(f"The quotient of all your statements is this: {quotient1}")
    elif divops == "sets" or divops == "set of numbers" or divops == "number sets":
        set = eval(input("Enter the set of numbers you want to divide: "))
        print("The quotient of all the numbers in this set is: ", set)

    else:
        print("Please enter either Sets or Numbers! You may have done a typo.")


elif usrcalc == "powers" or usrcalc == "Powers" or usrcalc == "power" or usrcalc == "powers":
    chcp = input("Perfect! Do you want to calculate the power of a single number,\n nested powers like (2^3)^2, or of two sets, like 2+3 * 8-5?\nType Single, Nested, or Sets respectively: ").lower()
    chcp = chcp.lower()
    if chcp == "Single" or chcp == "single" or chcp == "one number" or chcp == "number":
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent: "))
        result = base ** exponent
        print(f"{base} raised to the power of {exponent} is: {result}")

    elif chcp == "nested" or chcp == "powers in powers" or chcp == "nested powers":
        nests = int(input("How many nests are there? Like (2^3)^2 has 2 nests,\nand ((2^3)^2)^4 has 3 nests: "))
        result1 = eval(input("Enter the first nested power: "))
        for i in range(nests - 1):
            np = eval(input("Enter the next nested power: "))
            result1 **= np
        print(f"The result of your nested powers is: {result1}")

    elif chcp == "sets" or chcp == "set of numbers" or chcp == "number sets":
        numsets = int(input("How many sets of numbers do you want to calculate powers for? "))
        result2 = eval(input("Enter the first set: "))
        for i in range(numsets - 1):
            pows = eval(input("Enter the next set: "))
            result2 **= pows
        print(f"The result of the power of your number set is this: {result2}")

    else:
        print("Please enter an option from the ones give above!")


elif usrcalc == "roots" or usrcalc == "root":
    chcr = input("Spectacular! Please remember, variables are not going to get counted.\nDo you want to calculate roots of an expression, or of a single number?\nType Eq or Num respectively: ")
    chcr = chcr.lower()
    if chcr == "eq" or chcr == "equation" or chcr == "an equation":
        eq = eval(input("Please enter the equation you want to be rooted: "))
        root = float(input("Enter the degree of the root for the equation,\neg cube root is degree 3, so write 3: "))
        print(eq**(1/root))

    elif chcr == "num" or chcr == "number" or chcr == "no." or chcr == "no":
        number1 = float(input("Enter a number which's root you want to find out: "))
        decimal = int(input("How many decimal places do you want your power to be rounded to?"))
        root2 = float(input("Enter the degree of your root, eg cube root is 3rd degree, so you write 3. :  "))
        res = round((number1 ** (1/root2)), decimal)
        print(res)

    else:
        print("Please enter either Eq or Num:)!")


elif usrcalc == "logarithm" or usrcalc == "log":
        logtype = input("Which logarithm do you want? Type 'common' for log base 10,\n 'natural' for ln or phi, or 'custom' for any base: ").lower()
        if logtype == "common":
            num = float(input("Enter the number: "))
            result = math.log10(num)
            print(f"log₁₀({num}) = {result}")
    
        elif logtype == "natural":
            num = float(input("Enter the number: "))
            result = math.log(num)
            print(f"ln({num}) = {result}")
    
        elif logtype == "custom":
            num = float(input("Enter the number: "))
            base = float(input("Enter the base: "))
            result = math.log(num, base)
            print(f"log_{base}({num}) = {result}")

    
elif usrcalc == "area" or "surface area":
    print("Please remember, do not enter units when asked to enter the value\nof any dimension of your shape. We will add it later.")
    shpops = ["Triangle", "Square", "Rectangle",
              "Circle", "Ellpse", "Parallelogram",
              "Rhombus", "Kite", "Sector", "Hexagon"]
    shp = input(f"Which shape do you want to calculate the area for?\nType an option from the one given below:\n{shpops}\n")
    shp = shp.lower()
    if shp == "triangle":
        method = input("Do you know the base and height, or all three sides? Type 'bh' or 'sides': ").lower()
        if method == "bh" or method == "base and height":
            base, height = map(float, input("Enter base and height separated by space: ").split())
            area = (base * height) / 2
        elif method == "sides" or method == "three sides" or method == "3 sides":
            side1, side2, side3 = map(float, input("Enter the three sides separated by spaces: ").split())
            s = (side1 + side2 + side3) / 2
            area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        print(f"The area is: {round(area, 5)}")
        
    elif shp == "square":
        unit = input("Please enter the unit of the side of your square:  ")
        side = float(input("Enter the length of any side of the square:  "))
        area = sq_a(side)
        print(f"The area of your square with sidelength as {side} {unit} is {area} {unit}².  ")

    elif shp == "rectangle":
        unit = input("Please enter only the unit of the dimensions of the rectangle\nIf they are not the same unit, please convert them to the same unit.\nEnter the unit here:  ")
        side1, side2 = map(float, input("Enter the two adjacent sides separated by spaces: ").split())
        area = rect_a(side1, side2)
        print(f"The area of your rectangle with dimensions as {side1} {unit} and {side2} {unit} is {area} {unit}².  ")
        


    elif shp == "circle" or shp == "area of a circle":
        pival = int(input("Do you want to take pi as 3.14 or 22/7?\nType 1 if 3.14, type 2 if 22/7: "))
        circf = input("Do you have the value of the circumference of your circle?\nType the value if you do, otherwise leave one space: ")
        circf = circf.strip()
        if circf:
            circf = float(circf)
            if pival == 1:
                rad = circf/3.14/2
                area = 3.14*(rad**2)
                print("The area of your circle with circumference as ", circf, " is: ", area)
            elif pival == 2:
                rad = circf/(22/7)/2
                area = (22/7)*(rad**2)
                print("The area of your circle with circumference as ", circf, " is: ", area)

        else:
            diam = input("Do you have the value of the diameter of the circle?\nEven if you have the radius, multiply it by two and enter it.\nIf yes, type it in. If no, leave a space: ")
            diam = diam.strip()
            if diam:
                diam = float(diam)
                if pival == 1:
                    rad = diam/2
                    area = 3.14*(rad**2)
                elif pival == 2:
                    rad = diam/2
                    area = (22/7)*(rad**2)
                print("The area of your circle with circumference as ", circf, " is: ", area)
    elif shp == "ellipse" or shp == "oval":
        l = float(input("Please enter the length of your ellipse, no units: "))
        b = float(input("Please enter the breadth of your ellipse, no units"))
        unit = input("Please enter the units, eg if centimeters then enter cm. :  ")
        r1, r2 = l/2, b/2
        pival = int(input("Do you want to take pi as 3.14 or 22/7?\nType 1 if 3.14, type 2 if 22/7: "))
        if pival == 1:
            area = 3.14*r1*r2 
        elif pival == 2:
            area = (22/7)*r1*r2
        else:
            print("Please enter a valid value from the options of pi.")
        print("The area of your ellipse with length and breadth as ", l, " and ", b, " respectively is ", area, " cm²")

    elif shp == "parallelogram" or shp == "paralellogram":
        exshap = '''
      _________________
     / |              /
    /  |             /
   /   |            /   
  /    |           /
 /     |          /
------------------
'''      
        base, height = map(float, input(f"Please enter the length and breadth of your parallelogram.\nKindly remember, the length and breadth are not the two sides. For reference:\n{exshap}\nHere, the length is the vertical line, \nand the breadth is the top and bottom side lengths. \n Please enter the length and breadth without any units, and separate them by a space: ").split())
        area = base*height
        print(f"The area of your parallelogram with the base as {base} and height as {height} is {area}.")

    elif shp == "rhombus" or shp == "rombus" or shp == "a rhombus":
        print("The two diagonals of a rhombus are the two lines that are made by connecting \nopposite points to each other.")
        d1, d2 = map(float, input("Enter the two diagonals separated by space: ").split())
        area = (d1 * d2) / 2
        print(f"The area is: {round(area, 5)}")    

    elif shp == "kite" or shp == "diamond" or shp == "a kite":
        print("The two diagonals of a kite are the two lines that are made by connecting \nopposite points to each other.")
        d1, d2 = map(float, input("Enter the two diagonals of your kite separated by space: ").split())
        area = (d1 * d2) / 2
        print(f"The area of your kite is: {round(area, 5)}")

    elif shp == "sector" or shp == "part of a circle":
        rad = float(input("Please enter the radius of your circle:  "))
        pival = int(input("For pi, do you want the value to be 3.14159, 3.14, or 22/7?\nEnter 1 if 3.14159, 2 if 3.14, or 3 if 22/7:  "))
        angle = float(input("The angle between the two rays that extend from the center\nof your circle is called the angle of your sector.\nPlease enter the angle of your sector:  "))
        if pival == 1:
            area = (angle/360)* 3.14159*rad*rad
        elif pival == 2:
            area = (angle/360)*3.14*rad*rad
        elif pival == 3:
            area = (angle/360)*(22/7)*rad*rad
        else:
            print("Please enter either 1, 2, or 3 for the value of pi.")
        print(f"The area of your sector with value of pi as {pival} and the radius of your circle as {rad}\nand the angle of your sector as {angle} is {area} units.")

    elif shp == "hexagon":
        side = float(input("Enter the side length of your regular hexagon: "))
        area = (3 * math.sqrt(3) / 2) * (side ** 2)
        print(f"The area of your hexagon with side length {side} is: {round(area, 5)}")


elif usrcalc == "volume":
    print("Please remember, do not enter units when asked to enter the value\nof any dimension of your shape. We will add it later.")
    shpops = ["Sphere", "Cuboid", "Cube", "Cylinder", "Cone", 
          "Spherical Sector", "Square Pyramid", "Triangular Pyramid", 
          "Prism (any base)", "Pyramid (any base)"]
    shp = input(f"Please enter what 3D shape you want to find the area of from the ones given below:\n{shpops}\nPlease enter exactly what is written in the options:  ")
    shp = shp.lower().strip()
    if shp == "sphere" or shp == "circle":
        pival = float(input("Please enter your desired value of pi, for example 22/7, or 3.14159, etc:  "))
        rad = float(input("Please enter the value of the radius of your sphere without units:  "))
        area = (4/3) * pival * (rad**3)
        print(f"The area of your circle with radius of {rad} and pi value as {pival} is {area}")

    elif shp == "cuboid" or shp == "rectangle":
        hei = float(input("Please enter the height of your cuboid:  "))
        wid = float(input("Please enter the width of your cuboid:  "))
        len = float(input("Please enter the length of your cuboid:  "))
        unit = input("Please enter your unit(eg, cm, or mm, etc):  ")
        print(f"The area of your cuboid with height, width, and length as {hei}, {wid}, {len} is {hei*wid*len} {unit}³.")

    elif shp == "cube" or shp == "square":
        dim = float(input("Please enter any side length of your cube: "))
        unit = input("Please enter your measurement unit(eg cm, or mm, etc):  ")
        print(f"The area of your cube with side length as {dim} is {dim**2} {unit}³. ")

    elif shp == "cylinder" or shp == "cilynder" or shp == "cilinder" or shp == "cylynder":
        rad = float(input("Please enter the radius of the circular part of your sphere:  "))
        pival = float(input("Please enter the value of pi that you want,\nfor example 3.14 or 3.14159 or 22/7:  "))
        hei = float(input("Please enter the height of your cylinder:  "))
        unit = input("Please enter the unit(eg cm, or mm, etc):  ")
        print(f"The volume of your cylinder with pi value, radius, and height\nas {pival}, {rad}, and {hei} is {rad*rad*pival} {unit}³. ")

    elif shp == "cone":
        rad = float(input("Please enter the radius of the base of your cone:  "))
        pival = float(input("Enter your desired value of pi(eg 3.14159):  "))
        hei = float(input("Please enter the height of your cone here:  "))
        unit = input("Please enter your desired unite for measurement: ")
        vol = pival*rad*rad*(hei/3)
        print(f"The volume of our triangle with pi value, height, and\nradius as {pival}, {hei}, {rad} is {vol}. ")

    elif shp == "sphericalsector" or shp == "sector":
        rad = float(input("Please enter the radius of your sector's circle:  "))
        pival = float(input("Please enter your desired value of pi(eg 3.14159):  "))
        print("The height of your sector is the height of the spherical cap that forms the base of the sector.")
        hei = float(input("Enter the height of your sector:  "))
        unit = input("Please enter the desired unit of measuremen(eg cm):  ")
        volume = (2/3)*pival*(rad**2)*hei
        print(f"The volume of your sector with radius as {rad}, pi value as {pival} and unit as {unit} is {volume} cubic {unit}")

    elif shp == "squarepyramid" or shp == "pentahedron":
        side = float(input("Please enter the side length of the square at the pyramid's base:  "))
        print("The height of your pyramid is the PERPENDICULAR length from the base's\ncenter to the apex,not one triangular side length.")
        hei = float(input("Please enter the height of your pyramid:  "))
        vol = ((side**2)*hei)/3
        unit = input("Please enter your unit(eg cm):  ")
        print(F"The volume of your tetrahedron pyramid with base side length as {side} and height as {hei} is {vol} cubic {unit}s")

    elif shp == "triangularpyramid" or shp == "tetrahedron":
        unit = input("Please enter the unit of measurement(eg cm):  ")
        triops = int(input("Do you have the area of the base of your pyramid? Type 1 if yes, or 2 if no:  "))
        if triops == 1:
            area = float(input("Please enter the area of the triangular\nbase of your pyramid without any units:  "))
            print("The height of your pyramid is the PERPENDICULAR length from the base's\ncenter to the apex,not one triangular side length.")
            hei = float(input("Please enter the perpendicular height of your pyramid:  "))
            vol = (1/3)*area*hei
        elif triops == 2:
            side1, side2, side3 = map(float, input("Enter the three sides of the triangular base separated by spaces: ").split())
            s = (side1 + side2 + side3) / 2
            area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
            print("The height of your pyramid is the PERPENDICULAR length from the base's\ncenter to the apex,not one triangular side length.")
            hei = float(input("Please enter the perpendicular height of your pyramid:  "))
            vol = (1/3)*area*hei
        else:
            print("Please enter either 1 or 2 depending on whether\nyou have the base area or not.")

        print(f"The volume of your tetrahedron pyramid with base area as {area} and height as {hei} is {vol} cubic {unit}s.")

    elif shp == "prism" or shp == "prism(anybase)" or shp == "prismanyshape":
        shps = ["Rectangle", "Triangle", "Hexagon", "Circle",
                "Square", "Parallelogram"]
        chcs = input(f"{shps}\nIs your prism's base shape in any of these?\nIf yes, type the shape, else, leave blank").lower()
        chcs = chcs.strip()
        if chcs:
            print("Please find the area of your base shape from the area option in our calculator!")
            area = input("Please enter the area without any units here:  ")
            height = float(input("Please enter the height of your prism(Height from top face to bottom face)\nwithout any units:  "))
        else:
            print("Please find the area of the base face of your 3D figure.")
            area = float(input("Please enter the area here without any units:  "))
            height = float(input("Please enter the height of your prism\n(Height from top to bottom face)here without any units:  "))
        units = input("Please enter the unit of measuremement(eg cm or m) here:  ")
        vol = area*height
        print("The volume of your prism with area of the base shape as {area} square {units}, height of the prism as {height} {units} is {vol} {units}³") 

    elif shp == "pyramid(anybase)" or shp == "pyramidanybase" or shp == "pyramidanybaseshape" or shp == "pyramid":
        shps = ["Rectangle", "Triangle", "Hexagon", "Circle",
                "Square", "Parallelogram"]
        chcs = input(f"{shps}\nIs your pyramid's base shape in any of these?\nIf yes, type the shape, else, leave blank").lower()
        chcs = chcs.strip()
        if chcs:
            print("Please find the area of your base shape from the area option in our calculator!")
            area = input("Please enter the area without any units here:  ")
            height = float(input("Please enter the height of your pyramid\n(Perpendicular height from centre of base to apex)without any units:  "))
        else:
            print("Please find the area of the base face of your 3D figure.")
            area = float(input("Please enter the area here without any units:  "))
            height = float(input("Please enter the height of your pyramid\n(Perpendicular height from centre of base to apex)without any units:  "))
        units = input("Please enter the unit of measuremement(eg cm or m) here:  ")
        vol = (area*height)/3
        print("The volume of your pyramid with area of the base shape as {area} square {units}, height of the pyramid as {height} {units} is {vol} {units}³")


elif usrcalc == "force":
    fops = ["Basic Force with Mass and Acceleration", "Friction", 
            "Gravity","Multidirectional Force"]
    uc = input("What type of force do you want to calculate? Choose from below.\nAlso write Basic if you ant to calcualte basic force.\n", fops,"\n")
    uc = uc.lower().strip()
    if uc in ["basic", "basicforce", "massandacceleration", "basicforcewthmassandacceleration"]:
        accun = input("Enter the unit of acceleration(eg m/s or km/h)\n with a slash(like m/s or km/h) Also, you\ndon't need to write m/s², just m/s:  ")
        acc = float(input("Please enter the value of acceleration(nu units needed :]):  "))
        mu = input("Please enter the unit of mass, eg grams:  ")
        mass = float(input("Please enter the mass of your object(no units needed!):  "))
        print(f"The force of your object with acceleration as {acc} {accun} and mass as {mass} {mu} is {acc * mass} {accun}²  ")

    elif uc == "friction":
        print("Friction force = coefficient of friction × normal force")
    
        choice = input("Do you know the normal force, or do you need to calculate it?\nType 'know' or 'calculate': ").lower()
    
        if choice == "know":
            normal_force = float(input("Enter the normal force (N): "))
            mu = float(input("Enter the coefficient of friction: "))
            friction = mu * normal_force
            print(f"The friction force is: {friction} N")
    
        elif choice == "calculate":
            surface = input("Is the object on a flat surface or an incline?\nType 'flat' or 'incline': ").lower()
        
            if surface == "flat":
                mass = float(input("Enter the mass (kg): "))
                mu = float(input("Enter the coefficient of friction: "))
                gravity = 9.8
                normal_force = mass * gravity
                friction = mu * normal_force
                print(f"The friction force is: {friction} N")
        
            elif surface == "incline":
                mass = float(input("Enter the mass (kg): "))
                mu = float(input("Enter the coefficient of friction: "))
                angle = float(input("Enter the incline angle (degrees): "))
                gravity = 9.8
                angle_rad = math.radians(angle)
                normal_force = mass * gravity * math.cos(angle_rad)
                friction = mu * normal_force
                print(f"The friction force is: {friction} N")

    elif uc == "gravity" or uc == "gravitationalforce":
        unit = input("Please enter the unit of mass for both objects.\nIf they are different, please convert them to the same unit.\n  ")
        m1 = float(input("Please enter the mass of the first object without any units:  "))
        m2 = float(input("Please enter the mass of the second object without any units:  "))
        und = input("Please enter the unit of distance between both objects:  ")
        dis = float(input("Please enter the distance between both objects without units:  "))
        fc = 9.8 * (m1 * m2) / dis
        print(f"Given that the mass of your first object is {m1} {unit}s and the mass\nof your second object is {m2} {unit}s, and that the distance\nbetween both objects is {dis} {und}s, the gravitational\nforce between both the objects will be {fc} newtons.")

    elif usrcalc == "multidirectional force" or usrcalc == "resultant force":
        print("This calculates the resultant force when multiple forces act in different directions.")
    
        dimension = input("Are the forces in 2D (on a plane) or 3D (in space)?\nType '2d' or '3d': ").lower()
    
        if dimension == "2d":
            num_forces = int(input("How many forces are acting? "))
        
             # Initialize total force components
            total_x = 0
            total_y = 0
        
            for i in range(num_forces):
                print(f"\nForce {i+1}:")
                method = input("Do you know the force magnitude and angle, or x and y components?\nType 'magnitude' or 'components': ").lower()
            
                if method == "magnitude":
                    magnitude = float(input("Enter the force magnitude: "))
                    angle = float(input("Enter the angle from positive x-axis (degrees): "))
                
                    # Convert to radians and calculate components
                    angle_rad = math.radians(angle)
                    force_x = magnitude * math.cos(angle_rad)
                    force_y = magnitude * math.sin(angle_rad)
                
                    total_x += force_x
                    total_y += force_y
            
                elif method == "components":
                    force_x = float(input("Enter the x-component of the force: "))
                    force_y = float(input("Enter the y-component of the force: "))
                
                    total_x += force_x
                    total_y += force_y
        
            # Calculate resultant force
            resultant = math.sqrt(total_x**2 + total_y**2)
        
            # Calculate angle
            if total_x != 0:
                angle_result = math.degrees(math.atan(total_y / total_x))
            else:
                angle_result = 90 if total_y > 0 else -90
        
            unit = input("Enter the unit of force (e.g., N for Newtons): ")
        
            print(f"\nResultant Force: {round(resultant, 3)} {unit}")
            print(f"Direction: {round(angle_result, 2)}° from positive x-axis")
            print(f"Components: x = {round(total_x, 3)} {unit}, y = {round(total_y, 3)} {unit}")

        elif dimension == "3d":
            num_forces = int(input("How many forces are acting? "))
            total_x = 0
            total_y = 0
            total_z = 0
            for i in range(num_forces):
                print(f"\nForce {i+1}:")
                method = input("Do you know the components (x, y, z) or magnitude with angles?\nType 'components' or 'magnitude': ").lower()
                if method == "components":
                    force_x = float(input("Enter the x-component: "))
                    force_y = float(input("Enter the y-component: "))
                    force_z = float(input("Enter the z-component: "))
                    total_x += force_x
                    total_y += force_y
                    total_z += force_z
                elif method == "magnitude":
                    magnitude = float(input("Enter the force magnitude: "))
                    alpha = float(input("Enter angle with x-axis (degrees): "))
                    beta = float(input("Enter angle with y-axis (degrees): "))
                    gamma = float(input("Enter angle with z-axis (degrees): "))
                    force_x = magnitude * math.cos(math.radians(alpha))
                    force_y = magnitude * math.cos(math.radians(beta))
                    force_z = magnitude * math.cos(math.radians(gamma))
                    total_x += force_x
                    total_y += force_y
                    total_z += force_z
            resultant = math.sqrt(total_x**2 + total_y**2 + total_z**2)
            if resultant != 0:
                alpha_result = math.degrees(math.acos(total_x / resultant))
                beta_result = math.degrees(math.acos(total_y / resultant))
                gamma_result = math.degrees(math.acos(total_z / resultant))
            else:
                alpha_result = beta_result = gamma_result = 0
            unit = input("Enter the unit of force (e.g., N for Newtons): ")
            print(f"\nResultant Force: {round(resultant, 3)} {unit}")
            print(f"Direction angles:")
            print(f"  α (with x-axis): {round(alpha_result, 2)}°")
            print(f"  β (with y-axis): {round(beta_result, 2)}°")
            print(f"  γ (with z-axis): {round(gamma_result, 2)}°")
            print(f"Components: x = {round(total_x, 3)} {unit}, y = {round(total_y, 3)} {unit}, z = {round(total_z, 3)} {unit}")
    
        else:
            print("Please enter either '2d' or '3d'!") 


elif usrcalc == "mass" or usrcalc == "kilograms" or usrcalc == "pounds":
    print("Choose how you want to calculate mass:")
    mass_options = """
    1. From density and volume
    2. From force and acceleration (F = ma)
    3. From weight (gravitational force)
    4. From momentum and velocity
    5. From kinetic energy and velocity
    """
    print(mass_options)
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        density = float(input("Enter density (kg/m³): "))
        volume = float(input("Enter volume (m³): "))
        mass = density * volume
        print(f"The mass is: {mass} kg")
    
    elif choice == "2":
        force = float(input("Enter force (N): "))
        acceleration = float(input("Enter acceleration (m/s²): "))
        mass = force / acceleration
        print(f"The mass is: {mass} kg")
    
    elif choice == "3":
        weight = float(input("Enter weight (N): "))
        gravity = float(input("Enter gravity (default 9.8 m/s²): ") or "9.8")
        mass = weight / float(gravity)
        print(f"The mass is: {mass} kg")
    
    elif choice == "4":
        momentum = float(input("Enter momentum (kg·m/s): "))
        velocity = float(input("Enter velocity (m/s): "))
        mass = momentum / velocity
        print(f"The mass is: {mass} kg")
    
    elif choice == "5":
        kinetic_energy = float(input("Enter kinetic energy (J): "))
        velocity = float(input("Enter velocity (m/s): "))
        mass = (2 * kinetic_energy) / (velocity ** 2)
        print(f"The mass is: {mass} kg")
    
    else:
        print("Invalid choice!")


elif usrcalc == "pressure":

    pt = ["Atmospheric Pressure (1)", "Liquid Pressure (2)", "Total Pressure (3)",
          "Normal Pressure on a surface (4)", "Pressure of an object (5)"]
    print(f"What type of pressure do you want to calculate? The options are as given below:\n{pt}.")
    uo = input("Enter eiter 1,2,3,4, or 5 for the options:  ")
    while True:
        try:
            uo = int(uo)
            break
        except ValueError:
            print("Your options are given above. Beside each one is a number from\n1 to 5. Please enter either 1,2,3,4, or 5.")
            uo = input("Enter eiter 1,2,3,4, or 5 for the options:  ")

    if uo == 1:
        height = float(input("Enter height (m): "))
        density = float(input("Enter air density (kg/m³, default 1.225): ") or "1.225")
        g = 9.8
        atmospheric_pressure = density * g * height
        print(f"Atmospheric Pressure: {atmospheric_pressure} Pa")

    elif uo == 2:
        height = float(input("Enter liquid height (m): "))
        density = float(input("Enter liquid density (kg/m³): "))
        g = 9.8
        liquid_pressure = density * g * height
        print(f"Liquid Pressure: {liquid_pressure} Pa")

    elif uo == 3:
        atmospheric = float(input("Enter atmospheric pressure (Pa, default 101325): ") or "101325")
        height = float(input("Enter liquid height (m): "))
        density = float(input("Enter liquid density (kg/m³): "))
        g = 9.8
        total_pressure = atmospheric + (density * g * height)
        print(f"Total Pressure: {total_pressure} Pa")

    elif uo == 4:
        force = float(input("Enter normal force (N): "))
        area = float(input("Enter surface area (m²): "))
        normal_pressure = force / area
        print(f"Normal Pressure: {normal_pressure} Pa")

    elif uo == 5:
        force = float(input("Enter force applied (N): "))
        area = float(input("Enter contact area (m²): "))
        object_pressure = force / area
        print(f"Pressure of object: {object_pressure} Pa")

    else:
        print("Invalid option. Please choose between 1 and 5.")


elif usrcalc == "factorial":
    print("A factorial of a number is the num * num-1 * num-2 * um-3 until num-x where\n the product becomes zero. For example:\n5 factorial  = 5*4*3*2*1 which is 120.")
    fn = int(input("Please enter a postive integer of whose factorial you wanna find out:  "))
    while fn <= 0 or fn%1 != 0:
        fn = int(input("Please enter a valid, non-decimal and positive number to find its factorial:  "))
    f2 = fn
    num = 1
    for i in range(fn):
        num *= fn
        if fn == 1:
            break
        fn -= 1
    print(f"The factorial of {f2} is {num}")