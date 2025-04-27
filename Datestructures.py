letter_values = {
    'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
    'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
    't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26
}

initials = ['k', 'b', 'c']
second_letters = ['a', 'r', 'y']

matrix1 = [[letter_values[initials[0]], letter_values[initials[1]], letter_values[initials[2]]],
           [letter_values[second_letters[0]], letter_values[second_letters[1]], letter_values[second_letters[2]]]]

student_number_part1 = [2, 0, 2]
student_number_part2 = [0, 0, 9]

matrix2 = [student_number_part1, student_number_part2]

print("1st Matrix:")
for row in matrix1:
    print(row)

print("\n2nd Matrix:")
for row in matrix2:
    print(row)

matrix3 = [[matrix1[i][j] + matrix2[i][j] for j in range(3)] for i in range(2)]

print("\n3rd Matrix (Matrix Addition):")
for row in matrix3:
    print(row)

matrix4 = [[2 * matrix1[i][j] for j in range(3)] for i in range(2)]

print("\n4th Matrix (Scalar Multiplication by 2):")
for row in matrix4:
    print(row)

matrix5 = [[matrix2[j][i] for j in range(2)] for i in range(3)]

print("\n5th Matrix (Transpose of 2nd Matrix):")
for row in matrix5:
    print(row)

matrix6 = [
    [matrix3[0][0] * matrix5[0][0] + matrix3[0][1] * matrix5[1][0] + matrix3[0][2] * matrix5[2][0],
     matrix3[0][0] * matrix5[0][1] + matrix3[0][1] * matrix5[1][1] + matrix3[0][2] * matrix5[2][1]],

    [matrix3[1][0] * matrix5[0][0] + matrix3[1][1] * matrix5[1][0] + matrix3[1][2] * matrix5[2][0],
     matrix3[1][0] * matrix5[0][1] + matrix3[1][1] * matrix5[1][1] + matrix3[1][2] * matrix5[2][1]]
]

print("\n6th Matrix (Matrix Multiplication):")
for row in matrix6:
    print(row)

sum_matrix3 = sum(sum(row) for row in matrix3)

print("\nSum of all elements in the 3rd Matrix:", sum_matrix3)

matrix7 = [[0, 0, 0], [0, 0, 0]]

print("\n7th Matrix (Zero Matrix):")
for row in matrix7:
    print(row)

