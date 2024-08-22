import open3d as o3d
from model.point import Point
import numpy as np


def create_point_cloud(points: list[Point]) -> o3d.geometry.PointCloud:
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(
        [[point.x, point.y, point.z] for point in points]
    )
    point_cloud.colors = o3d.utility.Vector3dVector([point.rgb for point in points])

    return point_cloud


def append_to_point_cloud(
    point_cloud: o3d.geometry.PointCloud, points: list[Point]
) -> None:
    point_cloud.points.extend(
        o3d.utility.Vector3dVector([[point.x, point.y, point.z] for point in points])
    )
    point_cloud.colors.extend(
        o3d.utility.Vector3dVector([np.float(point.rgb) for point in points])
    )
