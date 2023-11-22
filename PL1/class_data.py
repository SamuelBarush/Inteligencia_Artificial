class Data:
    def __init__(self, file_path,delimiter) -> None:
        # Define the path to the text file
        self.file_path = file_path
        self.data = self.read_data(self.file_path)
        self.delimiter = delimiter
        
    def read_data(self, file_path):
        data = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    row = []
                    for cell in line.strip().split(self.delimiter):
                        type = self.get_type(cell)
                        row.append((cell, type))
                    data.append(row)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        
        return data
        
    def get_type(self, value):
        try:
            int(value)
            return 'int'
        except ValueError:
            try:
                float(value)
                return 'float'
            except ValueError:
                return 'string'
    
    def show_data(self):
        for row in self.data:
            for cell in row:
                print(cell, end=' ')
            print()