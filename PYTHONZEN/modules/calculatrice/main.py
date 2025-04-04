from calculatrice import calculate_area

def main():
    print("Welcome to the Area Calculator!")
    figure = input("Enter the figure type (circle or rectangle): ").strip().lower()
    if figure == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_area(figure, radius)
        print(f"The area of the circle with radius {radius} is: {area}")
    elif figure == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_area(figure, length, width)
        print(f"The area of the rectangle with length {length} and width {width} is: {area}")
    else:
        print("Invalid figure type. Please enter 'circle' or 'rectangle'.")

if __name__ == "__main__":
    main()