#This file demonstrates how to load the result of the export in numpy
import numpy as np

def load_pts_data(f, nr_pts):
    return np.stack([np.fromstring(f.readline(), sep=" ") for pts_i in range(nr_pts)], axis=0)

with open("vector_transport_export.csv", "r") as f:
    nr_pts = int(f.readline())
    vertices = load_pts_data(f, nr_pts)
    tangent_vecs = load_pts_data(f, nr_pts)
    transported_vec = load_pts_data(f, nr_pts)
    
transported_vec_3D = tangent_vecs[..., :3] * transported_vec[..., 0:1] + tangent_vecs[..., 3:] * transported_vec[..., 1:2]

#transported_vec_3D will hold the transported vector(s) in cartesian coordinates

#Plot using pyvista (optional)
"""
import pyvista as pv
geom = pv.Arrow()
pd = pv.PolyData(vertices)
pd.point_arrays["transported_vec_3D"] = transported_vec_3D
pd.set_active_vectors("transported_vec_3D")
glyphs = pd.glyph(geom=geom)
# plot using the plotting class
p = pv.Plotter()
p.add_mesh(glyphs)
p.show()
"""