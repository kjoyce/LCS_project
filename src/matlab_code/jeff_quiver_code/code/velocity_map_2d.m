%the code is used to read velocity data in text files and write in matlab data files

clear
clc

file=['filename']	%name the data fule
[h, A] = hdrload(file);
B=sortrows(A,1);
ndata=max(size(A));
nx=46;			%# of nodes in x
ny=34;			%# of nodes in y
xcoor=B(1:nx,1);	%x coordinates
ycoor=A(1:ny,2);
[xloc yloc]=meshgrid(xcoor,ycoor);
save('xgrid','xcoor');
save('ygrid','ycoor');

nfile=545;

for i=1:nfile
    clear u v;
    file=['filename' num2str(i)];	%i is the index of frame #
    eval(expression);
    for j=1:nx
        u(1:ny,j)=A(1+ny*(j-1):ny*j,3);
        v(1:ny,j)=A(1+ny*(j-1):ny*j,4);
    end 
    expression=['u' num2str(i) '=u'';'];
    eval(expression);
    expression=['v' num2str(i) '=v'';'];
    eval(expression);
    expression=['save(''U_T' num2str(i) ''',''u' num2str(i) ''');'];
    eval(expression);
    expression=['save(''V_T' num2str(i) ''',''v' num2str(i) ''');'];
    eval(expression);
    expression=['clear u' num2str(i) ' v' num2str(i) ';'];
    eval(expression);
    if mod(i,10)==0
        c_proc = strcat( 'process accomplished :  ', ...
            num2str( 100*(i-1)/(nfile-1),' %03.0f' ), '/100' );
        disp( c_proc );
    end
end
