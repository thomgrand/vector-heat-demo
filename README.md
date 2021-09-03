# vector-heat-demo
C++ demo of the Vector Heat Method (Sharp, Soliman, and Crane. 2019.)

The Vector Heat Method is implemented in [geometry-central](http://geometry-central.net), this is just a simple application to demonstrate the functionality.

See also the geometry-central documentation for [the Vector Heat Method](http://geometry-central.net/surface/algorithms/vector_heat_method/) and [centers on surfaces](http://geometry-central.net/surface/algorithms/surface_centers/).

![demo git](https://github.com/nmwsharp/vector-heat-demo/blob/master/vector_heat_demo.gif)

## Branch Note

This branch additionally enables the export of the transported vector(s) and the logmap, found on the right side of the GUI. The results will be written in csv-files. [load_exported_vector_transport.py](load_exported_vector_transport.py) demonstrates how to import the transported vector(s) in numpy with an optional visualization in [pyvista](https://www.pyvista.org).

### Building and running

```
git clone --recurse-submodules https://github.com/nmwsharp/vector-heat-demo.git
cd vector-heat-demo
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j4
./bin/vector_heat /path/to/your/mesh.obj
```

This will open a UI window showing your mesh. The command window in the upper right can be used to run the algorithms, while the window on the left adjusts visualization setting. Note that both transport sources and averaging sites can be selected in these windows; some arbtrirary vertices are selected initially.
