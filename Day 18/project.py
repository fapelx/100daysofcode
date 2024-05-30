import os
import colorgram

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the image file
image_path = os.path.join(current_dir, 'damien.jpg')

# Extract colors from the image
colors = colorgram.extract(image_path, 30)
rgb_colors = []
# Print the RGB values of the extracted colors
for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  new_color = (r,g,b)
  if r < 235 and g < 235 and b < 235:
      rgb_colors.append(new_color)
print(rgb_colors)