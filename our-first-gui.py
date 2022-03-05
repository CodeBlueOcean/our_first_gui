#Exercise!
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# # print('') it has \n, empty string is going to default to a empty new line. 
# for image in picture:
#     for pixel in image:
#         if (pixel == 1):
#             print('*', end='')
#         else:
#             print('', end='')

# change row
for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')





#1 interate over picture.
    # if 0 -> print ''
    # if 1 -> print * 

