class File:
    def __init__(self, file_path, delimiter):
        self.file_path = file_path
        self.delimiter = delimiter

    def write_data(self, data):
        with open(self.file_path, 'w') as file:
            for row in data:
                line = self.delimiter.join(map(str, row))
                file.write(line + '\n')
            print('Archivo creado')