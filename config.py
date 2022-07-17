"""
url str:
    Url to get the matrix.

data dict:
    Request parameters to get the matrix.

matrix_ids [str]:
    Id list for scraping the matrix.

pattern [[int]]:
    Two-dimensional list showing the position and order of passwords.
    [matrix idx, row idx, col idx] indicates a position of the matrix.
    So you can express your password as follows:
        pattern = [[0,0,0], [1,2,3], [0,3,1], [2,1,2], ...]

         matrix[0]    matrix[1]    matrix[2]
        [ 1 * * * ]  [ * * * * ]  [ * * * * ]  row[0]
        [ * * * * ]  [ * * * * ]  [ * * 4 * ]  row[1]
        [ * * * * ]  [ * * * 2 ]  [ * * * * ]  row[2]
        [ * 3 * * ]  [ * * * * ]  [ * * * * ]  row[3]
          ^              ^
          col[0]         col[1]
"""

url = 'https://your-matrix-site.example.com/ui/index.php'
data = {
    'param1': 'value1',
    'param2': 'value2'
}
matrix_ids = ['randamNumbarTable1st', 'randamNumbarTable2nd', 'randamNumbarTable3rd']
pattern = [[0,0,0], [1,2,3], [0,3,1], [2,1,2]]
