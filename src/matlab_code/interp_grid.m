% -- Makes a regular grid from the  image of stereographic projection using 2d linear interpolation
function [xx yy] = interp_grid( x,y,z,nx,ny )
% xx	interpolated x-coordinates
% yy	interpolated y-coordinates
% x	x-coordinates of stereographic projection
% y	y-coordinates of stereographic projection
% nx	number of points in grid x dimension
% ny	number of points in grid y dimension
%
%     /`-_-'\
%    /       \
%    `-_   _-'
%       `-'
% Stereographic projection sends longitude lines to rays through the origin
% on the plane and latitude lines to circles centered at the origin. Hence,
% we can easily find the coordinates of the largest rectangle that fits
% inside the region defined by the stereographic projection output. 
xmin = x(1,1)
xmax = -xmin

ind = find(x(:,end) > xmin,1,'first')
[nny, mmy] = size(y)

ymin = y(ind,end)
ymax = ymax = y(floor(nny/2),1)

xx = linspace(xmin,xmax,nx)
yy = linspace(ymin,ymax,ny)


