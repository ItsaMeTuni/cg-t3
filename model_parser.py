from model import Model

def parse_model(file_path):
    file = open(file_path)

    # skip first line
    file.readline()

    colors = []
    color_count = int(file.readline())
    for _ in range(color_count):
        channels = split(file.readline(), ' ')
        colors.append((channels[0], channels[1], channels[2]))

    # skip blank line
    file.readline()

    # skip section name
    file.readline()
   
    pixels = []
    [row_count, col_count] = split(file.readline(), ' ')
    for _ in range(row_count):
        row_pixels = [int(pixel) for pixel in split(file.readline(), ' ')]
        pixels.extend(row_pixels)

    return Model(col_count, row_count, colors, pixels)
