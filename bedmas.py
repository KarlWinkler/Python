import file_io as io
import operator

debug = True

class bedmas_calculator:
    '''
        expects a list were each pair of entries is a list of numbers and a list of operators
        expects input reader to implement read_to_array()
    '''
    def __init__(self, input_reader):
        self.input_reader = input_reader

    def calculate(self):    
        in_array = self.input_reader.to_array()
        out_array = []
        print(in_array)
        i = 0
        while i < len(in_array):
            out_array.append(self.calculate_recursive(in_array[i], in_array[i+1]))
            i += 2

        return out_array             

    def calculate_recursive(self, nums, operators):
        if debug:
            print(nums)
            print(operators)

        self.proccess_brackets(nums, operators)
        if debug:
            print('brackets')
            print(nums)
            print(operators)

        self.calculate_step(nums, operators, ['^', '**'])
        if debug:
            print('exponents')
            print(nums)
            print(operators)

        self.calculate_step(nums, operators, ['*', '/', '//', '%'])
        if debug:
            print('multiplication')
            print(nums)
            print(operators)

        self.calculate_step(nums, operators, ['+', '-'])
        if debug:
            print('addition')
            print(nums)
            print(operators)

        return nums[0]

    def proccess_brackets(self, nums, operators):
        i = 0
        while i < len(operators):
            if operators[i].find('(') >= 0:
                operators[i] = operators[i].replace("(","",1)
                j = i
                bracket_counter = 1
                while j < len(operators):
                    if operators[j].find('(') >= 0:
                        bracket_counter += 1
                    if operators[j].find(')') >= 0:
                        if bracket_counter > 1:
                            bracket_counter -= 1
                        else:
                            operators[j] = operators[j].replace(")","",1)
                            calc = self.calculate_recursive(nums[i:j + 2], operators[i:j + 1])
                            del nums[i:j + 2]
                            del operators[i:j + 1]
                            nums.insert(i, calc)
                    j += 1
            i += 1

    def calculate_step(self, nums, operators, ops):
        i = 0
        while i < len(operators):
            if operators[i] in ops:
                calc = self.eval_expr(nums[i], operators[i], nums[i+1])
                del nums[i:i+2]
                del operators[i]
                nums.insert(i, calc)
                i -= 1
            i += 1

    def eval_expr(self, num1, op, num2):
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
            '//' : operator.floordiv,
            '%' : operator.mod,
            '^' : operator.pow,
            '**' : operator.pow
        }
        num1, num2 = float(num1), float(num2)
        return ops[op](num1, num2)

# file_io = io.bedmas_file_io('bedmas-test.txt')
file_io = io.csv_file_io('bedmas-csv.csv')

calc = bedmas_calculator(file_io)
calc_res = calc.calculate()   

i = 1
for res in calc_res:
    print(f"result of equation {i} is {res}")
    i += 1
