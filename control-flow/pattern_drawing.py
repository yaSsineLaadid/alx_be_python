# pattern_drawing.py
pattern = int(input("Enter the size of the pattern:"))
while pattern <= 0:
    print("Error: Please Enter a positive number.")
    pattern = int(input("Enter the size of the pattern:"))
for row in range(pattern):
    for col in range(pattern):
        print("*", end="")
    print()

