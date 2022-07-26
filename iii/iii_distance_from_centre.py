import svgwrite
import random
import math

width = 100
height = 100
dwg = svgwrite.Drawing(
  'test.svg', 
  size=(width, height), 
  profile='tiny', 
  stroke_width=0.15,
  stroke='black',
  stroke_opacity=1.0,
  fill='none'
)

subdivision_probability = 0.6
ignore_count = 2

def get_probability(position, square_width, square_height):
    centre_of_square = (position[0] + square_width/2, position[1] + square_height/2)
    centre = (width/2, height/2)
    distance_from_centre = math.sqrt(abs(centre[0] - centre_of_square[0])**2 + abs(centre[1] - centre_of_square[1])**2)
    max_distance = math.sqrt((width/2)**2 + (height/2)**2)
    return distance_from_centre/max_distance

def draw_square_or_subdivide(position, width, height, depth, ignore_count):
    subdivision_probability = get_probability(position, width, height)
    if depth < 7 and random.random() < subdivision_probability or ignore_count > 0:
        ignore_count -= 1
        new_depth = depth + 1
        return subdivide(position, width, height, new_depth, ignore_count)
    color_fill = choose_fill()
    return dwg.rect(position, (width, height), fill=color_fill)

def choose_fill():
    n = random.random()
    if n > 0.98: return "#00ecff"
    if n > 0.96: return "#f300c8"
    if n > 0.94: return "#ffe321"
    if n > 0.9: return "#000000"
    return "#ffffff"

def subdivide(position, width, height, depth, ignore_count):
    group = dwg.g()
    for x in range(0, 2):
        for y in range(0, 2):
            square_width = width/2
            square_height = height/2
            x_position = position[0] + (x * square_width)
            y_position = position[1] + (y * square_height)
            square_position = (x_position, y_position)
            group.add(draw_square_or_subdivide(square_position, square_width, square_height, depth, ignore_count))
    return group

dwg.add(subdivide((0,0), width, height, 0, 1))
dwg.saveas("iii105.svg")

### 007 series - increasing subdisivion chance
### 100 series - distance from centre = probability

## TODO: probability based on proximity to the centre - maybe colour probability in particular corners?