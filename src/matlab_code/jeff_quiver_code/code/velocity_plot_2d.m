%the code is used to plot velocity field

clear;
clc;
load('xgrid');
load('ygrid');
[xloc yloc]=meshgrid(xcoor,ycoor);

for i=150:5:150
    expression=['load(''U_T' num2str(i) '.mat'');'];
    eval(expression);
    expression=['load(''V_T' num2str(i) '.mat'');'];
    eval(expression);
    expression=['u=u' num2str(i) ';'];
    eval(expression);
    expression=['v=v' num2str(i) ';'];
    eval(expression);
    expression=['clear u' num2str(i) ' v' num2str(i) ';'];
    eval(expression);
    
    quiver(xloc,yloc,u',v',4);
    axis([-2 18 -14 2]);
    text1=['slide # :' num2str(i)];
    text(0,1,text1);
    pause;
end