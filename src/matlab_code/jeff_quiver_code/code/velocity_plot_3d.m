clear
clc

folder=['2010041400'];
dir=['../velocity data/' folder '/'];

nx=41;
ny=44;
nz=26;

nT=5;
iz=12;
m=0.5;

load('xgrid');
load('ygrid');

xmin=min(xcoor);
xmax=max(xcoor);
ymin=min(ycoor);
ymax=max(ycoor);
[xmesh ymesh]=meshgrid(xcoor,ycoor);

figure
for iT=0:nT
    expression=['load(''' dir 'U_T' num2str(iT) '.mat'');'];
    eval(expression);
    expression=['load(''' dir 'V_T' num2str(iT) '.mat'');'];
    eval(expression);
    expression=['load(''' dir 'W_T' num2str(iT) '.mat'');'];
    eval(expression);
    expression=['u=u' num2str(iT) ';'];
    eval(expression);
    expression=['v=v' num2str(iT) ';'];
    eval(expression);
    expression=['w=w' num2str(iT) ';'];
    eval(expression);
    expression=['clear u' num2str(iT) ' v' num2str(iT) ' w' num2str(iT) ';'];
    eval(expression);
    
    umesh=u(:,:,iz);
    vmesh=v(:,:,iz);
    
    clf
    quiver(resizem(xmesh,m),resizem(ymesh,m),resizem(umesh',m),resizem(vmesh',m),2);
    hold on
    axis equal
    axis([xmin xmax ymin ymax]);
    pause(0.2)
end