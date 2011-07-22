%NcomCurrentsFcasts.m 
%This script retrieves Current Forecasts from NCOM global surface files
%with the format: ncom_glb_sfc_YYYYMMDD00.nc.gz 
%The U (+ eastward) and Z (+northward) are retrieved in individual
%variables at a 3 hour timestep from 0 - 72 hours.
%The source directory of the NCOM files needs to be changed by the user
%on line 32. Also, the date of the files is set by the Rollback variable on
%line 12. 
%B.Daniels 11/19/2009  NOAA/NCEP/Ocean Prediction Center
%robert.daniels@noaa.gov

Rollback =1;%Rollback number of days (0 = today, 1 = yesterday, etc.)
sourcedir = '/%%%%%/'%enter path of your source directory for Ncom file here 
%Find day of year
V = date;
N = datenum(V) - Rollback;
Day1 = datevec(datenum(date)-Rollback) %Find Day1's date 
%if month is 1-9 then add a leading 0 to string
Ayear = num2str(Day1(1));
if Day1(2)<10
    Amonth=strcat('0',num2str(Day1(2)));
else
    Amonth=num2str(Day1(2));
end
%if day is 1-9 then add a leading 0 to string
if Day1(3)<10
    Aday=strcat('0',num2str(Day1(3)));
else
    Aday=num2str(Day1(3));
end

%Change path below to directory of Ncom file
ncomfile = strcat(sourcedir,'ncom_glb_sfc_',Ayear,Amonth,Aday,'00.nc');
warning off

%% Get desired data from file and put into temporary variables
ncin = netcdf.open(ncomfile,'NC_NOWRITE');

ucur = netcdf.getVar(ncin,7,'single');
for a = 1:25;
    fcst = (a-1) * 3;
    
    if fcst < 10
	fcstname = strcat('ucurf0',num2str(fcst));    
    else
        fcstname = strcat('ucurf',num2str(fcst));	
    end
mkfcast = [fcstname, ' = transpose(ucur(:,:,:,a))/1000;'];
eval(mkfcast);
cleanfcast = [fcstname,'(find(',fcstname,' == -30))= NaN;'];
eval(cleanfcast);
end
clear ucur;
%Get V currents
vcur = netcdf.getVar(ncin,8,'single');
for b = 1:25;
    fcst = (b-1) * 3;
    if b < 10
	fcstname = strcat('vcurf0',num2str(fcst));    
    else
        fcstname = strcat('vcurf',num2str(fcst));	
    end
mkfcast = [fcstname, ' = transpose(vcur(:,:,:,b))/1000;'];
eval(mkfcast);
cleanfcast = [fcstname,'(find(',fcstname,' == -30))= NaN;'];
eval(cleanfcast);
end
clear vcur;

netcdf.close(ncin)















