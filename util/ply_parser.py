from model.point import Point


# Going to assume there's only 2 sets of RGBa values. Modify this function if there are more.
def parse_ply_file(file_path: str, from_line: int = 19) -> list[Point]:
    # Initialize empty arrays for points
    points: list[Point] = []

    # Read the file
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")

    # Parse the lines starting from the 15th line
    for line in lines[from_line:]:
        # Split the line by whitespace
        values = line.split()

        # Extract the x, y, z coordinates
        x = float(values[0])
        y = float(values[1])
        z = float(values[2])

        # Extract the first set of RGBa color values
        r1 = float(values[4])
        g1 = float(values[5])
        b1 = float(values[6])
        i1 = float(values[7])

        # skip UV_x and UV_y

        r2 = float(values[10])
        g2 = float(values[11])
        b2 = float(values[12])
        i2 = float(values[13])

        # data isn't clean, it stores colour values for road and ground in the same line, extract non 0 ones.
        if r1 == 0 and g1 == 0 and b1 == 0 and i1 == 0:
            r = r2
            g = g2
            b = b2
            intensity = i2
        else:
            r = r1
            g = g1
            b = b1
            intensity = i1

        # Create a Point object and append it to the points array
        point = Point(x, y, z, [r, g, b], intensity)
        points.append(point)

    return points
