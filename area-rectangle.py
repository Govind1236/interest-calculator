def calculate_area_of_rectangle(length, widht):
    if length <= 0 or widht <= 0:
        print("Input value is negative enter positive number: ")
    area = length * widht
    return area
length = float(input("Enter Number: "))
widht =  float(input("Enter Second Number: "))
area = calculate_area_of_rectangle(length=length, widht = widht)
print(area)
