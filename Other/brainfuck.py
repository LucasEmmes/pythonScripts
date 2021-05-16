from os import error
import sys

class brainfuck:
    def __init__(self):
        self.cells = [0]
        self.pointer = 0

    def increment(self):
        self.cells[self.pointer] = self.cells[self.pointer] + 1 % 256

    def decrement(self):
        self.cells[self.pointer] = self.cells[self.pointer] - 1 % 256
    
    def move_right(self):
        self.pointer += 1
        if self.pointer == len(self.cells):
            self.cells.append(0)
    
    def move_left(self):
        self.pointer -= 1
        if self.pointer < 0:
            self.pointer = 0
            self.cells.insert(0,0)
    
    def print_cell(self):
        print(chr(self.cells[self.pointer]), end="")
    
    def get_input(self):
        char = input()
        self.cells[self.pointer] = (ord(char[0]) if len(char) > 0 else 0) % 256
    
    def run_loop(self):
        return self.cells[self.pointer]

        
def execute(filename):
    bf = brainfuck()
    f = open(filename)
    data = f.read()
    f.close()
    i = 0
    loop_stack = []
    loop_counter = 0
    while i < len(data):
        command = data[i]

        if command == ">":
            bf.move_right()

        elif command == "<":
            bf.move_left()

        elif command == "+":
            bf.increment()

        elif command == "-":
            bf.decrement()

        elif command == ".":
            bf.print_cell()

        elif command == ",":
            bf.get_input()

        elif command == "[":
            if bf.run_loop():
                loop_stack.append(i-1)
            else:
                loop_counter = 1
                while loop_counter != 0:
                    i += 1
                    if data[i] == "[":
                        loop_counter += 1
                    elif data[i] == "]":
                        loop_counter -= 1

        elif command == "]":
            i = loop_stack.pop()

        elif command == "\n":
            pass
        
        else:
            print(f"Cannot parse command '{command}'. Please re-read the napkin that people call the BrainFuck documentation")
            raise error("Fuck u")
        
        i += 1

def main():
  if len(sys.argv) == 2: execute(sys.argv[1])
  else: print("Usage:", sys.argv[0], "filename")

if __name__ == "__main__": main()