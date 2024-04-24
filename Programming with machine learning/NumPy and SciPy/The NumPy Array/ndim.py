# Import numpy with the alias np
import numpy as np

data_1 = [1,2,3,4,5]

data_2 = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]]

data_3 = [
            [
                [1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15]
            ],
            [
                [1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15]
            ]
        ]

data_4 = [

            [
                [
                    [1,2,3,4,5],
                    [6,7,8,9,10]
                ],

                [
                    [11,12,13,14,15],
                    [16,17,18,19,20]
                ]
            ],

            [
                [
                    [1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10]
                ],

                [
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20]
                ]
            ]

        ]

# Declare three separate numpy arrays using different approaches
arr_data_1 = np.array(data_1)
arr_data_2 = np.array(data_2)
arr_data_3 = np.array(data_3)
arr_data_4 = np.array(data_4)

# Output the number of dimensions in each array
print("arr_data_1 ndim: ", arr_data_1.ndim)
print("arr_data_2 ndim: ", arr_data_2.ndim)
print("arr_data_3 ndim: ", arr_data_3.ndim)
print("arr_data_4 ndim: ", arr_data_4.ndim)

# Output the shape of each array
print("arr_data_1 shape: ", arr_data_1.shape)
print("arr_data_2 shape: ", arr_data_2.shape)
print("arr_data_3 shape: ", arr_data_3.shape)
print("arr_data_4 shape: ", arr_data_4.shape)
