class cube:
    def __init__(self):
        self.top = [0]*9
        self.bottom = [1]*9
        self.left = [2]*9
        self.right = [3]*9
        self.front = [4]*9
        self.back = [5]*9
    
    def formatted_print(self):
        formatted_string = ""
        for i in range(3):
            formatted_string += f"{self.left[3*i:3*i+3]} {self.top[3*i:3*i+3]} {self.right[3*i:3*i+3]}\n"
        formatted_string += "\n"
        temp_arr = [self.front, self.bottom, self.back]
        for side in temp_arr:
            for i in range(3):
                formatted_string += f"{side[3*i:3*i+3]}\n".rjust(20, " ")
            formatted_string += "\n"
        
        return formatted_string

    # def rotate_face(self, amount, side):
    #     temp_arr = side[0:3] + [side[5]] + side[8:5:-1] + [side[3]]

    #     for i in range(amount):
    #         for j in range(2):
    #             temp_arr.insert(0, temp_arr.pop())
    
    def rotate(self, direction, unwrapped_cube, angle):
        # unwrapped_cube: [top, front, bottom, back, left, right]
        # angle: what side is facing you e.g. front (0) / right (1) / back (2) / left (3)

        # extract col to modify
        rotating_column = unwrapped_cube[0:4]
        column_values = []
        for side in rotating_column:
            for i in range(3):
                column_values.append(side[i*3])
        
        # modify
        for i in range(3):
            if direction == -1:
                # ROTATE LEFT BY 1 - L
                column_values.append(column_values.pop(0))
            else:
                # ROTATE RIGHT BY 1 - L'
                column_values.insert(0, column_values.pop())


        # put back
        counter = 0
        for side in rotating_column:
            for i in range(3):
                side[i*3] = column_values[counter * 3 + i]
            counter += 1

        # rotate left side
        side = unwrapped_cube[4]
        temp_arr = side[0:3] + [side[5]] + side[8:5:-1] + [side[3]]

        for i in range(2):
            # left side
            if direction == -1:
                temp_arr.append(temp_arr.pop(0))
            else:
                temp_arr.insert(0, temp_arr.pop())


        # put that shit right back
        side[0:3] = temp_arr[0:3]
        side[5] = temp_arr[3]
        side[8:5:-1] = temp_arr[4:7]
        side[3] = temp_arr[7]

        
    def l(self, direction):
        self.rotate(direction, [self.top, self.front, self.bottom, self.back, self.left, self.right])
    
    def r(self, direction):
        self.rotate(direction, [self.top, self.back, self.bottom, self.front, self.right, self.left])





c = cube()
c.left = [0,1,2,3,4,5,6,7,8]
c.right = [0,1,2,3,4,5,6,7,8]
c.r(1)
print(c.formatted_print())