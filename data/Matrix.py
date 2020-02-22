# make adj matrix
# source: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/


# Big-O time complexity of O(n^2)
def create():
    arr = [[0 for i in range(27)] for j in range(27)]
    return arr


# Big-O time complexity of O(n^2)
def build():
    arr = [[0 for i in range(27)] for j in range(27)]
    arr[0][0:1] = [0.0]
    arr[1][0:2] = [7.2, 0.0]
    arr[2][0:3] = [3.8, 7.1, 0.0]
    arr[3][0:4] = [11.0, 6.4, 9.2, 0.0]
    arr[4][0:5] = [2.2, 6.0, 4.4, 5.6, 0.0]
    arr[5][0:6] = [3.5, 4.8, 2.8, 6.9, 1.9, 0.0]
    arr[6][0:7] = [10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0.0]
    arr[7][0:8] = [8.6, 2.8, 6.3, 4.0, 5.1, 4.3, 4.0, 0.0]
    arr[8][0:9] = [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.0]
    arr[9][0:10] = [2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8.0, 9.3, 4.8, 0.0]
    arr[10][0:11] = [6.4, 7.3, 10.4, 1.0, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0.0]
    arr[11][0:12] = [3.2, 5.3, 3.0, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0.0]
    arr[12][0:13] = [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12.0, 4.7, 0.0]
    arr[13][0:14] = [5.2, 3.0, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0.0]
    arr[14][0:15] = [4.4, 4.6, 5.6, 4.3, 2.4, 3.0, 8.0, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0.0]
    arr[15][0:16] = [3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4.0, 5.4, 2.9, 6.6, 1.5, 0.6, 0.0]
    arr[16][0:17] = [7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4.0, 6.4, 5.6, 0.0]
    arr[17][0:18] = [2.0, 6.0, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0.0]
    arr[18][0:19] = [3.6, 5.0, 3.6, 6.0, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1.0, 5.4, 3.0, 2.2, 1.7, 6.1, 1.6, 0.0]
    arr[19][0:20] = [6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1.0, 4.1,
                     11.5, 3.7, 1.0, 6.9, 6.8, 6.4, 7.2, 4.9, 4.4, 0.0]
    arr[20][0:21] = [1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8,
                     6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6, 3.0, 4.6, 7.5, 0.0]
    arr[21][0:22] = [3.4, 10.9, 5.0, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3,
                     6.2, 10.3, 8.2, 7.4, 6.9, 12.0, 5.0, 6.6, 9.3, 2.0, 0.0]
    arr[22][0:23] = [2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10.0, 7.8, 7.8, 4.3, 4.1, 3.4,
                     7.8, 5.5, 4.6, 4.2, 9.4, 2.3, 3.9, 6.8, 2.9, 4.4, 0.0]
    arr[23][0:24] = [6.4, 6.9, 9.7, 0.6, 6.0, 9.0, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9,
                     11.5, 4.4, 4.8, 5.6, 7.5, 5.5, 6.5, 11.4, 6.4, 7.9, 4.5, 0.0]
    arr[24][0:25] = [2.4, 10.0, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5,
                     7.2, 6.3, 5.9, 11.1, 4.0, 5.6, 8.5, 2.8, 3.4, 1.7, 5.4, 0.0]
    arr[25][0:26] = [5.0, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11.0, 3.7, 2.8,
                     6.4, 6.5, 5.7, 6.2, 5.1, 4.3, 1.8, 6.0, 7.9, 6.8, 10.6, 7.0, 0.0]
    arr[26] = [3.6, 13.0, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6.0, 6.8, 6.4, 14.1,
               10.5, 8.8, 8.4, 13.6, 5.2, 6.9, 13.1, 4.1, 4.7, 3.1, 7.8, 1.3, 8.3, 0.0]
    return arr
