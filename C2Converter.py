from PIL import Image
from xlwt import Workbook

wb = Workbook()
graph = wb.add_sheet('Sheet 1')
img = Image.open("Input.png")
img = img.convert('RGB')
map = img.load()
colors = {}
num = 0
width, height = img.size
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        color = colors.get(f'{r}, {g}, {b}')
        if color:
            graph.write(y, x, color)
        else:
            num += 1
            colors[f'{r}, {g}, {b}'] = num
            graph.write(y, x, colors[f'{r}, {g}, {b}'])

wb.save('Output.xls')