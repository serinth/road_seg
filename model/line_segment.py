from model.point import Point
from typing import Optional


class LineSegment:
    def __init__(self, points: list[Point], indices: Optional[list[int, int]] = None):
        self.points = points

        # tells us how the points are connected
        self.line_indices = indices

    def get_line_indices(self) -> list[list[int, int]]:
        if self.line_indices:
            return self.line_indices
        else:
            return [[i, i + 1] for i in range(len(self.points) - 1)]
