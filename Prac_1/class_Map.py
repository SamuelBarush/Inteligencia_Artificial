class Board:

    def __init__(self, file_path , value_init, value_end) -> None:
        # Define the path to the text file
        self.board_file_path = file_path
        self.board_data = self.read_board(self.board_file_path)
        self.board_init = value_init
        self.board_end = value_end


    def read_board(self, file_path):
        board = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    row = []
                    for cell in line.strip().split(','):
                        if cell == '0':
                            row.append([0,0,0]) # 0 = Es muro ,  1 es camino
                        elif cell == '1':
                            row.append([1,0,0]) 
                        else:
                            row.append((int(cell), 'white'))  # Default color for unknown values
                    board.append(row)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        
        return board

    def update_cel_values(self, pos_row, pos_col, values): 
        row = pos_col
        col	= pos_row
        if 0 <= pos_row < len(self.board_data) and 0 <= pos_col < len(self.board_data[0]) and len(values) == 3:
            self.board_data[row][col] = values
        else:
            print("Invalid position or values")

    def show_board(self):
        for row in self.board_data:
            for cell in row:
                print(cell, end=' ')
            print()  # Move to the next row

    def get_cell_value(self, coordinates):
        x, y = coordinates
        if 0 <= x < len(self.board_data) and 0 <= y < len(self.board_data[0]):
            return self.board_data[y][x]
        else:
            print("Invalid coordinates")
            return None  # You can choose to return a default value or raise an exception instead of None
