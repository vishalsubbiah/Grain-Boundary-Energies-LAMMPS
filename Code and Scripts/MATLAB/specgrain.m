clear
clc
GBEValues=importdata('GBEValues.csv');
Data=GBEValues.data;
TextData=GBEValues.textdata;

DataEng=Data(:,1);
DataTheta=Data(:,2);

AlEng=DataEng(1:16,1);
CuEng=DataEng(17:32,1);
NiEng=DataEng(33:48,1);

AlTheta=DataTheta(1:16,1);
CuTheta=DataTheta(17:32,1);
NiTheta=DataTheta(33:48,1);
position=[NiEng(2:15)+200, NiTheta(2:15)];
hold on;
axis([0 90 0 3000]);
set(gca,'FontSize',16);
scatter(AlTheta,AlEng,'r','s','filled');
scatter(CuTheta,CuEng,'b','s','filled');
scatter(NiTheta,NiEng,'g','s','filled');

line(AlTheta,AlEng,'Color','r');
line(CuTheta,CuEng,'Color','b');
line(NiTheta,NiEng,'Color','g');
xlabel('Misorientation Angle (degrees)');
ylabel('GB Energy (mJ/m^2)');
legend('Al','Cu','Ni');
%for i=1:14
%text(NiTheta(i+1),NiEng(i+1),TextData(i+1,5),'VerticalAlignment','top','Position',[position(i,2) position(i,1)]);
%end