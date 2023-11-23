class Data:
    def __init__(self, file_path, delimiter, attributes) -> None:
        # Define the path to the text file
        self.file_path = file_path        
        self.delimiter = delimiter
        self.attributes = attributes 
        self.data = self.read_data(self.file_path)
        
    def read_data(self, file_path):
        data = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    row = []
                    i = 0
                    for cell in line.strip().split(self.delimiter):
                        data_type = self.get_type(cell)
                        attribute = self.attributes[i]
                        print(attribute)
                        row.append((cell, data_type, attribute))
                        i += 1  # Increment i to move to the next attribute
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
    
    def get_column(self, column):
        column_data = []
        for row in self.data:
            column_data.append(row[column])
        return column_data
    
    def get_row(self, row):
        return self.data[row]
    
    def get_number_of_rows(self):
        return len(self.data)
    
    def get_number_of_columns(self):
        return len(self.data[0])-1
    
    def get_attribute(self, attributes):
        data = []
        for i in range(len(self.attributes)):
            if self.attributes[i] in attributes:
                data.append(self.get_column(i))
        return data
    
    def get_class(self, class_name):
        data = []
        for row in self.data:
            if row[0][0] == class_name:
                data.append(row)
        return data
    
    def show_database(self):
        for row in self.data:
            for cell in row:
                print(cell, end=' ')
            print()               

    def show_column(self, column):
        for row in self.data:
            print(row[column], end=' ')
            print()    
    
    def show_row(self, row):
        for cell in self.data[row]:
            print(cell, end=' ')
            print()
    
    def show_data(self, data):
        for row in data:
            for cell in row:
                print(cell, end=' ')
                print()
            print()
    
    def show_class(self, data):
        for row in data:
            for cell in row:
                print(cell, end=' ')
            print()    