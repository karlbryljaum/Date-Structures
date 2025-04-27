# Define the letter values
letter_values = {
    'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
    'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
    't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26
}

# --- 1.a.i. 1st Matrix ---
# First Set: Initials (KARL -> K, B, C)
# Second Set: Second letters in your names (First, Middle, Last)
# Karl's second letters: A (from Karl), R (from Bryl), Y (from Centinales)
initials = ['k', 'b', 'c']  # Your initials: KARL BRYL CENTINALES JAUM
second_letters = ['a', 'r', 'y']  # Second letters in the names

# Create the 1st matrix
matrix1 = [[letter_values[initials[0]], letter_values[initials[1]], letter_values[initials[2]]],
           [letter_values[second_letters[0]], letter_values[second_letters[1]], letter_values[second_letters[2]]]]

# --- 1.a.ii. 2nd Matrix ---
# Student number: 2023-4-0091
student_number_part1 = [2, 0, 2]  # First 3 numbers of student number
student_number_part2 = [0, 0, 9]  # Last 3 numbers of student number

# Create the 2nd matrix
matrix2 = [student_number_part1, student_number_part2]

# --- 1.b. Print both matrices ---
print("1st Matrix:")
for row in matrix1:
    print(row)

print("\n2nd Matrix:")
for row in matrix2:
    print(row)

# --- 2. Matrix Addition ---
# Ensure dimensions are the same before adding
matrix3 = [[matrix1[i][j] + matrix2[i][j] for j in range(3)] for i in range(2)]

# --- 2.b. Print the 3rd matrix ---
print("\n3rd Matrix (Matrix Addition):")
for row in matrix3:
    print(row)

# --- 3. Scalar Multiplication ---
# Multiply the 1st matrix by a scalar value of 2
matrix4 = [[2 * matrix1[i][j] for j in range(3)] for i in range(2)]

# --- 3.b. Print the 4th matrix ---
print("\n4th Matrix (Scalar Multiplication by 2):")
for row in matrix4:
    print(row)

# --- 4. Matrix Transpose ---
# Transpose the 2nd matrix
matrix5 = [[matrix2[j][i] for j in range(2)] for i in range(3)]

# --- 4.b. Print the 5th matrix ---
print("\n5th Matrix (Transpose of 2nd Matrix):")
for row in matrix5:
    print(row)

# --- 5. Matrix Multiplication ---
# Ensure dimensions are compatible for multiplication
matrix6 = [
    [matrix3[0][0] * matrix5[0][0] + matrix3[0][1] * matrix5[1][0] + matrix3[0][2] * matrix5[2][0],
     matrix3[0][0] * matrix5[0][1] + matrix3[0][1] * matrix5[1][1] + matrix3[0][2] * matrix5[2][1]],

    [matrix3[1][0] * matrix5[0][0] + matrix3[1][1] * matrix5[1][0] + matrix3[1][2] * matrix5[2][0],
     matrix3[1][0] * matrix5[0][1] + matrix3[1][1] * matrix5[1][1] + matrix3[1][2] * matrix5[2][1]]
]

# --- 5.b. Print the 6th matrix ---
print("\n6th Matrix (Matrix Multiplication):")
for row in matrix6:
    print(row)

# --- 6. Sum of All Elements ---
# Calculate the sum of all elements in the 3rd matrix
sum_matrix3 = sum(sum(row) for row in matrix3)

# --- 6.b. Print the sum ---
print("\nSum of all elements in the 3rd Matrix:", sum_matrix3)

# --- 7. Zero Matrix ---
# Create a 2x3 zero matrix
matrix7 = [[0, 0, 0], [0, 0, 0]]

# --- 7.b. Print the 7th matrix ---
print("\n7th Matrix (Zero Matrix):")
for row in matrix7:
    print(row)
