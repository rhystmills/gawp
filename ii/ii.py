import svgwrite
import random
import math

dwg = svgwrite.Drawing(
  'test.svg', 
  size=(100, 100), 
  profile='tiny', 
  stroke_width=1,
  stroke='black',
  stroke_opacity=1.0,
  fill='none'
)

# For n times
# Pick either x or y direction
# Return an array of all valid positions on that axis
# If there are none, do the other axis
# Pick one of those points  and draw a line to it from the previous point (if it's an acceptable point) 

width = 80
height = 80

# draw line: dwg.add(dwg.line((0, 0), (10, 0)))

def pick_x_or_y():
    if random.random() < 0.5: 
        return 'x'
    return 'y'

def is_valid(current_point):
    return True
    centre = (width/2, height/2)
    x = abs(centre[0] - current_point[0])
    y = abs(centre[1] - current_point[1])
    if math.sqrt(x**2 + y**2) < width/2 and (current_point[1] < width/4 or current_point[1] > 3 * width/4):
        return True 
    return False 

def get_valid_positions(axis, current_point):
    positions = [] 
    if axis == 'x':
        for i in range (0, width):
            possible_next_point = (i, current_point[1])
            if (is_valid(possible_next_point)):
                positions.append(possible_next_point)
        if not positions:
            return get_valid_positions('y', current_point)
        return positions
    if axis == 'y':
        for i in range (0, width):
            possible_next_point = (current_point[0], i)
            if (is_valid(possible_next_point)):
                positions.append(possible_next_point)
        if not positions:
            return get_valid_positions('x', current_point)
        return positions

def create_list_of_points(current_n, max_n, first_point):
    new_list = []
    current_point = first_point
    for n in range(current_n, max_n):
        axis = pick_x_or_y()
        valid_positions = get_valid_positions(axis, current_point)
        next_point = random.choice(valid_positions)
        current_point = next_point
        new_list.append(next_point)
    return new_list

def generate_valid_start_point():
    point = (random.randint(0,width), random.randint(0,height))
    if is_valid(point):
        return point
    return generate_valid_start_point()

list_of_points = create_list_of_points(0, 300, generate_valid_start_point())
dwg.add(dwg.polyline(points=list_of_points, stroke='#00ecff'))
list_of_points = create_list_of_points(0, 300, generate_valid_start_point())
dwg.add(dwg.polyline(points=list_of_points, stroke='#f300c8'))
list_of_points = create_list_of_points(0, 300, generate_valid_start_point())
dwg.add(dwg.polyline(points=list_of_points, stroke='#ffe321'))

dwg.saveas("iiPlot116.svg")

# TODO: Multiple different coloured lines
# TODO: DONUT


# idea: recursive cubes!!