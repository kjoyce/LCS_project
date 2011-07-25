Python 2.7.1+ (r271:86832, Apr 11 2011, 18:05:24) 
Type "copyright", "credits" or "license" for more information.                                                                                                
                                                                                                                                                              
IPython 0.10.1 -- An enhanced Interactive Python.                                                                                                             
?         -> Introduction and overview of IPython's features.                                                                                                 
%quickref -> Quick reference.                                                                                                                                 
help      -> Python's own help system.                                                                                                                        
object?   -> Details about 'object'. ?object also works, ?? prints more.                                                                                      
                                                                                                                                                              
In [1]: run netcdf_global_ocean_export.py 
 
In [2]: nfile = net 
netcdf_global_ocean_export.py   netcdf_global_ocean_export.pyc                                                                                                
                                                                                                                                                              
In [2]: nfile = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc')
 
In [3]: nfile.set_grid_region() 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
                                                                                                                                                              
/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()                                                              
----> 1                                                                                                                                                       
      2                                                                                                                                                       
      3 
      4 
      5 

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in set_grid_region(self, lat_min, lat_max, lon_min, lon_max)
     46     self.v = np.array(v)
     47 
---> 48     __set_cyl_basemap()
     49     __set_stere_basemap()
     50 

NameError: global name '_NcomNetcdf__set_cyl_basemap' is not defined

In [4]: run netcdf_global_ocean_export.py

In [5]: nfile = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc')

In [6]: nfile.set_grid_region()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in set_grid_region(self, lat_min, lat_max, lon_min, lon_max)
     46     self.v = np.array(v)
     47 
---> 48     __set_cyl_basemap()
     49     __set_stere_basemap()
     50 

NameError: global name '_NcomNetcdf__set_cyl_basemap' is not defined

In [7]: run netcdf_global_ocean_export.py

In [8]: nfile = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc')
 
In [9]: nfile.set_grid_region()
Out[9]: <__main__.NcomNetcdf instance at 0x9faa1cc>
 
In [10]: nfile.lat.shape 
Out[10]: (200,)

In [11]: def st: 
------------------------------------------------------------
   File "<ipython console>", line 1
     def st:
           ^
SyntaxError: invalid syntax


In [12]: def st(x,y): 
   ....:     x,y = meshgrid(x,y) 
   ....:     from numpy import pi,sin,cos,tan 
   ....:     return cos(x)/tan(y/2),sin(x)/tan(y/2) 
   ....:  

In [13]: import numpy as np 
 
In [14]: np.max(nfile.lat),np.min(nfile.lon) 
Out[14]: (69.875, 190.0)

In [15]: np.max(nfile.lat),np.min(nfile.lat)
Out[15]: (69.875, 45.0)

In [16]: from numpy import pi,sin,cos,tan 
 
In [17]: lat = pi/180*( 90 - lat ) 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

NameError: name 'lat' is not defined

In [18]: lat = pi/180*( 90 - nfile.lat )

In [19]: lon = nfile.lon 

In [20]: st(lon[0],lat[0]) - st(lon[0],lat[-1]) 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in st(x, y)
      1 
----> 2 
      3 
      4 
      5 

NameError: global name 'meshgrid' is not defined

In [21]: ru 
%run     %runlog  

In [21]: run netcdf_global_ocean_export.py 

In [22]: set 
set      setattr  

In [22]: x,y = stereo_proj(nfile.lon,nfile.lat) 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in stereo_proj(lon, lat)
    157   lat = pi/180*(90 - lat)
    158   lon = pi/189*lon
--> 159   x = cos( lon ) / tan( lat/2 )
    160   y = sin( lon ) / tan( lat/2 )
    161   return x,y

ValueError: shape mismatch: objects cannot be broadcast to a single shape

In [23]: run netcdf_global_ocean_export.py

In [24]: x,y = stereo_proj(nfile.lon,nfile.lat) 

In [25]: x.shape 
Out[25]: (200, 400)

In [26]: y.shape 
Out[26]: (200, 400)

In [27]: x[0][0] 
Out[27]: -2.4138800500947841

In [28]: y[0][0] - y[0][-1] 
Out[28]: 1.7666812512746213

In [29]: y[1][0] - y[1][-1] 
Out[29]: 1.7721464501939592

In [30]: np.di 
np.diag               np.diag_indices_from  np.diagonal           np.digitize           np.divide             
np.diag_indices       np.diagflat           np.diff               np.disp               

In [30]: def dist(x1,x2): 
   ....:     return np.sqrt(  
KeyboardInterrupt

In [30]: def dist(x1,x2): 
   ....:     return np.sqrt( ( x1[0] - x2[0] )**2 + (x1[1] - x2[1])**2 ) 
   ....:  

In [32]: dist( (x[0][0],y[0][0]) , (x[0][-1],y[0][-1]) ) 
Out[32]: 1.9446330417156679

In [33]: dist( (x[1][0],y[1][0]) , (x[1][-1],y[1][-1]) )
Out[33]: 1.9506487315241297

In [34]: dist( (x[100][0],y[100][0]) , (x[100][-1],y[100][-1]) )
Out[34]: 2.7635225910524901

In [35]: dist( (x[0][0],y[0][0]) , (x[-1][0],y[-1][0]) )
Out[35]: 3.221114966285358

In [36]: dist( (x[0][3],y[0][3]) , (x[-1][3],y[-1][3]) )
Out[36]: 3.2211149662853575

In [37]: np.abs(x) 
Out[37]: 
array([[ 2.41388005,  2.41379146,  2.41369246, ...,  1.60870295,
         1.60495919,  1.60120852],
       [ 2.42134735,  2.42125849,  2.42115917, ...,  1.61367944,
         1.60992411,  1.60616183],
       [ 2.4288542 ,  2.42876507,  2.42866544, ...,  1.6186823 ,
         1.61491532,  1.61114138],
       ..., 
       [ 5.56396309,  5.5637589 ,  5.56353069, ...,  3.70804001,
         3.69941071,  3.69076544],
       [ 5.59904097,  5.59883549,  5.59860584, ...,  3.73141727,
         3.72273357,  3.7140338 ],
       [ 5.63455003,  5.63434325,  5.63411215, ...,  3.75508188,
         3.74634311,  3.73758816]])

In [38]: x,y = stereo_proj(nfile.lon,-nfile.lat)
 
In [39]: dist( (x[0][3],y[0][3]) , (x[-1][3],y[-1][3]) )
Out[39]: 0.2367616188147911

In [40]: dist( (x[0][0],y[0][0]) , (x[-1][0],y[-1][0]) )
Out[40]: 0.23676161881479105

In [41]: run netcdf_global_ocean_export.py

In [42]: nfile = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc')
 
In [43]: nfile.set_grid_region()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in set_grid_region(self, lat_min, lat_max, lon_min, lon_max)
     46     self.v = np.array(v)
     47 
---> 48     __set_cyl_basemap()
     49     __set_stere_basemap()
     50 

NameError: global name '_NcomNetcdf__set_cyl_basemap' is not defined

In [44]: run netcdf_global_ocean_export.py

In [45]: nfile = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc') 

In [46]: nfile.set_grid_region() 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in set_grid_region(self, lat_min, lat_max, lon_min, lon_max)
     47 
     48     self.__set_cyl_basemap()
---> 49     self.__set_stere_basemap()
     50 
     51     return self

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in __set_stere_basemap(self)
     64                  height=3000000)
     65 
---> 66     self.x,self.y = bm(*np.meshgrid(self.lon,self.lat))
     67 
     68   def get_time_readable(self):

NameError: global name 'bm' is not defined

In [47]: run netcdf_global_ocean_export.py 
 
In [48]: nfile = NcomNetcdf('ncom_glb_sfcurrents_2011060900.nc') 
 
In [49]: nfile.set_grid_region() 
Out[49]: <__main__.NcomNetcdf instance at 0xaa0fa4c>
 
In [50]: nfile.x.shape 
Out[50]: (200, 400)

In [51]: dist( (nfile.x[0][0],nfile.y[0][0]) , (nfile.x[-1][0],nfile.y[-1][0]) )
Out[51]: 14309987.134813789

In [52]: R = 6 378.1e6
------------------------------------------------------------
   File "<ipython console>", line 1
     R = 6 378.1e6
                 ^
SyntaxError: invalid syntax


In [53]: R = 6378.1e6

In [54]: R = 6378.1e3 
 
In [55]: dist( (x[0][0],y[0][0]) , (x[-1][0],y[-1][0]) )
Out[55]: 0.23676161881479105

In [56]: dist( (x[0][0],y[0][0]) , (x[-1][0],y[-1][0]) )*R 
Out[56]: 1510089.2809626188

In [57]: dist( (nfile.x[0][0],nfile.y[0][0]) , (nfile.x[-1][0],nfile.y[-1][0]) )
Out[57]: 14309987.134813789

In [58]: dist( (nfile.x[0][10],nfile.y[0][10]) , (nfile.x[-1][10],nfile.y[-1][10]) )
Out[58]: 14035312.361033853

In [59]: def test_len(n): 
   ....:     return dist( (nfile.x[0][n],nfile.y[0][n]) , (nfile.x[-1][n],nfile.y[-1][n]) )
   ....:  

In [60]: import matplotlib.pyplot as plt 

In [61]: nfile.x.shape[1] 
Out[61]: 400

In [62]: range(400) 
Out[62]: 
[0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22,
 23,
 24,
 25,
 26,
 27,
 28,
 29,
 30,
 31,
 32,
 33,
 34,
 35,
 36,
 37,
 38,
 39,
 40,
 41,
 42,
 43,
 44,
 45,
 46,
 47,
 48,
 49,
 50,
 51,
 52,
 53,
 54,
 55,
 56,
 57,
 58,
 59,
 60,
 61,
 62,
 63,
 64,
 65,
 66,
 67,
 68,
 69,
 70,
 71,
 72,
 73,
 74,
 75,
 76,
 77,
 78,
 79,
 80,
 81,
 82,
 83,
 84,
 85,
 86,
 87,
 88,
 89,
 90,
 91,
 92,
 93,
 94,
 95,
 96,
 97,
 98,
 99,
 100,
 101,
 102,
 103,
 104,
 105,
 106,
 107,
 108,
 109,
 110,
 111,
 112,
 113,
 114,
 115,
 116,
 117,
 118,
 119,
 120,
 121,
 122,
 123,
 124,
 125,
 126,
 127,
 128,
 129,
 130,
 131,
 132,
 133,
 134,
 135,
 136,
 137,
 138,
 139,
 140,
 141,
 142,
 143,
 144,
 145,
 146,
 147,
 148,
 149,
 150,
 151,
 152,
 153,
 154,
 155,
 156,
 157,
 158,
 159,
 160,
 161,
 162,
 163,
 164,
 165,
 166,
 167,
 168,
 169,
 170,
 171,
 172,
 173,
 174,
 175,
 176,
 177,
 178,
 179,
 180,
 181,
 182,
 183,
 184,
 185,
 186,
 187,
 188,
 189,
 190,
 191,
 192,
 193,
 194,
 195,
 196,
 197,
 198,
 199,
 200,
 201,
 202,
 203,
 204,
 205,
 206,
 207,
 208,
 209,
 210,
 211,
 212,
 213,
 214,
 215,
 216,
 217,
 218,
 219,
 220,
 221,
 222,
 223,
 224,
 225,
 226,
 227,
 228,
 229,
 230,
 231,
 232,
 233,
 234,
 235,
 236,
 237,
 238,
 239,
 240,
 241,
 242,
 243,
 244,
 245,
 246,
 247,
 248,
 249,
 250,
 251,
 252,
 253,
 254,
 255,
 256,
 257,
 258,
 259,
 260,
 261,
 262,
 263,
 264,
 265,
 266,
 267,
 268,
 269,
 270,
 271,
 272,
 273,
 274,
 275,
 276,
 277,
 278,
 279,
 280,
 281,
 282,
 283,
 284,
 285,
 286,
 287,
 288,
 289,
 290,
 291,
 292,
 293,
 294,
 295,
 296,
 297,
 298,
 299,
 300,
 301,
 302,
 303,
 304,
 305,
 306,
 307,
 308,
 309,
 310,
 311,
 312,
 313,
 314,
 315,
 316,
 317,
 318,
 319,
 320,
 321,
 322,
 323,
 324,
 325,
 326,
 327,
 328,
 329,
 330,
 331,
 332,
 333,
 334,
 335,
 336,
 337,
 338,
 339,
 340,
 341,
 342,
 343,
 344,
 345,
 346,
 347,
 348,
 349,
 350,
 351,
 352,
 353,
 354,
 355,
 356,
 357,
 358,
 359,
 360,
 361,
 362,
 363,
 364,
 365,
 366,
 367,
 368,
 369,
 370,
 371,
 372,
 373,
 374,
 375,
 376,
 377,
 378,
 379,
 380,
 381,
 382,
 383,
 384,
 385,
 386,
 387,
 388,
 389,
 390,
 391,
 392,
 393,
 394,
 395,
 396,
 397,
 398,
 399]

In [63]: x = range(400) 

In [64]: y = [test_len(i) for i in range(400)] 

In [65]: plt.plot(x,y) 
---------------------------------------------------------------------------
TclError                                  Traceback (most recent call last)

/home/kjoyce/2011_summer/LCS_project/ocean_data/AKNS/netcdf_global_ocean_export.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/usr/lib/pymodules/python2.7/matplotlib/pyplot.pyc in plot(*args, **kwargs)
   2132 # changes will be lost

   2133 def plot(*args, **kwargs):
-> 2134     ax = gca()
   2135     # allow callers to override the hold state by passing hold=True|False

   2136     washold = ax.ishold()

/usr/lib/pymodules/python2.7/matplotlib/pyplot.pyc in gca(**kwargs)
    580     """
    581 
--> 582     ax =  gcf().gca(**kwargs)
    583     return ax
    584 

/usr/lib/pymodules/python2.7/matplotlib/pyplot.pyc in gcf()
    274         return figManager.canvas.figure
    275     else:
--> 276         return figure()
    277 
    278 fignum_exists = _pylab_helpers.Gcf.has_fignum

/usr/lib/pymodules/python2.7/matplotlib/pyplot.pyc in figure(num, figsize, dpi, facecolor, edgecolor, frameon, FigureClass, **kwargs)
    252                                              frameon=frameon,
    253                                              FigureClass=FigureClass,
--> 254                                              **kwargs)
    255 
    256         # make this figure current on button press event


/usr/lib/pymodules/python2.7/matplotlib/backends/backend_tkagg.pyc in new_figure_manager(num, *args, **kwargs)
     88     FigureClass = kwargs.pop('FigureClass', Figure)
     89     figure = FigureClass(*args, **kwargs)
---> 90     window = Tk.Tk()
     91     canvas = FigureCanvasTkAgg(figure, master=window)
     92     figManager = FigureManagerTkAgg(canvas, num, window)

/usr/lib/python2.7/lib-tk/Tkinter.pyc in __init__(self, screenName, baseName, className, useTk, sync, use)
   1686                 baseName = baseName + ext
   1687         interactive = 0
-> 1688         self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
   1689         if useTk:
   1690             self._loadtk()

TclError: couldn't connect to display ":0"

In [66]: % 
%Exit            %bookmark        %dirs            %logoff          %p               %popd            %quickref        %runlog          %unalias
%Pprint          %cd              %doctest_mode    %logon           %page            %profile         %quit            %save            %upgrade
%Quit            %clear           %ed              %logstart        %paste           %prun            %r               %sc              %who
%alias           %color_info      %edit            %logstate        %pdb             %psearch         %rehash          %store           %who_ls
%autocall        %colors          %env             %logstop         %pdef            %psource         %rehashx         %sx              %whos
%autoindent      %cpaste          %exit            %lsmagic         %pdoc            %pushd           %rep             %system_verbose  %xmode
%automagic       %debug           %hist            %macro           %pfile           %pwd             %reset           %time            
%bg              %dhist           %history         %magic           %pinfo           %pycat           %run             %timeit          

In [66]: echo $DISPLAY 
------------------------------------------------------------
   File "<ipython console>", line 1
     echo $DISPLAY
          ^
SyntaxError: invalid syntax


In [67]: exec('echo $DISPLAY') 
------------------------------------------------------------
   File "<string>", line 1
     echo $DISPLAY
          ^
SyntaxError: invalid syntax


In [68]: plt. 
Display all 217 possibilities? (y or n)
plt.Annotation               plt.__getattribute__         plt.colorbar                 plt.hold                     plt.rgrids
plt.Arrow                    plt.__hash__                 plt.colormaps                plt.hot                      plt.savefig
plt.Artist                   plt.__init__                 plt.colors                   plt.hsv                      plt.scatter
plt.AutoLocator              plt.__name__                 plt.connect                  plt.imread                   plt.sci
plt.Axes                     plt.__new__                  plt.contour                  plt.imsave                   plt.semilogx
plt.Button                   plt.__package__              plt.contourf                 plt.imshow                   plt.semilogy
plt.Circle                   plt.__reduce__               plt.cool                     plt.interactive              plt.set_cmap
plt.Figure                   plt.__reduce_ex__            plt.copper                   plt.ioff                     plt.setp
plt.FigureCanvasBase         plt.__repr__                 plt.csd                      plt.ion                      plt.show
plt.FixedFormatter           plt.__setattr__              plt.dedent                   plt.is_numlike               plt.silent_list
plt.FixedLocator             plt.__sizeof__               plt.delaxes                  plt.is_string_like           plt.specgram
plt.FormatStrFormatter       plt.__str__                  plt.disconnect               plt.ishold                   plt.spectral
plt.Formatter                plt.__subclasshook__         plt.draw                     plt.isinteractive            plt.spring
plt.FuncFormatter            plt._backend_selection       plt.draw_if_interactive      plt.jet                      plt.spy
plt.IndexLocator             plt._imread                  plt.errorbar                 plt.legend                   plt.stem
plt.Line2D                   plt._imsave                  plt.figaspect                plt.loglog                   plt.step
plt.LinearLocator            plt._interactive_bk          plt.figimage                 plt.matplotlib               plt.subplot
plt.Locator                  plt._pylab_helpers           plt.figlegend                plt.matshow                  plt.subplot_tool
plt.LogFormatter             plt._setp                    plt.fignum_exists            plt.minorticks_off           plt.subplots_adjust
plt.LogFormatterExponent     plt._x                       plt.figtext                  plt.minorticks_on            plt.summer
plt.LogFormatterMathtext     plt.acorr                    plt.figure                   plt.mlab                     plt.suptitle
plt.LogLocator               plt.annotate                 plt.fill                     plt.new_figure_manager       plt.switch_backend
plt.MaxNLocator              plt.arrow                    plt.fill_between             plt.normalize                plt.sys
plt.MultipleLocator          plt.autumn                   plt.fill_betweenx            plt.np                       plt.table
plt.Normalize                plt.axes                     plt.findobj                  plt.over                     plt.text
plt.NullFormatter            plt.axhline                  plt.flag                     plt.pcolor                   plt.thetagrids
plt.NullLocator              plt.axhspan                  plt.gca                      plt.pcolormesh               plt.title
plt.PolarAxes                plt.axis                     plt.gcf                      plt.pie                      plt.twinx
plt.Polygon                  plt.axvline                  plt.gci                      plt.pink                     plt.twiny
plt.Rectangle                plt.axvspan                  plt.get                      plt.plot                     plt.vlines
plt.ScalarFormatter          plt.bar                      plt.get_backend              plt.plot_date                plt.waitforbuttonpress
plt.Slider                   plt.barbs                    plt.get_cmap                 plt.plotfile                 plt.winter
plt.SubplotTool              plt.barh                     plt.get_current_fig_manager  plt.plotting                 plt.xcorr
plt.Text                     plt.bone                     plt.get_fignums              plt.polar                    plt.xlabel
plt.TickHelper               plt.box                      plt.get_plot_commands        plt.prism                    plt.xlim
plt.Widget                   plt.boxplot                  plt.get_scale_docs           plt.psd                      plt.xscale
plt.__builtins__             plt.broken_barh              plt.get_scale_names          plt.pylab_setup              plt.xticks
plt.__class__                plt.cla                      plt.getp                     plt.quiver                   plt.ylabel
plt.__delattr__              plt.clabel                   plt.ginput                   plt.quiverkey                plt.ylim
plt.__dict__                 plt.clf                      plt.gray                     plt.rc                       plt.yscale
plt.__doc__                  plt.clim                     plt.grid                     plt.rcParams                 plt.yticks
plt.__docstring_addendum     plt.close                    plt.hexbin                   plt.rcParamsDefault          
plt.__file__                 plt.cm                       plt.hist                     plt.rcdefaults               
plt.__format__               plt.cohere                   plt.hlines                   plt.register_cmap            

In [68]: plt.pylab_setup 
Out[68]: <function pylab_setup at 0xa83ab8c>

In [69]: plt.pylab_setup? 
Type:           function
Base Class:     <type 'function'>
String Form:    <function pylab_setup at 0xa83ab8c>
Namespace:      Interactive
File:           /usr/lib/pymodules/python2.7/matplotlib/backends/__init__.py
Definition:     plt.pylab_setup()
Docstring:
    return new_figure_manager, draw_if_interactive and show for pylab


In [70]: quit() 
Do you really want to exit ([y]/n)? y  
