from typing import Optional


class Point:
    def __init__(
        self,
        x: float,
        y: float,
        z: float,
        rgb: list[float] = [0, 0, 0],
        intensity: float = 0,
    ):
        self.x = x
        self.y = y
        self.z = z
        self.intensity = intensity
        self.rgb = rgb
