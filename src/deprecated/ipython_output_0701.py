Python 2.7.1+ (r271:86832, Apr 11 2011, 18:05:24) 
Type "copyright", "credits" or "license" for more information.                                                                                                
                                                                                                                                                              
IPython 0.10.1 -- An enhanced Interactive Python.                                                                                                             
?         -> Introduction and overview of IPython's features.                                                                                                 
%quickref -> Quick reference.                                                                                                                                 
help      -> Python's own help system.                                                                                                                        
object?   -> Details about 'object'. ?object also works, ?? prints more.                                                                                      
 
In [1]: run netcdf_global_ocean_export.py 
 
In [2]: nfile = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc')
 
In [3]: nfile.set_grid_region() 
Out[3]: <__main__.NcomNetcdf instance at 0xa170a4c>

In [4]: def test_len(n): 
   ...:   return dist( (nfile.x[0][n],nfile.y[0][n]) , (nfile.x[-1][n],nfile.y[-1][n]) )                                                                      
   ...:                                                                                                                                                       
In [5]: y = [test_len(i) for i in range(400)] 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in test_len(n)
      1 
----> 2 
      3 
      4 
      5 

NameError: global name 'dist' is not defined

In [6]: def dist(x1,x2): 
   ...:   return np.sqrt( ( x1[0] - x2[0] )**2 + (x1[1] - x2[1])**2 )  
   ...:  

In [7]: y = [test_len(i) for i in range(400)] 

In [8]: plt.plot(range(400),y) 
Out[8]: [<matplotlib.lines.Line2D object at 0xae5702c>]

In [9]: plt.show() 
 
 
In [10]:  

In [11]: xx,yy = stereo_proj(nfile.lon,nfile.lat) 
 
In [12]: R = 6378.1e3

In [13]: xx = R*xx 

In [14]: yy = R*yy 

In [15]: def test_len2(n):                     
  return dist( (xx[0][n],yy[0][n]) , (xx[-1][n],yy[-1][n]) )
   ....:  

In [17]: y2 = [test_len2(i) for i in range(400)]

In [18]: plt.plot(range(400),(y,y2))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/usr/lib/pymodules/python2.7/matplotlib/pyplot.pyc in plot(*args, **kwargs)
   2139         ax.hold(hold)
   2140     try:
-> 2141         ret = ax.plot(*args, **kwargs)
   2142         draw_if_interactive()
   2143     finally:

/usr/lib/pymodules/python2.7/matplotlib/axes.pyc in plot(self, *args, **kwargs)
   3430         lines = []
   3431 
-> 3432         for line in self._get_lines(*args, **kwargs):
   3433             self.add_line(line)
   3434             lines.append(line)

/usr/lib/pymodules/python2.7/matplotlib/axes.pyc in _grab_next_args(self, *args, **kwargs)
    309                 return
    310             if len(remaining) <= 3:
--> 311                 for seg in self._plot_args(remaining, kwargs):
    312                     yield seg
    313                 return

/usr/lib/pymodules/python2.7/matplotlib/axes.pyc in _plot_args(self, tup, kwargs)
    286             x = np.arange(y.shape[0], dtype=float)
    287 
--> 288         x, y = self._xy_from_xy(x, y)
    289 
    290         if self.command == 'plot':

/usr/lib/pymodules/python2.7/matplotlib/axes.pyc in _xy_from_xy(self, x, y)
    226         y = np.atleast_1d(y)
    227         if x.shape[0] != y.shape[0]:
--> 228             raise ValueError("x and y must have same first dimension")
    229         if x.ndim > 2 or y.ndim > 2:
    230             raise ValueError("x and y can be no greater than 2-D")

ValueError: x and y must have same first dimension

In [19]: plt.plot(range(400),y2)
Out[19]: [<matplotlib.lines.Line2D object at 0xb3373ac>]

In [20]: plt.plot(range(400),y)
Out[20]: [<matplotlib.lines.Line2D object at 0xb0c34ac>]

In [21]: plt.clf() 

In [22]: plt.quiver(xx,yy,nfile.u,nfile.v) 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
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

In [23]: plt.quiver(xx,yy,nfile.u[0],nfile.v[0])
Out[23]: <matplotlib.quiver.Quiver object at 0xaf5dd4c>

In [24]: plt.figure() 
Out[24]: <matplotlib.figure.Figure object at 0xb3605cc>

In [25]: plt.quiver(nfile.x,nfile.y,nfile.u[0],nfile.v[0]) 
Out[25]: <matplotlib.quiver.Quiver object at 0xe5eedac>

In [26]: plt.figure() 
Out[26]: <matplotlib.figure.Figure object at 0xe5bc46c>

In [27]: nfile.basemap.quiver(nfile.x,nfile.y,nfile.u[0],nfile.v[0]) 
Out[27]: <matplotlib.quiver.Quiver object at 0x118ca72c>

In [28]: bm = Basemap(projection = 'stere',
   ....:                 lon_0 = .5*( self.lon[0] - self.lon[-1]),
   ....:                 lat_0 = .5*( self.lat[0] - self.lat[-1]),
   ....:                 width=40000000,
Display all 281 possibilities? (y or n)
ArithmeticError                              _i20                                         ipython_output_0603.py
AssertionError                               _i21                                         is
AttributeError                               _i22                                         isinstance
BaseException                                _i23                                         issubclass
Basemap                                      _i24                                         iter
BufferError                                  _i25                                         jobs
BytesWarning                                 _i26                                         lambda
DeprecationWarning                           _i27                                         lc
EOFError                                     _i28                                         ldir
Ellipsis                                     _i3                                          len
EnvironmentError                             _i4                                          less
Exception                                    _i5                                          lf
False                                        _i6                                          license
FloatingPointError                           _i7                                          list
FutureWarning                                _i8                                          lk
GeneratorExit                                _i9                                          ll
IOError                                      _ih                                          locals
ImportError                                  _ii                                          long
ImportWarning                                _iii                                         ls
In                                           _ip                                          lx
IndentationError                             _oh                                          map
IndexError                                   _sh                                          max
KeyError                                     abs                                          memoryview
KeyboardInterrupt                            all                                          min
LookupError                                  and                                          mkdir
MemoryError                                  any                                          mv
NameError                                    apply                                        nc
NcomNetcdf                                   as                                           ncom_glb_sfcurrents_2011060600
NcomTime                                     assert                                       ncom_glb_sfcurrents_2011060600.nc
None                                         basestring                                   ncom_glb_sfcurrents_2011060600.zip
NotImplemented                               bin                                          ncom_glb_sfcurrents_2011060600_AK_stereo.nc
NotImplementedError                          bool                                         ncom_glb_sfcurrents_2011060900.nc
OSError                                      break                                        ncom_glb_sfcurrents_2011060900.nc.gz
Out                                          buffer                                       netcdf_global_ocean_export.py
OverflowError                                bytearray                                    netcdf_global_ocean_export.pyc
PendingDeprecationWarning                    bytes                                        next
R                                            callable                                     nfile
ReferenceError                               cat                                          not
RuntimeError                                 chr                                          np
RuntimeWarning                               class                                        object
StandardError                                classmethod                                  oct
StopIteration                                clear                                        open
SyntaxError                                  cmp                                          or
SyntaxWarning                                coerce                                       ord
SystemError                                  compile                                      os
SystemExit                                   complex                                      pass
TabError                                     continue                                     plt
True                                         copyright                                    pow
TypeError                                    cp                                           print
UnboundLocalError                            credits                                      property
UnicodeDecodeError                           datetime                                     quit
UnicodeEncodeError                           def                                          raise
UnicodeError                                 del                                          range
UnicodeTranslateError                        delattr                                      raw_input
UnicodeWarning                               dict                                         reduce
UserWarning                                  dir                                          region.png
ValueError                                   dist                                         reload
Warning                                      divmod                                       repr
ZeroDivisionError                            dreload                                      return
_                                            elif                                         reversed
_19                                          else                                         rm
_20                                          enumerate                                    rmdir
_23                                          eval                                         round
_24                                          except                                       set
_25                                          exec                                         setattr
_26                                          execfile                                     slice
_27                                          exit                                         sorted
_3                                           file                                         staticmethod
_8                                           filter                                       stereo_proj
__                                           finally                                      str
__IP                                         float                                        sum
__IPYTHON__                                  for                                          super
__IPYTHON__active                            format                                       sys
___                                          from                                         test_len
__debug__                                    frozenset                                    test_len2
__doc__                                      getattr                                      time_0_projection.png
__file__                                     global                                       timedelta
__import__                                   globals                                      try
__name__                                     hasattr                                      tuple
__nonzero__                                  hash                                         type
__package__                                  help                                         tzinfo
_dh                                          hex                                          unichr
_i                                           i                                            unicode
_i1                                          id                                           vars
_i11                                         if                                           while
_i12                                         import                                       with
_i13                                         in                                           xrange
_i14                                         input                                        xx
_i15                                         int                                          y
_i16                                         intern                                       y2
_i17                                         ip_set_hook                                  yield
_i18                                         ipalias                                      yy
_i19                                         ipmagic                                      zip
_i2                                          ipsystem                                     
   ....:                 width=40000000,#these are hardcoded for now
   ....:                 height=30000000) 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
      1 
----> 2 
      3 
      4 
      5 

NameError: name 'self' is not defined

In [29]:  



































































































                                        
   ....:  
   ....:  
   ....:  
   ....:  
   ....:  
   ....:  
   ....:  

KeyboardInterrupt

In [29]: bm =     self.basemap = Basemap(projection = 'stere', lon_0 = .5*( self.lon[0] - self.lon[-1]), lat_0 = .5*( self.lat[0] - self.lat[-1]), width=40000
000,
Display all 267 possibilities? (y or n)
ArithmeticError                              _i16                                         in
AssertionError                               _i17                                         input
AttributeError                               _i18                                         int
BaseException                                _i19                                         intern
Basemap                                      _i2                                          ip_set_hook
BufferError                                  _i20                                         ipalias
BytesWarning                                 _i21                                         ipmagic
DeprecationWarning                           _i22                                         ipsystem
EOFError                                     _i23                                         ipython_output_0603.py
Ellipsis                                     _i24                                         is
EnvironmentError                             _i25                                         isinstance
Exception                                    _i26                                         issubclass
False                                        _i27                                         iter
FloatingPointError                           _i28                                         jobs
FutureWarning                                _i29                                         lambda
GeneratorExit                                _i3                                          len
IOError                                      _i4                                          license
ImportError                                  _i5                                          list
ImportWarning                                _i6                                          locals
In                                           _i7                                          long
IndentationError                             _i8                                          map
IndexError                                   _i9                                          max
KeyError                                     _ih                                          memoryview
KeyboardInterrupt                            _ii                                          min
LookupError                                  _iii                                         nc
MemoryError                                  _ip                                          ncom_glb_sfcurrents_2011060600
NameError                                    _oh                                          ncom_glb_sfcurrents_2011060600.nc
NcomNetcdf                                   _sh                                          ncom_glb_sfcurrents_2011060600.zip
NcomTime                                     abs                                          ncom_glb_sfcurrents_2011060600_AK_stereo.nc
None                                         all                                          ncom_glb_sfcurrents_2011060900.nc
NotImplemented                               and                                          ncom_glb_sfcurrents_2011060900.nc.gz
NotImplementedError                          any                                          netcdf_global_ocean_export.py
OSError                                      apply                                        netcdf_global_ocean_export.pyc
Out                                          as                                           next
OverflowError                                assert                                       nfile
PendingDeprecationWarning                    basestring                                   not
R                                            bin                                          np
ReferenceError                               bool                                         object
RuntimeError                                 break                                        oct
RuntimeWarning                               buffer                                       open
StandardError                                bytearray                                    or
StopIteration                                bytes                                        ord
SyntaxError                                  callable                                     os
SyntaxWarning                                chr                                          pass
SystemError                                  class                                        plt
SystemExit                                   classmethod                                  pow
TabError                                     cmp                                          print
True                                         coerce                                       property
TypeError                                    compile                                      quit
UnboundLocalError                            complex                                      raise
UnicodeDecodeError                           continue                                     range
UnicodeEncodeError                           copyright                                    raw_input
UnicodeError                                 credits                                      reduce
UnicodeTranslateError                        datetime                                     region.png
UnicodeWarning                               def                                          reload
UserWarning                                  del                                          repr
ValueError                                   delattr                                      return
Warning                                      dict                                         reversed
ZeroDivisionError                            dir                                          round
_                                            dist                                         set
_19                                          divmod                                       setattr
_20                                          dreload                                      slice
_23                                          elif                                         sorted
_24                                          else                                         staticmethod
_25                                          enumerate                                    stereo_proj
_26                                          eval                                         str
_27                                          except                                       sum
_3                                           exec                                         super
_8                                           execfile                                     sys
__                                           exit                                         test_len
__IP                                         file                                         test_len2
__IPYTHON__                                  filter                                       time_0_projection.png
__IPYTHON__active                            finally                                      timedelta
___                                          float                                        try
__debug__                                    for                                          tuple
__doc__                                      format                                       type
__file__                                     from                                         tzinfo
__import__                                   frozenset                                    unichr
__name__                                     getattr                                      unicode
__nonzero__                                  global                                       vars
__package__                                  globals                                      while
_dh                                          hasattr                                      with
_i                                           hash                                         xrange
_i1                                          help                                         xx
_i11                                         hex                                          y
_i12                                         i                                            y2
_i13                                         id                                           yield
_i14                                         if                                           yy
_i15                                         import                                       zip

In [29]: bm = Basemap(projection = 'stere', lon_0 = .5*( self.lon[0] - self.lon[-1]), lat_0 = .5*( self.lat[0] - self.lat[-1]), width=40000000,height=30000000
)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

NameError: name 'self' is not defined

In [31]: bm = Basemap(projection = 'stere', lon_0 = .5*( nfile.lon[0] - nfile.lon[-1]), lat_0 = .5*( nfile.lat[0] - nfile.lat[-1]), width=40000000,height=3000
0000)
 
In [32]: bm.quiver(nfile.x,nfile.y,nfile.u[0],nfile.v[0]) 
Out[32]: <matplotlib.quiver.Quiver object at 0x1573382c>

In [33]: xxx,yyy = bm.(*np.meshgrid(nfile.lon,nfile.lat)) 
------------------------------------------------------------
   File "<ipython console>", line 1
     xxx,yyy = bm.(*np.meshgrid(nfile.lon,nfile.lat))
                  ^
SyntaxError: invalid syntax


In [34]: xxx,yyy = bm(*np.meshgrid(nfile.lon,nfile.lat))
 
In [35]: bm.quiver(xxx,yyy,nfile.u[0],nfile.v[0])
Out[35]: <matplotlib.quiver.Quiver object at 0x1571feac>

In [36]: plt.quiver(yy,xx,nfile.u[0],nfile.v[0]) 
Out[36]: <matplotlib.quiver.Quiver object at 0x181674ac>

In [37]: plt.clf() 
 
In [38]: plt.quiver(yy,xx,nfile.u[0],nfile.v[0]) 
Out[38]: <matplotlib.quiver.Quiver object at 0x1e61edac>

In [39]: plt.clf() 
 
In [40]: xxx,yyy = bm(*np.meshgrid(nfile.lon,nfile.lat)) 
 
In [41]: plt.quiver(xxx,yyy,nfile.u[0],nfile.v[0])
Out[41]: <matplotlib.quiver.Quiver object at 0x2180f08c>

In [42]: plt.quiver(yyy,xxx,nfile.u[0],nfile.v[0])
Out[42]: <matplotlib.quiver.Quiver object at 0x1b36484c>

In [43]: plt.clf() 
 
In [44]: plt.quiver(yyy,xxx,nfile.u[0],nfile.v[0]) 
Out[44]: <matplotlib.quiver.Quiver object at 0x27cb7f0c>

In [45]: plt.clf() 
 
In [46]: bm.quiver(yyy,xxx,nfile.u[0],nfile.v[0]) 
Out[46]: <matplotlib.quiver.Quiver object at 0x2af33d2c>

In [47]: from scipy.interpolate import griddata 

In [48]: pts = np.random.rand(1000,2) 

In [49]: pts.shape 
Out[49]: (1000, 2)

In [50]: np.mgrid? 
Type:             nd_grid
Base Class:       <class 'numpy.lib.index_tricks.nd_grid'>
String Form:   <numpy.lib.index_tricks.nd_grid object at 0xa30436c>
Namespace:        Interactive
Length:           0
File:             /usr/lib/pymodules/python2.7/numpy/lib/index_tricks.py
Docstring:
    `nd_grid` instance which returns a dense multi-dimensional "meshgrid".
    
    An instance of `numpy.lib.index_tricks.nd_grid` which returns an dense
    (or fleshed out) mesh-grid when indexed, so that each returned argument
    has the same shape.  The dimensions and number of the output arrays are
    equal to the number of indexing dimensions.  If the step length is not a
    complex number, then the stop is not inclusive.
    
    However, if the step length is a **complex number** (e.g. 5j), then
    the integer part of its magnitude is interpreted as specifying the
    number of points to create between the start and stop values, where
    the stop value **is inclusive**.
    
    Returns
    ----------
    mesh-grid `ndarrays` all of the same dimensions
    
    See Also
    --------
    numpy.lib.index_tricks.nd_grid : class of `ogrid` and `mgrid` objects
    ogrid : like mgrid but returns open (not fleshed out) mesh grids
    r_ : array concatenator
    
    Examples
    --------
    >>> np.mgrid[0:5,0:5]
    array([[[0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4]],
           [[0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4]]])
    >>> np.mgrid[-1:1:5j]
    array([-1. , -0.5,  0. ,  0.5,  1. ])
Class Docstring:
    Construct a multi-dimensional "meshgrid".
    
    ``grid = nd_grid()`` creates an instance which will return a mesh-grid
    when indexed.  The dimension and number of the output arrays are equal
    to the number of indexing dimensions.  If the step length is not a
    complex number, then the stop is not inclusive.
    
    However, if the step length is a **complex number** (e.g. 5j), then the
    integer part of its magnitude is interpreted as specifying the
    number of points to create between the start and stop values, where
    the stop value **is inclusive**.
    
    If instantiated with an argument of ``sparse=True``, the mesh-grid is
    open (or not fleshed out) so that only one-dimension of each returned
    argument is greater than 1.
    
    Parameters
    ----------
    sparse : bool, optional
        Whether the grid is sparse or not. Default is False.
    
    Notes
    -----
    Two instances of `nd_grid` are made available in the NumPy namespace,
    `mgrid` and `ogrid`::
    
        mgrid = nd_grid(sparse=False)
        ogrid = nd_grid(sparse=True)
    
    Users should use these pre-defined instances instead of using `nd_grid`
    directly.
    
    Examples
    --------
    >>> mgrid = np.lib.index_tricks.nd_grid()
    >>> mgrid[0:5,0:5]
    array([[[0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4]],
           [[0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4]]])
    >>> mgrid[-1:1:5j]
    array([-1. , -0.5,  0. ,  0.5,  1. ])
    
    >>> ogrid = np.lib.index_tricks.nd_grid(sparse=True)
    >>> ogrid[0:5,0:5]
    [array([[0],
            [1],
            [2],
            [3],
            [4]]), array([[0, 1, 2, 3, 4]])]

In [51]: (grid_x,grid_y) = np.mgrid[0:1:100j,0:1,200j] 
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/usr/lib/pymodules/python2.7/numpy/lib/index_tricks.pyc in __getitem__(self, key)
    207             typ = int
    208             for k in range(len(key)):
--> 209                 step = key[k].step
    210                 start = key[k].start
    211                 if start is None: start=0

AttributeError: 'complex' object has no attribute 'step'

In [52]: (grid_x,grid_y) = np.mgrid[0:1:100j,0:1:200j]

In [53]: grid_x.shape 
Out[53]: (100, 200)

In [54]: xxx.shape 
Out[54]: (200, 400)

In [55]: x[0:10][0:10] 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

NameError: name 'x' is not defined

In [56]: xxx[0:10][0:10] 
Out[56]: 
array([[ 1679377.57559313,  1678416.68167896,  1677722.52835002, ...,
         8534193.0308964 ,  8553784.83635189,  8573360.60657546],
       [ 1777906.36759818,  1776650.88082495,  1775661.57097624, ...,
         8556470.2971703 ,  8575981.56244777,  8595477.12203719],
       [ 1876111.19455992,  1874565.29949936,  1873284.99077764, ...,
         8578827.96271132,  8598258.56309037,  8617673.78671938],
       ..., 
       [ 2362245.78416179,  2359309.5967546 ,  2356635.65968677, ...,
         8691817.42492613,  8710842.91038768,  8729854.65408241],
       [ 2458489.31677611,  2455287.21522602,  2452346.62427333, ...,
         8714654.55651965,  8733598.67708055,  8752529.38080669],
       [ 2554403.40357764,  2550939.36703651,  2547736.07849772, ...,
         8737571.09963547,  8756433.74674255,  8775283.30121786]])

In [57]: np.meshgrid? 
Type:             function
Base Class:       <type 'function'>
String Form:   <function meshgrid at 0xa301a3c>
Namespace:        Interactive
File:             /usr/lib/pymodules/python2.7/numpy/lib/function_base.py
Definition:       np.meshgrid(x, y)
Docstring:
    Return coordinate matrices from two coordinate vectors.
    
    Parameters
    ----------
    x, y : ndarray
        Two 1-D arrays representing the x and y coordinates of a grid.
    
    Returns
    -------
    X, Y : ndarray
        For vectors `x`, `y` with lengths ``Nx=len(x)`` and ``Ny=len(y)``,
        return `X`, `Y` where `X` and `Y` are ``(Ny, Nx)`` shaped arrays
        with the elements of `x` and y repeated to fill the matrix along
        the first dimension for `x`, the second for `y`.
    
    See Also
    --------
    index_tricks.mgrid : Construct a multi-dimensional "meshgrid"
                         using indexing notation.
    index_tricks.ogrid : Construct an open multi-dimensional "meshgrid"
                         using indexing notation.
    
    Examples
    --------
    >>> X, Y = np.meshgrid([1,2,3], [4,5,6,7])
    >>> X
    array([[1, 2, 3],
           [1, 2, 3],
           [1, 2, 3],
           [1, 2, 3]])
    >>> Y
    array([[4, 4, 4],
           [5, 5, 5],
           [6, 6, 6],
           [7, 7, 7]])
    
    `meshgrid` is very useful to evaluate functions on a grid.
    
    >>> x = np.arange(-5, 5, 0.1)
    >>> y = np.arange(-5, 5, 0.1)
    >>> xx, yy = np.meshgrid(x, y)
    >>> z = np.sin(xx**2+yy**2)/(xx**2+yy**2)

In [58]: xxx[0][0],yyy[0][0] 
Out[58]: (1679377.5755931258, 40591826.833732188)

In [59]: points = np.zeros(200*400,2) 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

TypeError: data type not understood

In [60]: points = np.zeros((200*400,2))
 
In [61]: points.shape 
Out[61]: (80000, 2)

In [62]: for i in range(200): 
   ....:     for j in range(400): 
   ....:         points[400*i+j][0] = x[i][j] 
   ....:         points[400*i+j][1] = y[i][j] 
   ....:          
   ....:          
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
      1 
      2 
----> 3 
      4 
      5 

NameError: name 'x' is not defined

In [63]: for i in range(200):
    for j in range(400):
        points[400*i+j][0] = xxx[i][j] 
        points[400*i+j][1] = yyy[i][j]
   ....:          
   ....:          
 
In [67]: np.min( np.abs( xxx - yyy)) 
Out[67]: 15802869.757480223

In [68]: bm = Basemap(projection = 'stere', lon_0 = .5*( nfile.lon[0] - nfile.lon[-1]), lat_0 = .5*( nfile.lat[0] - nfile.lat[-1]), width=4e6,height=3e6) 
 
In [69]: plt.figure() 
Out[69]: <matplotlib.figure.Figure object at 0x1530f4ac>

In [70]: bm.drawcoastlines() 
Out[70]: <matplotlib.collections.LineCollection object at 0x1530ffac>

In [71]: bm = Basemap(projection = 'stere', lon_0 = .5*( nfile.lon[0] - nfile.lon[-1]), lat_0 = .5*( nfile.lat[0] - nfile.lat[-1]), width=4e6,height=3e6) 

KeyboardInterrupt

In [71]:  

In [72]:  

In [73]: m = Basemap(width=12000000,height=8000000, 
     ....:             resolution='l',projection='stere',\ 
   ....:             lat_ts=50,lat_0=50,lon_0=-107.) 
 
 
 
In [74]: 

In [75]: 

In [76]: plt.clf() 
 
In [77]: m.drawcoastlines() 
Out[77]: <matplotlib.collections.LineCollection object at 0x1530ff6c>

In [78]:                 lon_0 = .5*( self.lon[0] - self.lon[-1]),
   ....:  

KeyboardInterrupt

In [78]: .5*(nfile.lon[0] - self.lon[-1]) 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

NameError: name 'self' is not defined

In [80]: .5*(nfile.lon[0] - nfile.lon[-1])
Out[80]: -24.9375

In [81]: .5*(nfile.lat[0] - nfile.lat[-1])
Out[81]: -12.4375

In [82]: nfile.lat[0] 
Out[82]: 45.0

In [83]: nfile.lat[-1] 
Out[83]: 69.875

In [84]: bm = Basemap(projection = 'stere', lon_0 = .5*( nfile.lon[-1] - nfile.lon[0]), lat_0 = .5*( nfile.lat[-1] - nfile.lat[0]), width=4e6,height=3e6)
 
In [85]: plt.clf() 
 
In [86]: bm.drawcoastlines() 
Out[86]: <matplotlib.collections.LineCollection object at 0x2e51910c>

In [87]: bm = Basemap(projection = 'stere', lon_0 = .5*( nfile.lon[-1] + nfile.lon[0]), lat_0 = .5*( nfile.lat[-1] + nfile.lat[0]), width=4e6,height=3e6)
 
In [88]: bm.drawcoastlines() 
Out[88]: <matplotlib.collections.LineCollection object at 0x2e57c08c>

In [89]: plt.clf() 
 
In [90]: bm.drawcoastlines() 
Out[90]: <matplotlib.collections.LineCollection object at 0x2e57beac>

In [91]: x,y = bm(*np.meshgrid(nfile.lon,nfile.lat)) 
 
In [92]: bm.quiver(x,y,nfile.u[0],nfile.v[0]) 
Out[92]: <matplotlib.quiver.Quiver object at 0x2e7a68cc>

In [93]: bm.c 
bm.celestial          bm.coastpolygons      bm.coastpolygontypes  bm.coastsegs          bm.contour            bm.contourf           

In [93]: bm.c 
bm.celestial          bm.coastpolygons      bm.coastpolygontypes  bm.coastsegs          bm.contour            bm.contourf           

In [93]: plt.g 
plt.gca                      plt.get                      plt.get_current_fig_manager  plt.get_scale_docs           plt.ginput
plt.gcf                      plt.get_backend              plt.get_fignums              plt.get_scale_names          plt.gray
plt.gci                      plt.get_cmap                 plt.get_plot_commands        plt.getp                     plt.grid

In [93]: plt.ge 
plt.get                      plt.get_cmap                 plt.get_fignums              plt.get_scale_docs           plt.getp
plt.get_backend              plt.get_current_fig_manager  plt.get_plot_commands        plt.get_scale_names          

In [93]: plt.c 
plt.cla        plt.clf        plt.close      plt.cohere     plt.colormaps  plt.connect    plt.contourf   plt.copper     
plt.clabel     plt.clim       plt.cm         plt.colorbar   plt.colors     plt.contour    plt.cool       plt.csd        

In [93]: plt.cla() 
 
In [94]: xx,yy = stereo_proj(nfile.lon,nfile.lat) 
 
In [95]: bm.drawcoastlines() 
Out[95]: <matplotlib.collections.LineCollection object at 0x2e73e90c>

In [96]: bm.quiver(xx,yy,nfile.u[0],nfile.v[0]) 
Out[96]: <matplotlib.quiver.Quiver object at 0x2e7cfd6c>

In [97]: R = 6378.1e3

In [98]: bm.quiver(R*xx,r*yy,nfile.u[0],nfile.v[0])
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

NameError: name 'r' is not defined

In [99]: bm.quiver(R*xx,R*yy,nfile.u[0],nfile.v[0])
Out[99]: <matplotlib.quiver.Quiver object at 0x14e67aec>

In [100]: plt.clf() 

In [101]: xx = R*xx 
 
In [102]: yy = R*yy 

In [103]: xx[0][0] 
Out[103]: -15395968.347509542

In [104]: x[0][0] 
Out[104]: 42883.629143441096

In [105]: xx,yy = stereo_proj(nfile.lon,nfile.lat)
 
In [106]: xx 
Out[106]: 
array([[-2.41388005, -2.41379146, -2.41369246, ..., -1.60870295,
        -1.60495919, -1.60120852],
       [-2.42134735, -2.42125849, -2.42115917, ..., -1.61367944,
        -1.60992411, -1.60616183],
       [-2.4288542 , -2.42876507, -2.42866544, ..., -1.6186823 ,
        -1.61491532, -1.61114138],
       ..., 
       [-5.56396309, -5.5637589 , -5.56353069, ..., -3.70804001,
        -3.69941071, -3.69076544],
       [-5.59904097, -5.59883549, -5.59860584, ..., -3.73141727,
        -3.72273357, -3.7140338 ],
       [-5.63455003, -5.63434325, -5.63411215, ..., -3.75508188,
        -3.74634311, -3.73758816]])

In [107]: nfile.lon 
Out[107]: 
array([ 190.   ,  190.125,  190.25 ,  190.375,  190.5  ,  190.625,
        190.75 ,  190.875,  191.   ,  191.125,  191.25 ,  191.375,
        191.5  ,  191.625,  191.75 ,  191.875,  192.   ,  192.125,
        192.25 ,  192.375,  192.5  ,  192.625,  192.75 ,  192.875,
        193.   ,  193.125,  193.25 ,  193.375,  193.5  ,  193.625,
        193.75 ,  193.875,  194.   ,  194.125,  194.25 ,  194.375,
        194.5  ,  194.625,  194.75 ,  194.875,  195.   ,  195.125,
        195.25 ,  195.375,  195.5  ,  195.625,  195.75 ,  195.875,
        196.   ,  196.125,  196.25 ,  196.375,  196.5  ,  196.625,
        196.75 ,  196.875,  197.   ,  197.125,  197.25 ,  197.375,
        197.5  ,  197.625,  197.75 ,  197.875,  198.   ,  198.125,
        198.25 ,  198.375,  198.5  ,  198.625,  198.75 ,  198.875,
        199.   ,  199.125,  199.25 ,  199.375,  199.5  ,  199.625,
        199.75 ,  199.875,  200.   ,  200.125,  200.25 ,  200.375,
        200.5  ,  200.625,  200.75 ,  200.875,  201.   ,  201.125,
        201.25 ,  201.375,  201.5  ,  201.625,  201.75 ,  201.875,
        202.   ,  202.125,  202.25 ,  202.375,  202.5  ,  202.625,
        202.75 ,  202.875,  203.   ,  203.125,  203.25 ,  203.375,
        203.5  ,  203.625,  203.75 ,  203.875,  204.   ,  204.125,
        204.25 ,  204.375,  204.5  ,  204.625,  204.75 ,  204.875,
        205.   ,  205.125,  205.25 ,  205.375,  205.5  ,  205.625,
        205.75 ,  205.875,  206.   ,  206.125,  206.25 ,  206.375,
        206.5  ,  206.625,  206.75 ,  206.875,  207.   ,  207.125,
        207.25 ,  207.375,  207.5  ,  207.625,  207.75 ,  207.875,
        208.   ,  208.125,  208.25 ,  208.375,  208.5  ,  208.625,
        208.75 ,  208.875,  209.   ,  209.125,  209.25 ,  209.375,
        209.5  ,  209.625,  209.75 ,  209.875,  210.   ,  210.125,
        210.25 ,  210.375,  210.5  ,  210.625,  210.75 ,  210.875,
        211.   ,  211.125,  211.25 ,  211.375,  211.5  ,  211.625,
        211.75 ,  211.875,  212.   ,  212.125,  212.25 ,  212.375,
        212.5  ,  212.625,  212.75 ,  212.875,  213.   ,  213.125,
        213.25 ,  213.375,  213.5  ,  213.625,  213.75 ,  213.875,
        214.   ,  214.125,  214.25 ,  214.375,  214.5  ,  214.625,
        214.75 ,  214.875,  215.   ,  215.125,  215.25 ,  215.375,
        215.5  ,  215.625,  215.75 ,  215.875,  216.   ,  216.125,
        216.25 ,  216.375,  216.5  ,  216.625,  216.75 ,  216.875,
        217.   ,  217.125,  217.25 ,  217.375,  217.5  ,  217.625,
        217.75 ,  217.875,  218.   ,  218.125,  218.25 ,  218.375,
        218.5  ,  218.625,  218.75 ,  218.875,  219.   ,  219.125,
        219.25 ,  219.375,  219.5  ,  219.625,  219.75 ,  219.875,
        220.   ,  220.125,  220.25 ,  220.375,  220.5  ,  220.625,
        220.75 ,  220.875,  221.   ,  221.125,  221.25 ,  221.375,
        221.5  ,  221.625,  221.75 ,  221.875,  222.   ,  222.125,
        222.25 ,  222.375,  222.5  ,  222.625,  222.75 ,  222.875,
        223.   ,  223.125,  223.25 ,  223.375,  223.5  ,  223.625,
        223.75 ,  223.875,  224.   ,  224.125,  224.25 ,  224.375,
        224.5  ,  224.625,  224.75 ,  224.875,  225.   ,  225.125,
        225.25 ,  225.375,  225.5  ,  225.625,  225.75 ,  225.875,
        226.   ,  226.125,  226.25 ,  226.375,  226.5  ,  226.625,
        226.75 ,  226.875,  227.   ,  227.125,  227.25 ,  227.375,
        227.5  ,  227.625,  227.75 ,  227.875,  228.   ,  228.125,
        228.25 ,  228.375,  228.5  ,  228.625,  228.75 ,  228.875,
        229.   ,  229.125,  229.25 ,  229.375,  229.5  ,  229.625,
        229.75 ,  229.875,  230.   ,  230.125,  230.25 ,  230.375,
        230.5  ,  230.625,  230.75 ,  230.875,  231.   ,  231.125,
        231.25 ,  231.375,  231.5  ,  231.625,  231.75 ,  231.875,
        232.   ,  232.125,  232.25 ,  232.375,  232.5  ,  232.625,
        232.75 ,  232.875,  233.   ,  233.125,  233.25 ,  233.375,
        233.5  ,  233.625,  233.75 ,  233.875,  234.   ,  234.125,
        234.25 ,  234.375,  234.5  ,  234.625,  234.75 ,  234.875,
        235.   ,  235.125,  235.25 ,  235.375,  235.5  ,  235.625,
        235.75 ,  235.875,  236.   ,  236.125,  236.25 ,  236.375,
        236.5  ,  236.625,  236.75 ,  236.875,  237.   ,  237.125,
        237.25 ,  237.375,  237.5  ,  237.625,  237.75 ,  237.875,
        238.   ,  238.125,  238.25 ,  238.375,  238.5  ,  238.625,
        238.75 ,  238.875,  239.   ,  239.125,  239.25 ,  239.375,
        239.5  ,  239.625,  239.75 ,  239.875])

In [108]: nfile.lat[0:10] 
Out[108]: 
array([ 45.   ,  45.125,  45.25 ,  45.375,  45.5  ,  45.625,  45.75 ,
        45.875,  46.   ,  46.125])

In [109]: 90 - nfile.lat[0:10] 
Out[109]: 
array([ 45.   ,  44.875,  44.75 ,  44.625,  44.5  ,  44.375,  44.25 ,
        44.125,  44.   ,  43.875])

In [110]: xx,yy = stereo_proj(-nfile.lon,-nfile.lat)
 
In [111]: xx = R*xx 

In [112]: yy = R*yy 

In [113]: xx[0][0] 
Out[113]: -2641530.5566988606

In [114]: yy[0][0] 
Out[114]: 43912.049574271106

In [115]: bm.drawcoastlines() 
Out[115]: <matplotlib.collections.LineCollection object at 0x319dfbec>

In [116]: plt.clf() 
 
In [117]: plt.quiver(xx,yy,nfile.u[0],nfile.v[0]) 
Out[117]: <matplotlib.quiver.Quiver object at 0x38320f0c>

In [118]: plt.cla() 

In [119]: plt.quiver(-xx,-yy,nfile.u[0],nfile.v[0])
Out[119]: <matplotlib.quiver.Quiver object at 0x3b53752c>

In [120]: plt.cla() 

In [121]: plt.quiver(-xx,yy,nfile.u[0],nfile.v[0])
Out[121]: <matplotlib.quiver.Quiver object at 0x3b5379cc>

In [122]: plt.cla() 

In [123]: plt.quiver(xx,-yy,nfile.u[0],nfile.v[0])
Out[123]: <matplotlib.quiver.Quiver object at 0x37df102c>

In [124]: xx = xx*cos(-3*pi/2) 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

NameError: name 'cos' is not defined

In [125]: xx = xx*np.cos(-3*np.pi/2)
 
In [126]: yy = yy*np.cos(-3*np.pi/2)

In [127]: plt.cla() 
 
In [128]: plt.quiver(xx,yy,nfile.u[0],nfile.v[0])
Out[128]: <matplotlib.quiver.Quiver object at 0xae86dec>

In [129]: xx,yy = stereo_proj(-nfile.lon,-nfile.lat)
 
In [130]: xx = R*np.cos(-3*np.pi/4)

In [131]: xx,yy = stereo_proj(-nfile.lon,-nfile.lat) 

In [132]: xx = R*xx*np.cos(-3*np.pi/4) 
 
In [133]: yy = R*yy*np.cos(-3*np.pi/4)

In [134]: plt.quiver(xx,yy,nfile.u[0],nfile.v[0])
Out[134]: <matplotlib.quiver.Quiver object at 0x47820eec>

In [135]: plt.cla() 

In [136]: plt.quiver(xx,yy,nfile.u[0],nfile.v[0]) 
Out[136]: <matplotlib.quiver.Quiver object at 0x4462ec6c>

In [137]: xx,yy = stereo_proj(-nfile.lon,-nfile.lat)
 
In [138]: xx = R*xx*np.cos(-3*np.pi/4)

In [139]: yy = R*yy*np.sin(-3*np.pi/4)

In [140]: plt.cl 
plt.cla     plt.clabel  plt.clf     plt.clim    plt.close   

In [140]: plt.cla()

In [141]: plt.quiver(xx,yy,nfile.u[0],nfile.v[0])
Out[141]: <matplotlib.quiver.Quiver object at 0x3b53c08c>

In [142]: xx,yy = stereo_proj(-nfile.lon,-nfile.lat) 

In [143]: plt.cla() 
 
In [144]: plt.quiver(xx,yy,nfile.u[0],nfile.v[0]) 
Out[144]: <matplotlib.quiver.Quiver object at 0x38320eac>

In [145]: from numpy import cos,sin,tan,pi 

KeyboardInterrupt

In [145]: from numpy import cos,sin,tan,pi 
 
In [146]: plt.quiver(xx*cos(pi/4),yy*sin(pi/4),nfile.u[0],nfile.v[0])
Out[146]: <matplotlib.quiver.Quiver object at 0x2e514d6c>

In [147]: plt.cla() 
 
In [148]: def rotate(x,y): 
   .....:  

KeyboardInterrupt

In [148]: def rotate(x,y,th): 
   .....:     return (x*cos(th) - y*sin(th), x*sin(th) + y*cos(th)) 
   .....:  

In [150]: plt.quiver(*rotate(xx,yy,-3*pi/4),nfile.u[0],nfile.v[0]) 
------------------------------------------------------------
   File "<ipython console>", line 1
SyntaxError: only named arguments may follow *expression (<ipython console>, line 1)


In [151]: xxx,yyy = rotate(xx,yy,-3*pi/4) 
 
In [152]: plt.quiver(xxx,yyy,nfile.u[0],nfile.v[0])
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

NameError: name 'coy' is not defined

In [153]: plt.quiver(xxx,yyy,nfile.u[0],nfile.v[0])
Out[153]: <matplotlib.quiver.Quiver object at 0x3830e40c>

In [154]: plt.quiver(rotate(xx,yy,-3*pi/4),nfile.u[0],nfile.v[0])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
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

In [155]: plt.quiver(*rotate(xx,yy,-3*pi/4),nfile.u[0],nfile.v[0])
------------------------------------------------------------
   File "<ipython console>", line 1
SyntaxError: only named arguments may follow *expression (<ipython console>, line 1)


In [156]: *(1,2)
------------------------------------------------------------
   File "<ipython console>", line 1
     *(1,2)
     ^
SyntaxError: invalid syntax


In [157]: rotate(*(xx,yy,pi)) 
Out[157]: 
(array([[ 0.41415634,  0.41414114,  0.41412415, ...,  0.27600979,
         0.27536746,  0.27472395],
       [ 0.41287911,  0.41286395,  0.41284702, ...,  0.27515859,
         0.27451825,  0.27387672],
       [ 0.41160302,  0.41158792,  0.41157103, ...,  0.27430816,
         0.27366979,  0.27303025],
       ..., 
       [ 0.17967835,  0.17967176,  0.17966439, ...,  0.1197446 ,
         0.11946593,  0.11918675],
       [ 0.17855267,  0.17854612,  0.1785388 , ...,  0.1189944 ,
         0.11871748,  0.11844004],
       [ 0.17742743,  0.17742092,  0.17741364, ...,  0.1182445 ,
         0.11796932,  0.11769363]]),
 array([[-0.00688482, -0.00774532, -0.0086058 , ..., -0.3088551 ,
        -0.30942792, -0.3099994 ],
       [-0.00686358, -0.00772144, -0.00857926, ..., -0.30790261,
        -0.30847366, -0.30904338],
       [-0.00684237, -0.00769757, -0.00855274, ..., -0.30695097,
        -0.30752026, -0.30808822],
       ..., 
       [-0.00298692, -0.00336025, -0.00373356, ..., -0.13399427,
        -0.13424278, -0.13449071],
       [-0.00296821, -0.00333919, -0.00371016, ..., -0.1331548 ,
        -0.13340175, -0.13364813],
       [-0.0029495 , -0.00331815, -0.00368678, ..., -0.13231565,
        -0.13256105, -0.13280588]]))

In [158]: plt.quiver(*rotate(xx,yy,-3*pi/4)+(nfile.u[0],nfile.v[0]))
Out[158]: <matplotlib.quiver.Quiver object at 0x4dc16f8c>

In [159]: plt.cla() 
 
In [160]: plt.quiver(*rotate(xx,yy,-pi/4)+(nfile.u[0],nfile.v[0]))
Out[160]: <matplotlib.quiver.Quiver object at 0x5721ac2c>

In [161]: plt.quiver(*rotate(xx,yy,-pi/2)+(nfile.u[0],nfile.v[0]))
Out[161]: <matplotlib.quiver.Quiver object at 0x38252b2c>

In [162]: plt.quiver() 
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
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
    336     if len(args) == 3 or len(args) == 5:
    337         C = np.atleast_1d(args.pop(-1))
--> 338     V = np.atleast_1d(args.pop(-1))
    339     U = np.atleast_1d(args.pop(-1))
    340     if U.ndim == 1:

IndexError: pop from empty list

In [163]: plt.cla() 

In [164]: plt.quiver(*rotate(xx,yy,3*pi/2)+(nfile.u[0],nfile.v[0]))
Out[164]: <matplotlib.quiver.Quiver object at 0x3b53c60c>

In [165]: plt.cla()

In [166]: plt.quiver(*rotate(xx,yy,pi/2)+(nfile.u[0],nfile.v[0]))
Out[166]: <matplotlib.quiver.Quiver object at 0x540169ac>

In [167]: plt.quiver(*rotate(xx,yy,3*pi/4)+(nfile.u[0],nfile.v[0]))
Out[167]: <matplotlib.quiver.Quiver object at 0x3830e0ac>

In [168]: plt.cla() 
 
In [169]: plt.quiver(*rotate(xx,yy,3*pi/4)+(nfile.u[0],nfile.v[0])) 
Out[169]: <matplotlib.quiver.Quiver object at 0x50e1b34c>

In [170]: plt.figure() 
Out[170]: <matplotlib.figure.Figure object at 0xe5c6fcc>

In [171]: bm.drawcoastlines() 
Out[171]: <matplotlib.collections.LineCollection object at 0x4dc16b2c>

In [172]: xx.shape[0]/2 
Out[172]: 100

In [173]: deltax = np.abs(xx[xx.shape[0]/2+1] - xx[xx.shape[0]/2]) 
 
In [174]: deltax 
Out[174]: 
array([ 0.00118297,  0.00118292,  0.00118287,  0.00118282,  0.00118276,
        0.0011827 ,  0.00118263,  0.00118255,  0.00118247,  0.00118239,
        0.0011823 ,  0.00118221,  0.00118211,  0.001182  ,  0.00118189,
        0.00118178,  0.00118166,  0.00118153,  0.0011814 ,  0.00118127,
        0.00118113,  0.00118098,  0.00118083,  0.00118068,  0.00118051,
        0.00118035,  0.00118018,  0.00118   ,  0.00117982,  0.00117963,
        0.00117944,  0.00117925,  0.00117904,  0.00117884,  0.00117863,
        0.00117841,  0.00117819,  0.00117796,  0.00117773,  0.00117749,
        0.00117725,  0.001177  ,  0.00117675,  0.00117649,  0.00117623,
        0.00117596,  0.00117569,  0.00117541,  0.00117513,  0.00117484,
        0.00117455,  0.00117425,  0.00117395,  0.00117364,  0.00117333,
        0.00117301,  0.00117268,  0.00117235,  0.00117202,  0.00117168,
        0.00117134,  0.00117099,  0.00117064,  0.00117028,  0.00116991,
        0.00116955,  0.00116917,  0.00116879,  0.00116841,  0.00116802,
        0.00116762,  0.00116723,  0.00116682,  0.00116641,  0.001166  ,
        0.00116558,  0.00116515,  0.00116472,  0.00116429,  0.00116385,
        0.00116341,  0.00116296,  0.0011625 ,  0.00116204,  0.00116158,
        0.00116111,  0.00116063,  0.00116015,  0.00115967,  0.00115918,
        0.00115869,  0.00115819,  0.00115768,  0.00115717,  0.00115666,
        0.00115614,  0.00115561,  0.00115508,  0.00115455,  0.00115401,
        0.00115347,  0.00115292,  0.00115236,  0.0011518 ,  0.00115124,
        0.00115067,  0.00115009,  0.00114951,  0.00114893,  0.00114834,
        0.00114775,  0.00114715,  0.00114654,  0.00114593,  0.00114532,
        0.0011447 ,  0.00114408,  0.00114345,  0.00114281,  0.00114218,
        0.00114153,  0.00114088,  0.00114023,  0.00113957,  0.00113891,
        0.00113824,  0.00113757,  0.00113689,  0.00113621,  0.00113552,
        0.00113483,  0.00113413,  0.00113342,  0.00113272,  0.001132  ,
        0.00113129,  0.00113057,  0.00112984,  0.00112911,  0.00112837,
        0.00112763,  0.00112688,  0.00112613,  0.00112537,  0.00112461,
        0.00112385,  0.00112308,  0.0011223 ,  0.00112152,  0.00112073,
        0.00111994,  0.00111915,  0.00111835,  0.00111754,  0.00111674,
        0.00111592,  0.0011151 ,  0.00111428,  0.00111345,  0.00111262,
        0.00111178,  0.00111093,  0.00111009,  0.00110923,  0.00110838,
        0.00110751,  0.00110665,  0.00110577,  0.0011049 ,  0.00110402,
        0.00110313,  0.00110224,  0.00110134,  0.00110044,  0.00109954,
        0.00109863,  0.00109771,  0.00109679,  0.00109587,  0.00109494,
        0.00109401,  0.00109307,  0.00109213,  0.00109118,  0.00109022,
        0.00108927,  0.00108831,  0.00108734,  0.00108637,  0.00108539,
        0.00108441,  0.00108343,  0.00108244,  0.00108144,  0.00108044,
        0.00107944,  0.00107843,  0.00107742,  0.0010764 ,  0.00107537,
        0.00107435,  0.00107332,  0.00107228,  0.00107124,  0.00107019,
        0.00106914,  0.00106809,  0.00106703,  0.00106596,  0.00106489,
        0.00106382,  0.00106274,  0.00106166,  0.00106057,  0.00105948,
        0.00105838,  0.00105728,  0.00105618,  0.00105507,  0.00105395,
        0.00105283,  0.00105171,  0.00105058,  0.00104945,  0.00104831,
        0.00104717,  0.00104602,  0.00104487,  0.00104372,  0.00104256,
        0.00104139,  0.00104022,  0.00103905,  0.00103787,  0.00103669,
        0.0010355 ,  0.00103431,  0.00103311,  0.00103191,  0.00103071,
        0.0010295 ,  0.00102829,  0.00102707,  0.00102585,  0.00102462,
        0.00102339,  0.00102215,  0.00102091,  0.00101967,  0.00101842,
        0.00101717,  0.00101591,  0.00101465,  0.00101338,  0.00101211,
        0.00101083,  0.00100955,  0.00100827,  0.00100698,  0.00100569,
        0.00100439,  0.00100309,  0.00100178,  0.00100047,  0.00099916,
        0.00099784,  0.00099652,  0.00099519,  0.00099386,  0.00099252,
        0.00099118,  0.00098984,  0.00098849,  0.00098714,  0.00098578,
        0.00098442,  0.00098305,  0.00098168,  0.00098031,  0.00097893,
        0.00097755,  0.00097616,  0.00097477,  0.00097337,  0.00097197,
        0.00097057,  0.00096916,  0.00096775,  0.00096633,  0.00096491,
        0.00096349,  0.00096206,  0.00096063,  0.00095919,  0.00095775,
        0.0009563 ,  0.00095485,  0.0009534 ,  0.00095194,  0.00095048,
        0.00094901,  0.00094754,  0.00094607,  0.00094459,  0.00094311,
        0.00094162,  0.00094013,  0.00093864,  0.00093714,  0.00093564,
        0.00093413,  0.00093262,  0.00093111,  0.00092959,  0.00092806,
        0.00092654,  0.00092501,  0.00092347,  0.00092193,  0.00092039,
        0.00091884,  0.00091729,  0.00091574,  0.00091418,  0.00091262,
        0.00091105,  0.00090948,  0.00090791,  0.00090633,  0.00090475,
        0.00090316,  0.00090157,  0.00089998,  0.00089838,  0.00089678,
        0.00089517,  0.00089356,  0.00089195,  0.00089033,  0.00088871,
        0.00088709,  0.00088546,  0.00088383,  0.00088219,  0.00088055,
        0.00087891,  0.00087726,  0.00087561,  0.00087395,  0.00087229,
        0.00087063,  0.00086896,  0.00086729,  0.00086562,  0.00086394,
        0.00086226,  0.00086058,  0.00085889,  0.0008572 ,  0.0008555 ,
        0.0008538 ,  0.0008521 ,  0.00085039,  0.00084868,  0.00084696,
        0.00084524,  0.00084352,  0.0008418 ,  0.00084007,  0.00083833,
        0.0008366 ,  0.00083486,  0.00083311,  0.00083137,  0.00082962,
        0.00082786,  0.0008261 ,  0.00082434,  0.00082258,  0.00082081,
        0.00081904,  0.00081726,  0.00081548,  0.0008137 ,  0.00081191,
        0.00081012,  0.00080833,  0.00080653,  0.00080473,  0.00080293,
        0.00080112,  0.00079931,  0.0007975 ,  0.00079568,  0.00079386,
        0.00079203,  0.0007902 ,  0.00078837,  0.00078654,  0.0007847 ])

In [175]: deltax = np.abs(xx[-1][xx.shape[0]/2+1] - xx[-1][xx.shape[0]/2])
 
In [176]: deltax = np.abs(xx[-1][xx.shape[0]/2+1] - xx[-1][xx.shape[0]/2])

In [177]: deltax 
Out[177]: 8.2417925591382613e-05

In [178]: deltay = np.abs(yy[-1][0] - yy[-2][0]) 

In [179]: deltay 
Out[179]: 1.8705718005955843e-05

In [180]: np.linspace? 
Type:             function
Base Class:       <type 'function'>
Base Class:       <type 'function'>
String Form:   <function linspace at 0xa2d3f44>
Namespace:        Interactive
File:             /usr/lib/pymodules/python2.7/numpy/core/function_base.py
Definition:       np.linspace(start, stop, num=50, endpoint=True, retstep=False)
Docstring:
    Return evenly spaced numbers over a specified interval.
    
    Returns `num` evenly spaced samples, calculated over the
    interval [`start`, `stop` ].
    
    The endpoint of the interval can optionally be excluded.
    
    Parameters
    ----------
    start : scalar
        The starting value of the sequence.
    stop : scalar
        The end value of the sequence, unless `endpoint` is set to False.

In [181]: np.mgrid? 
Type:             nd_grid
Base Class:       <class 'numpy.lib.index_tricks.nd_grid'>
String Form:   <numpy.lib.index_tricks.nd_grid object at 0xa30436c>
Namespace:        Interactive
Length:           0
File:             /usr/lib/pymodules/python2.7/numpy/lib/index_tricks.py
Docstring:
    `nd_grid` instance which returns a dense multi-dimensional "meshgrid".
    
    An instance of `numpy.lib.index_tricks.nd_grid` which returns an dense
    (or fleshed out) mesh-grid when indexed, so that each returned argument
    has the same shape.  The dimensions and number of the output arrays are
    equal to the number of indexing dimensions.  If the step length is not a
    complex number, then the stop is not inclusive.
    
    However, if the step length is a **complex number** (e.g. 5j), then
    the integer part of its magnitude is interpreted as specifying the
    number of points to create between the start and stop values, where
    the stop value **is inclusive**.
    
    Returns
    ----------
    mesh-grid `ndarrays` all of the same dimensions
    
    See Also
    --------
    numpy.lib.index_tricks.nd_grid : class of `ogrid` and `mgrid` objects
    ogrid : like mgrid but returns open (not fleshed out) mesh grids
    r_ : array concatenator
    
    Examples
    --------
    >>> np.mgrid[0:5,0:5]
    array([[[0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4]],
           [[0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4]]])
    >>> np.mgrid[-1:1:5j]
    array([-1. , -0.5,  0. ,  0.5,  1. ])
Class Docstring:
    Construct a multi-dimensional "meshgrid".
    
    ``grid = nd_grid()`` creates an instance which will return a mesh-grid
    when indexed.  The dimension and number of the output arrays are equal
    to the number of indexing dimensions.  If the step length is not a
    complex number, then the stop is not inclusive.


print HEY
In [182]: XIO:  fatal IO error 11 (Resource temporarily unavailabl after 40288 requests (40288 known processed) with 0 events remaining 
