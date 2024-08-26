from model.point import Point
from typing import Optional

# Going to assume there's only 2 sets of RGBa values. Modify this function if there are more.


def parse_ply_file(file_path: str) -> list[Point]:
    # Initialize empty arrays for points
    points: list[Point] = []

    # Read the file
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")

    header_end_index = 0
    for i, line in enumerate(lines):
        if line.startswith("end_header"):
            header_end_index = i
            break
    has_color = any(attr in headers for attr in [
                    "road_colour_a", "ground_colour_a"] for headers in lines[:header_end_index])

    # Parse the lines starting from the 15th line
    from_line = header_end_index + 1
    for line in lines[from_line:]:
        # Split the line by whitespace
        values = line.split()

        # Extract the x, y, z coordinates
        x = float(values[0])
        y = float(values[1])
        z = float(values[2])

        # Default values for color and intensity
        colour: list[float] = []
        intensity: float = 0
        if has_color:
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
                colour = [r2, g2, b2]
                intensity = i2
            else:
                colour = [r1, g1, b1]
                intensity = i1
        # Create a Point object and append it to the points array
        point = Point(x, y, z)
        if len(colour) > 0 and intensity != 0:
            point = Point(x, y, z, colour, intensity)
        points.append(point)
    return points
