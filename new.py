def calculate_average(nums):
    return sum(nums)/len(nums)

def main():
    start = input("Unilateral or Bilateral? (1/2)")

    if start == '1':
        first = float(input("First: "))
        second = float(input("Second: "))
        third = float(input("Third: "))
        average = calculate_average([first, second, third])
        print("The average is: ", average, " lbs\n")
    elif start == '2':
        first_right = float(input("Right Hand - First Measurement: "))
        second_right = float(input("Right Hand - Second Measurement: "))
        third_right = float(input("Right Hand - Third Measurement: "))
        first_left = float(input("Left Hand - First Measurement: "))
        second_left = float(input("Left Hand - Second Measurement: "))
        third_left = float(input("Left Hand - Third Measurement: "))
        average_right = calculate_average([first_right, second_right, third_right])
        average_left = calculate_average([first_left, second_left, third_left])
        print("The average of the right hand is: ", average_right, " lbs\n")
        print("The average of the left hand is: ", average_left, " lbs")
    else:
        print("Invalid input")
        


if __name__ == "__main__":

    main()