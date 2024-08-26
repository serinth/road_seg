import open3d as o3d


pc = o3d.io.read_point_cloud("./data/basic.ply")
vis = o3d.visualization.VisualizerWithEditing()


print("1) Please pick at least three correspondences using [shift + left click]")
print("   Press [shift + right click] to undo point picking")
print("2) After picking points, press 'Q' to close the window")
vis.create_window()
vis.add_geometry(pc)
vis.run()  # user picks points
vis.destroy_window()
print("---------")
vis.get_picked_points()
