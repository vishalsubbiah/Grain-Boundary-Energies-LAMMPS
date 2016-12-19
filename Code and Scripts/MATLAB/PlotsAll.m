clear
clc

Al_0_5=importdata('Al_0_Data_100.txt');
%Al_300_5=importdata('Al_300_Data_100.txt'); %Negative
%Al_600_5=importdata('Al_600_Data_100.txt'); %Negative
AlEng5=Al_0_5(:,2);

Al_0_10=importdata('Al_0_Data_100_large.txt');
AlEng10=Al_0_10(:,2);


Cu_0_5=importdata('Cu_0_Data_100.txt');
%Cu_300_5=importdata('Cu_300_Data_100.txt'); Negative
%Cu_600_5=importdata('Cu_600_Data_100.txt'); Negative
CuEng5=Cu_0_5(:,2);

Fe_0_5=importdata('Fe_0_Data_100.txt');
%Fe_300_5=importdata('Fe_300_Data_100.txt'); Error
%Fe_600_5=importdata('Fe_600_Data_100.txt'); Error
FeEng5=Fe_0_5(:,2);

Ni_0_5=importdata('Ni_0_Data_100.txt');
%Ni_300_5=importdata('Ni_300_Data_100.txt');
%Ni_600_5=importdata('Ni_600_Data_100.txt'); Negative
NiEng5=Ni_0_5(:,2);
%Ni300Eng5=Ni_300_5(:,2);

Na_0_5=importdata('Na_0_Data_100.txt');
%Na_300_5=importdata('Na_300_Data_100.txt'); Negative
%Na_600_5=importdata('Na_600_Data_100.txt'); Negative
NaEng5=Na_0_5(:,2);

Theta=0:1:90;

%plot(Theta,AlEng5,'g', Theta, FeEng5, 'r-', Theta, NiEng5,'k', Theta, NaEng5,'b', Theta, CuEng5,'m');
%plot(Theta,NiEng5,Theta,Ni300Eng5);
mNi=polyfit(AlEng5,NiEng5,1);
mCu=polyfit(AlEng5,CuEng5,1);
mNa=polyfit(AlEng5,NaEng5,1);
mFe=polyfit(AlEng5,FeEng5,1);

hold on;

%scatter(AlEng5, AlEng5)
%plot(AlEng5,AlEng5);

scatter( AlEng5, NiEng5,'r') 
plot(AlEng5,(mNi(1).*AlEng5+ mNi(2)),'k');

scatter( AlEng5, CuEng5,'b')
plot(AlEng5,(mCu(1).*AlEng5+ mCu(2)),'k');

%scatter(AlEng5, NaEng5,'r') 
%plot(AlEng5,(mNa(1).*AlEng5+ mNa(2)),'k');

%scatter(AlEng5, FeEng5,'b') 
%plot(AlEng5,(mFe(1).*AlEng5+ mFe(2)),'k');

axis([300 1100 -100 3200]);
set(gca,'FontSize',16);
%title('Grain Boundary Energy vs Misorientation');
xlabel('GB Energy of Al  (mJ/m^2)');
ylabel('GB Energy of FCC elements (mJ/m^2)');
h=legend('Ni - Al ','Ni - Al fit ','Cu - Al','Cu - Al fit');
%set(legend,'FontSize',16,'Orientation','horizontal');
%h.Orientation = 'horizontal';