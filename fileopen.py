'''
This is a code to read in the Lazor boards bff file and put the information into a txt file.
'''

def load_file(filename):
	'''
	This function will read in the lazor board bff file.
	The bff file will contain information about the lazor board.

    **Parameters**

        filename: *str*
            The file to be read in.

    **Returns**

        board_data: *str*
            The relative board information inside the file, including the shape of the grid, 
        numbers and types of the blocks, location and direction of all the laser points, 
        location of all the final points.
	'''
	board_data = open(filename, 'r').readlines()
	return board_data

def write_file(board_data, filename):
    '''
    Given a string with information about the lazor board,
    save them to a given txt file.

    **Parameters**

        board_data: *str*
            Information about the lazor board. The return of the load_file function.
        filename: *str*
            The name of the file we will write.

    **Returns**

        None
    '''

    board_data_file = open(filename, "w")
    board_data_file.write(''.join(map(str, board_data)))
    board_data_file.close()

def get_grid(board_data):
	'''
    The function can extract the information about the grid from board_data, and transfer it into a 
    list of matrix. 
    The way to realize it is to go through each line of the board_data, and if the first character of 
    the line is string 'o' or 'x', then this line is a part of the grid.

    **Parameters**

        board_data: *str*
            Information about the lazor board. The return of the load_file function.

    **Returns**

        grid: 
    '''
	
	grid = []
	for i in range(len(board_data)):

		if board_data[i][0] == str('o') or\
		   board_data[i][0] == str('x'):
			print(board_data[i])
			grid.append(board_data[i].strip('\n').split(' '))

	return grid

def get_blocks(board_data):
	'''
    The function can extract the information about the blocks from board_data.
    The way to realize it is to go through each line of the board_data, and if the first character of 
    the line is string 'A' or 'B' or 'C', then this line is a part of the blocks information.
    **Parameters**

        board_data: *str*
            Information about the lazor board. The return of the load_file function.

    **Returns**

        None
    '''
	blocks = []
	for i in range(len(board_data)):

		if board_data[i][0] == str('A') or\
	 	   board_data[i][0] == str('B') or\
	 	   board_data[i][0] == str('C'):
	 		blocks.append(board_data[i].strip('\n'))

	return blocks

def get_lasers(board_data):
    '''
    The function can extract the information about the lasers from board_data.
    The way to realize it is to go through each line of the board_data, and if the first character of 
    the line is string 'L', then this line is a part of the laser.

    **Parameters**

        board_data: *str*
            Information about the lazor board. The return of the load_file function.

    **Returns**

        None
    '''

    lasers = []
    for i in range(len(board_data)):
        if board_data[i][0] == str('L'):
            # print(board_data[i])
            lasers.append(board_data[i].strip('\n'))

    return lasers

def get_points(board_data):
	'''
    The function can extract the information about the final points from board_data.
    The way to realize it is to go through each line of the board_data, and if the first character of 
    the line is string 'P', then this line is a part of the blocks information.
    **Parameters**

        board_data: *str*
            Information about the lazor board. The return of the load_file function.

    **Returns**

        None
    '''
	points = []
	for i in range(len(board_data)):

		if board_data[i][0] == str('P'):
	 		# print(board_data[i])
	 		points.append(board_data[i].strip('\n'))

	return points

if __name__ == '__main__':
	dark_1_data = load_file('dark_1.bff')
	# print(type(dark_1_data))
	write_file(dark_1_data, 'dark_1.txt')

	a = get_grid(dark_1_data)
	print(a)

	b = get_blocks(dark_1_data)
	print(b)
	# print('The numbers of the blocks is %s' % b[0])

	c = get_lasers(dark_1_data)
	print(c)

	d = get_points(dark_1_data)
	print(d)


	# mad_1_data = load_file('mad_1.bff')
	# print(mad_1_data)
	# write_file(mad_1_data, 'mad_1.txt')

	# mad_4_data = load_file('mad_4.bff')
	# print(mad_4_data)
	# write_file(mad_4_data, 'mad_4.txt')