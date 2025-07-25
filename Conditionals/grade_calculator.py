marks = int(input("Enter your marks: "))

if marks >= 101:
    print("Kindly verify your Marks!")
    exit()

if marks >= 90 and marks <= 100:
    print("You have got 'A' Grade")
elif marks >= 80 and marks < 90:
    print("You have got 'B' Grade")
elif marks >= 70 and marks <= 79:
    print("You have got 'C' Grade")
elif marks >= 60 and marks <= 69:
    print("You have got 'D' Grade")
else:
    print("You have FAILED!")