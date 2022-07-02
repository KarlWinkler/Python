class file_io:

    def __init__(self,  file_name):
        self.file_name = file_name

    def to_array(self):
        list = []
        file = open(self.file_name, 'r')
        for line in file:
            if line.startswith('\n') or line.startswith('\r'):
                continue
            elif not line:
                break
            else:
                list.append(line.strip('\n').strip('\r'))

        return list

    def amend_from_array(self, input):
        file = open(self.file_name, 'a')
        for entry in input:
            file.write(entry + '\n')

    def csv_to_array(self, csv):
        return [entry.strip() for entry in csv.split(',')]

class bedmas_file_io(file_io):
    
        '''
            expects a file in the format of bedmas-test.txt
            documentation of the format is in doc/bedmas_file_entry.md
        '''

        def to_array(self):
            array = []
            file = open(self.file_name, 'r')
            for line in file:
                if line.startswith('#') or line.startswith('\n') or line.startswith('\r'):
                    continue
                elif line.startswith('end') or not line:
                    break
                else:
                    array.append(self.csv_to_array(line.strip('\n').strip('\r').strip('[').strip(']')))
    
            return array

class csv_file_io(file_io):

    '''
        expects a csv file with numbers and operators lists on sepetate lines
    '''

    def to_array(self):
        array = []
        file = open(self.file_name, 'r')
        for line in file:
            array.append(self.csv_to_array(line.strip('\n').strip('\r')))

        return array
