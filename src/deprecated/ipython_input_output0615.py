Python 2.7.1+ (r271:86832, Apr 11 2011, 18:05:24) 
Type "copyright", "credits" or "license" for more information.                                                                                                
                                                                                                                                                              
IPython 0.10.1 -- An enhanced Interactive Python.                                                                                                             
?         -> Introduction and overview of IPython's features.                                                                                                 
%quickref -> Quick reference.                                                                                                                                 
help      -> Python's own help system.                                                                                                                        
object?   -> Details about 'object'. ?object also works, ?? prints more.                                                                                      
                                                                                                                                                              
In [1]: run ../../src/ncom_netcdf_global_ocean_export.py
 
In [2]: nf = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc')
                                                                                                                                                              
In [3]: nf.set                                                                                                                                                
nf.set_grid_region  nf.set_time_range                                                                                                                         
                                                                                                                                                              
In [3]: nf.set_grid_region()                                                                                                                                  
 
In [4]: nf.set 
nf.set_grid_region  nf.set_time_range                                                                                                                         

In [4]: nf.set_time_range() 
> /home/kjoyce/2011_summer/LCS_project/src/ncom_netcdf_global_ocean_export.py(48)set_time_range()
     47     debug_here()
---> 48     if (idx0 == idx1): #then both are zero
     49       self.t = self.infile.variables['time'][:]

ipdb> q 
Exiting Debugger.

In [5]: run ../../src/ncom_netcdf_global_ocean_export.py

In [6]: nf = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc')

In [7]: nf.se 
nf.set_grid_region  nf.set_time_range   

In [7]: nf.set_grid_region() 
 
In [8]: nf.set_time_range() 

In [9]: nf.lo 
nf.load_frame   nf.load_memory  nf.lon          

In [9]: nf.load 
nf.load_frame   nf.load_memory  

In [9]: nf.load_memory() 
 
In [10]: nf.in 
nf.infile            nf.interpolate_grid  

In [10]: nf.interpolate_grid() 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/src/ncom_netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

TypeError: interpolate_grid() takes exactly 2 arguments (1 given)

In [11]: nf.interpolate_grid(1) 
 
In [12]: nf.ui 
Out[12]: 
array([[[ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        ..., 
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan]],

       [[ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        ..., 
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan]],

       [[ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        ..., 
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan]],

       ..., 
       [[ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        ..., 
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan]],

       [[ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        ..., 
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan]],

       [[ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        ..., 
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan],
        [ nan,  nan,  nan, ...,  nan,  nan,  nan]]])

In [13]: plt.quiver(nf. 
nf._NcomNetcdf__set_cyl_basemap    nf.export_spherical_txt            nf.load_frame                      nf.t
nf._NcomNetcdf__set_stere_basemap  nf.export_stereo_txt               nf.load_memory                     nf.u
nf.__class__                       nf.get_time_readable               nf.lon                             nf.ui
nf.__doc__                         nf.grid_x                          nf.max_lat                         nf.v
nf.__init__                        nf.grid_y                          nf.max_lon                         nf.vi
nf.__module__                      nf.import_txt                      nf.min_lat                         nf.x
nf.basemap                         nf.infile                          nf.min_lon                         nf.y
nf.dirname                         nf.interpolate_grid                nf.set_grid_region                 
nf.export_nc                       nf.lat                             nf.set_time_range                  

In [13]: plt.quiver(nf.grid_x,nf.grid_y,nf.ui,nf.vi) 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/src/ncom_netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/usr/lib/pymodules/python2.7/matplotlib/pyplot.pyc in quiver(*args, **kw)
   2196         ax.hold(hold)
   2197     try:
-> 2198         ret = ax.quiver(*args, **kw)
   2199         draw_if_interactive()
   2200     finally:

/usr/lib/pymodules/python2.7/matplotlib/axes.pyc in quiver(self, *args, **kw)
   5873     def quiver(self, *args, **kw):
   5874         if not self._hold: self.cla()
-> 5875         q = mquiver.Quiver(self, *args, **kw)
   5876         self.add_collection(q, False)
   5877         self.update_datalim(q.XY)

/usr/lib/pymodules/python2.7/matplotlib/quiver.pyc in __init__(self, ax, *args, **kw)
    371     def __init__(self, ax, *args, **kw):
    372         self.ax = ax
--> 373         X, Y, U, V, C = _parse_args(*args)
    374         self.X = X
    375         self.Y = Y

/usr/lib/pymodules/python2.7/matplotlib/quiver.pyc in _parse_args(*args)
    341         nr, nc = 1, U.shape[0]
    342     else:
--> 343         nr, nc = U.shape
    344     if len(args) == 2: # remaining after removing U,V,C
    345         X, Y = [np.array(a).ravel() for a in args]

ValueError: too many values to unpack

In [14]: plt.quiver(nf.grid_x,nf.grid_y,nf.ui[0],nf.vi[0])
Out[14]: <matplotlib.quiver.Quiver object at 0xa2dd88c>

In [15]: plt.show() 
 
In [16]: nf.grid_x.shape 
Out[16]: (200, 400)

In [17]: nf.ui[0].shape 
Out[17]: (200, 400)

In [18]: nf.ui[0].shape 
Out[18]: (200, 400)

In [19]: plt.contourf(grid_x,grid_y,nf.ui[0]) 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/src/ncom_netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

NameError: name 'grid_x' is not defined

In [20]: plt.contourf(nf.grid_x,nf.grid_y,nf.ui[0])
Out[20]: <matplotlib.contour.ContourSet instance at 0xd8cfd8c>

In [21]: plt.figure() 
Out[21]: <matplotlib.figure.Figure object at 0xda4a24c>

In [22]: plt.contourf(nf.x,nf.y,nf.u[0]) 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/src/ncom_netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/usr/lib/pymodules/python2.7/matplotlib/pyplot.pyc in contourf(*args, **kwargs)
   1873         ax.hold(hold)
   1874     try:
-> 1875         ret = ax.contourf(*args, **kwargs)
   1876         draw_if_interactive()
   1877     finally:

/usr/lib/pymodules/python2.7/matplotlib/axes.pyc in contourf(self, *args, **kwargs)
   6842         if not self._hold: self.cla()
   6843         kwargs['filled'] = True
-> 6844         return mcontour.ContourSet(self, *args, **kwargs)
   6845     contourf.__doc__ = mcontour.ContourSet.contour_doc
   6846 

/usr/lib/pymodules/python2.7/matplotlib/contour.pyc in __init__(self, ax, *args, **kwargs)
    572             raise ValueError('Either colors or cmap must be None')
    573         if self.origin == 'image': self.origin = mpl.rcParams['image.origin']
--> 574         x, y, z = self._contour_args(*args)        # also sets self.levels,
    575                                                    #  self.layers

    576         if self.colors is not None:

/usr/lib/pymodules/python2.7/matplotlib/contour.pyc in _contour_args(self, *args)
    761             x, y = self._initialize_x_y(z)
    762         elif Nargs <=4:
--> 763             x,y,z = self._check_xyz(args[:3])
    764         else:
    765             raise TypeError("Too many arguments to %s; see help(%s)" % (fn,fn))

/usr/lib/pymodules/python2.7/matplotlib/contour.pyc in _check_xyz(self, args)
    742             return x,y,z
    743         if x.ndim != 1 or y.ndim != 1:
--> 744             raise TypeError("Inputs x and y must be 1D or 2D.")
    745         nx, = x.shape
    746         ny, = y.shape

TypeError: Inputs x and y must be 1D or 2D.

In [23]: nf.x.shape 
Out[23]: (200, 400)

In [24]: nf.u.shape 
Out[24]: (25, 400, 200)

In [25]: reset 
Once deleted, variables cannot be recovered. Proceed (y/[n])?  y 

In [26]: run ../../src/ncom_netcdf_global_ocean_export.py

In [27]: nf = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc')

In [28]: nf.set_time_range()

In [29]: nf.set_grid_region()
 
In [30]: nf.loa 
nf.load_frame   nf.load_memory  

In [30]: nf.load_memory() 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/src/ncom_netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/home/kjoyce/2011_summer/LCS_project/src/ncom_netcdf_global_ocean_export.py in load_memory(self)
     91     self.v = np.zeros( (Tlen,(x1-x0),(y1-y0)))
     92     for t in range(Tlen):
---> 93       self.u[t] = self.infile.variables['water_u'][t][0][y0:y1][:,x0:x1]
     94       self.v[t] = self.infile.variables['water_v'][t][0][y0:y1][:,x0:x1]
     95 

ValueError: shape mismatch: objects cannot be broadcast to a single shape

In [31]: run ../../src/ncom_netcdf_global_ocean_export.py

In [32]: nf = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc')

In [33]: nf.set_grid_region()
 
In [34]: nf.set_time_range() 

In [35]: nf.loa 
nf.load_frame   nf.load_memory  

In [35]: nf.load_memory() 
 
In [36]: plt.con 
plt.connect   plt.contour   plt.contourf  

In [36]: plt.cont 
plt.contour   plt.contourf  

In [36]: plt.contourf(nf.x,nf.y,nf.u[0]) 
Out[36]: <matplotlib.contour.ContourSet instance at 0xdd4134c>

In [37]: nf.interpolate_grid(1) 
 
In [38]: plt.figure() 
Out[38]: <matplotlib.figure.Figure object at 0xa12926c>

In [39]: nf.u 
nf.u   nf.ui  

In [39]: plt.quiver(nf.grid_x,nf.grid_y,nf.ui[0],nf.vi[0]) 
Out[39]: <matplotlib.quiver.Quiver object at 0xdde3d8c>

In [40]: nf.ui[0] 
Out[40]: 
array([[ nan,  nan,  nan, ...,  nan,  nan,  nan],
       [ nan,  nan,  nan, ...,  nan,  nan,  nan],
       [ nan,  nan,  nan, ...,  nan,  nan,  nan],
       ..., 
       [ nan,  nan,  nan, ...,  nan,  nan,  nan],
       [ nan,  nan,  nan, ...,  nan,  nan,  nan],
       [ nan,  nan,  nan, ...,  nan,  nan,  nan]])

In [41]: plt.cla() 
 
In [42]: plt.quiver(nf.grid_x[60:-60],nf.grid_y[60:-60],nf.ui[0][60:-60],nf.vi[0][60:-60])
Out[42]: <matplotlib.quiver.Quiver object at 0xddef92c>

In [43]: plt.cla() 

In [44]: plt.quiver(nf.grid_x[50:-50],nf.grid_y[50:-50],nf.ui[0][50:-50],nf.vi[0][50:-50])
Out[44]: <matplotlib.quiver.Quiver object at 0x1109f76c>

In [45]: plt.quiver? 
Type:             function
Base Class:       <type 'function'>
String Form:   <function quiver at 0xa0c6844>
Namespace:        Interactive
File:             /usr/lib/pymodules/python2.7/matplotlib/pyplot.py
Definition:       plt.quiver(*args, **kw)
Docstring:
    Plot a 2-D field of arrows.
    
    call signatures::
    
      quiver(U, V, **kw)
      quiver(U, V, C, **kw)
      quiver(X, Y, U, V, **kw)
      quiver(X, Y, U, V, C, **kw)
    
    Arguments:
    
      *X*, *Y*:
    
        The x and y coordinates of the arrow locations (default is tail of
        arrow; see *pivot* kwarg)
    
      *U*, *V*:
    
        give the *x* and *y* components of the arrow vectors
    
      *C*:
        an optional array used to map colors to the arrows
    
    All arguments may be 1-D or 2-D arrays or sequences. If *X* and *Y*
    are absent, they will be generated as a uniform grid.  If *U* and *V*
    are 2-D arrays but *X* and *Y* are 1-D, and if len(*X*) and len(*Y*)
    match the column and row dimensions of *U*, then *X* and *Y* will be
    expanded with :func:`numpy.meshgrid`.
    
    *U*, *V*, *C* may be masked arrays, but masked *X*, *Y* are not
    supported at present.
    
    Keyword arguments:
    
      *units*: ['width' | 'height' | 'dots' | 'inches' | 'x' | 'y' ]
        arrow units; the arrow dimensions *except for length* are in
        multiples of this unit.
    
        * 'width' or 'height': the width or height of the axes
    
        * 'dots' or 'inches': pixels or inches, based on the figure dpi
    
        * 'x' or 'y': *X* or *Y* data units
    
        The arrows scale differently depending on the units.  For
        'x' or 'y', the arrows get larger as one zooms in; for other
        units, the arrow size is independent of the zoom state.  For
        'width or 'height', the arrow size increases with the width and
        height of the axes, respectively, when the the window is resized;
        for 'dots' or 'inches', resizing does not change the arrows.
    
       *angles*: ['uv' | 'xy' | array]
        With the default 'uv', the arrow aspect ratio is 1, so that
        if *U*==*V* the angle of the arrow on the plot is 45 degrees
        CCW from the *x*-axis.
        * 'x' or 'y': *X* or *Y* data units
    Plot a 2-D field of arrows.
    
    call signatures::
    
      quiver(U, V, **kw)
      quiver(U, V, C, **kw)
      quiver(X, Y, U, V, **kw)
      quiver(X, Y, U, V, C, **kw)
    
    Arguments:
    
      *X*, *Y*:
    
        The x and y coordinates of the arrow locations (default is tail of
        arrow; see *pivot* kwarg)
    
      *U*, *V*:
    
        give the *x* and *y* components of the arrow vectors
    
      *C*:
        an optional array used to map colors to the arrows
    
    All arguments may be 1-D or 2-D arrays or sequences. If *X* and *Y*
    are absent, they will be generated as a uniform grid.  If *U* and *V*
    are 2-D arrays but *X* and *Y* are 1-D, and if len(*X*) and len(*Y*)
    match the column and row dimensions of *U*, then *X* and *Y* will be
    expanded with :func:`numpy.meshgrid`.
    
    *U*, *V*, *C* may be masked arrays, but masked *X*, *Y* are not
    supported at present.
    
    Keyword arguments:
    
      *units*: ['width' | 'height' | 'dots' | 'inches' | 'x' | 'y' ]
        arrow units; the arrow dimensions *except for length* are in
        multiples of this unit.
    
        * 'width' or 'height': the width or height of the axes
    
        * 'dots' or 'inches': pixels or inches, based on the figure dpi
    
        * 'x' or 'y': *X* or *Y* data units
    
        The arrows scale differently depending on the units.  For
        'x' or 'y', the arrows get larger as one zooms in; for other
        units, the arrow size is independent of the zoom state.  For
        'width or 'height', the arrow size increases with the width and
        height of the axes, respectively, when the the window is resized;
        for 'dots' or 'inches', resizing does not change the arrows.
    
       *angles*: ['uv' | 'xy' | array]
        With the default 'uv', the arrow aspect ratio is 1, so that
        if *U*==*V* the angle of the arrow on the plot is 45 degrees
        CCW from the *x*-axis.
        With 'xy', the arrow points from (x,y) to (x+u, y+v).
        Alternatively, arbitrary angles may be specified as an array
        of values in degrees, CCW from the *x*-axis.
    
      *scale*: [ None | float ]
        data units per arrow unit, e.g. m/s per plot width; a smaller
        scale parameter makes the arrow longer.  If *None*, a simple
        autoscaling algorithm is used, based on the average vector length
        and the number of vectors.
    
      *width*:
        shaft width in arrow units; default depends on choice of units,
        above, and number of vectors; a typical starting value is about
        0.005 times the width of the plot.
    
      *headwidth*: scalar
        head width as multiple of shaft width, default is 3
    
      *headlength*: scalar
        head length as multiple of shaft width, default is 5
    
      *headaxislength*: scalar
        head length at shaft intersection, default is 4.5
    
      *minshaft*: scalar
        length below which arrow scales, in units of head length. Do not
        set this to less than 1, or small arrows will look terrible!
        Default is 1
    
        CCW from the *x*-axis.
        With 'xy', the arrow points from (x,y) to (x+u, y+v).
        Alternatively, arbitrary angles may be specified as an array
        of values in degrees, CCW from the *x*-axis.
    
      *scale*: [ None | float ]
        data units per arrow unit, e.g. m/s per plot width; a smaller
        scale parameter makes the arrow longer.  If *None*, a simple
        autoscaling algorithm is used, based on the average vector length
        and the number of vectors.
    
      *width*:
        shaft width in arrow units; default depends on choice of units,
        above, and number of vectors; a typical starting value is about
        0.005 times the width of the plot.
    
      *headwidth*: scalar
        head width as multiple of shaft width, default is 3
    

In [46]: plt.figure() 
Out[46]: <matplotlib.figure.Figure object at 0xddb7e6c>

In [47]: plt.quiver(nf.grid_x[50:-50],nf.grid_y[50:-50],nf.ui[0][50:-50],nf.vi[0][50:-50],scale=.5)
Out[47]: <matplotlib.quiver.Quiver object at 0x141b6f4c>

In [48]: plt.cla() 

In [49]: plt.quiver(nf.grid_x[50:-50],nf.grid_y[50:-50],nf.ui[0][50:-50],nf.vi[0][50:-50],scale=1)
Out[49]: <matplotlib.quiver.Quiver object at 0x141c4f0c>

In [50]: plt.cla() 

In [51]: plt.quiver(nf.grid_x[50:-50],nf.grid_y[50:-50],nf.ui[0][50:-50],nf.vi[0][50:-50],scale=10)
Out[51]: <matplotlib.quiver.Quiver object at 0x15b4df4c>

In [52]: plt.cla() 

In [53]: plt.quiver(nf.grid_x[50:-50],nf.grid_y[50:-50],nf.ui[0][50:-50],nf.vi[0][50:-50],scale=50)
Out[53]: <matplotlib.quiver.Quiver object at 0x15b4dd6c>

In [54]: plt.quiver? 
Type:             function
Base Class:       <type 'function'>
String Form:   <function quiver at 0xa0c6844>
Namespace:        Interactive
File:             /usr/lib/pymodules/python2.7/matplotlib/pyplot.py
Definition:       plt.quiver(*args, **kw)
Docstring:
    Plot a 2-D field of arrows.
    
    call signatures::
    
      quiver(U, V, **kw)
      quiver(U, V, C, **kw)
      quiver(X, Y, U, V, **kw)
      quiver(X, Y, U, V, C, **kw)
    
    Arguments:
    
      *X*, *Y*:
    
        The x and y coordinates of the arrow locations (default is tail of
        arrow; see *pivot* kwarg)
    
      *U*, *V*:
    
        give the *x* and *y* components of the arrow vectors
    
      *C*:
        an optional array used to map colors to the arrows
    
    All arguments may be 1-D or 2-D arrays or sequences. If *X* and *Y*
    are absent, they will be generated as a uniform grid.  If *U* and *V*
    are 2-D arrays but *X* and *Y* are 1-D, and if len(*X*) and len(*Y*)
    match the column and row dimensions of *U*, then *X* and *Y* will be
    expanded with :func:`numpy.meshgrid`.
    
    *U*, *V*, *C* may be masked arrays, but masked *X*, *Y* are not
    supported at present.
    
    Keyword arguments:
    
      *units*: ['width' | 'height' | 'dots' | 'inches' | 'x' | 'y' ]
        arrow units; the arrow dimensions *except for length* are in

In [55]: plt.cla()
 
In [56]: plt.quiver(nf.grid_x[50:-50],nf.grid_y[50:-50],nf.ui[0][50:-50],nf.vi[0][50:-50],scale=25)
Out[56]: <matplotlib.quiver.Quiver object at 0x1aedf4cc>

In [57]: run ../../src/ncom_netcdf_global_ocean_export.py

In [58]: nf = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc')

In [59]: nf.set_ 
nf.set_grid_region  nf.set_time_range   

In [59]: nf.set_grid_region() 
--Return--
None
> /home/kjoyce/2011_summer/LCS_project/src/ncom_netcdf_global_ocean_export.py(154)__set_stere_basemap()
    153     self.x,self.y = self.basemap(*np.meshgrid(self.lon,self.lat))
--> 154     debug_here()
    155 

ipdb> plt.figure() 
<matplotlib.figure.Figure object at 0xdd40c0c>
ipdb> plt.contourf(x,y,np.ones(x.shape)) 
<matplotlib.contour.ContourSet instance at 0x1ac2862c>
ipdb> q 
Exiting Debugger.
 
In [60]:  
