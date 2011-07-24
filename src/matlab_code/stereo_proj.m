% -- Projects a regular grid on the surface of a sphere to a plane by standard stereographic projections.
function [x y] = stereo_proj(lon,lat)
% x	an array with the same dimensions as lon and lat that is the x-coordinates of stereographic projection of the given latitude and longitude grid.
% y	the y coordinates of the projected grid
% lon	the longitude coordinates of a regular grid on the surface of a sphere
% lat	the latitude coordinates of a regular grid on the surface of a sphere with 0 at the equator

R = 63781000;
% Rotate to sphereical coordinates, and rotate so that the central meridian is the first longitude coordinate
lon = lon - lon(1);
lat = 90 - lat;

lat = pi/180*lat;
lon = pi/180*lon;

% This is stereographic projection for spherical coordinate domain
x = cos( lon ) ./ tan( lat/2 );
y = sin( lon ) ./ tan( lat/2 );

% rotate so that the north pole is upwards
[x y] = rotate_pts(x,y,-(abs(lon(1,1) - lon(end,end))/2 + pi/2));
x = R*x;
y = R*y;
end;

% -- Rotate points on a plane by angle 'th' measured in radians
function [xx yy] = rotate_pts(x,y,th)
xx = x * cos(th) - y*sin(th);
yy = x * sin(th) + y*cos(th);

% Example usage
% [lon lat] = meshgrid( linspace(45,75,200), linspace(-175,-150,400));
% [x y] = stereo_proj(lon,lat);
end;
