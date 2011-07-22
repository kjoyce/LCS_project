clear
clc

T0=200911;
iT=2;
folder=[num2str(T0) num2str(iT,'%02.2d') '00'];

nx=139;
ny=107;
nz=29;

iiT=0;
for iT=2:10
    
    if iiT==0
        mkdir('../velocity data/',folder);
        output_dir=['../velocity data/' folder '/'];
    end
    
    folder=[num2str(T0) num2str(iT,'%02.2d') '00'];
    dir=['../original data/' folder '/'];
    
    file=[dir 'hour' num2str(0,'%02.2d') '.dat']
    A=dlmread(file);
    for iz=1:nz
        for iy=1:ny
            u(1:nx,iy,iz)=A(nx*ny*(iz-1)+nx*(iy-1)+1:nx*ny*(iz-1)+nx*iy,1);
            v(1:nx,iy,iz)=A(nx*ny*(iz-1)+nx*(iy-1)+1:nx*ny*(iz-1)+nx*iy,2);
            w(1:nx,iy,iz)=A(nx*ny*(iz-1)+nx*(iy-1)+1:nx*ny*(iz-1)+nx*iy,3);
        end
    end
    
    expression=['u' num2str(iiT) '=u;'];
    eval(expression);
    expression=['v' num2str(iiT) '=v;'];
    eval(expression);
    expression=['w' num2str(iiT) '=w;'];
    eval(expression);
    expression=['save(''' output_dir 'U_T' num2str(iiT) ''',''u' num2str(iiT) ''');'];
    eval(expression);
    expression=['save(''' output_dir 'V_T' num2str(iiT) ''',''v' num2str(iiT) ''');'];
    eval(expression);
    expression=['save(''' output_dir 'W_T' num2str(iiT) ''',''w' num2str(iiT) ''');'];
    eval(expression);
    expression=['clear u' num2str(iiT) ' v' num2str(iiT) ' w' num2str(iiT) ';'];
    eval(expression);     
    
    iiT=iiT+1;
    
    folder=[num2str(T0) num2str(iT,'%02.2d') '12'];
    dir=['../original data/' folder '/'];
    
    file=[dir 'hour' num2str(0,'%02.2d') '.dat']
    A=dlmread(file);
    for iz=1:nz
        for iy=1:ny
            u(1:nx,iy,iz)=A(nx*ny*(iz-1)+nx*(iy-1)+1:nx*ny*(iz-1)+nx*iy,1);
            v(1:nx,iy,iz)=A(nx*ny*(iz-1)+nx*(iy-1)+1:nx*ny*(iz-1)+nx*iy,2);
            w(1:nx,iy,iz)=A(nx*ny*(iz-1)+nx*(iy-1)+1:nx*ny*(iz-1)+nx*iy,3);
        end
    end
    
    expression=['u' num2str(iiT) '=u;'];
    eval(expression);
    expression=['v' num2str(iiT) '=v;'];
    eval(expression);
    expression=['w' num2str(iiT) '=w;'];
    eval(expression);
    expression=['save(''' output_dir 'U_T' num2str(iiT) ''',''u' num2str(iiT) ''');'];
    eval(expression);
    expression=['save(''' output_dir 'V_T' num2str(iiT) ''',''v' num2str(iiT) ''');'];
    eval(expression);
    expression=['save(''' output_dir 'W_T' num2str(iiT) ''',''w' num2str(iiT) ''');'];
    eval(expression);
    expression=['clear u' num2str(iiT) ' v' num2str(iiT) ' w' num2str(iiT) ';'];
    eval(expression);     
    
    iiT=iiT+1;
    
%     c_proc = strcat( 'process accomplished :  ', ...
%         num2str( 100*iT/(nT+1),' %03.0f' ), '/100' );
%     disp( c_proc );
end