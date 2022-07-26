import svgwrite
import random

dwg = svgwrite.Drawing(
  'test.svg', 
  size=(100, 100), 
  profile='tiny', 
  stroke_width=0.5,
  stroke='black',
  stroke_opacity=1.0,
  fill='none'
)

width = 10
height = 20
position_dampener = 400
rotation_dampener = 15

one_dp = lambda x: "{:.1f}".format(x)
random_magnitude = lambda x,y : (random.random() - 0.5) * (x + (y * width)) * y
random_position_magnitude = lambda x,y : random_magnitude(x,y) / position_dampener

for i in range(0, 10):
    group = dwg.g()
    for x in range(0, width):
        for y in range(0, height):
            position_modifier_x = random_position_magnitude(x,y)
            x_position = x * 10 + position_modifier_x

            position_modifier_y = random_position_magnitude(x,y)
            y_position = y * 10 + position_modifier_y

            rotation = one_dp(random_magnitude(x,y) / rotation_dampener)

            group.add(dwg.rect(
                (one_dp(x_position),one_dp(y_position)
                ),
                (10,10),
                transform = f"rotate({rotation},{one_dp(x_position + 5)},{one_dp(y_position + 5)})"
            ))
    dwg.add(group)

dwg.saveas("shotterGroup.svg")