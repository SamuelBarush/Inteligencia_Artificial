class Board:

    def __init__(self, file_path) -> None:
        # Define the path to the text file
        self.board_file_path = file_path
        self.board_data = self.read_board(self.board_file_path)
        #self.board_data_with_labels = self.add_labels(self.board_data)

    # Read the board configuration from the text file
    def read_board(self, file_path):
        board = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    row = []
                    for cell in line.strip().split(','):
                        if cell == '0':
                            row.append((0,0))
                        elif cell == '1':
                            row.append((1,0))
                        elif cell == '2':
                            row.append((2,0))
                        elif cell == '3':
                            row.append((3,0))
                        elif cell == '4':
                            row.append((4,0))
                        else:
                            row.append((int(cell), 'white'))  # Default color for unknown values
                    board.append(row)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        
        print(board)
        return board
