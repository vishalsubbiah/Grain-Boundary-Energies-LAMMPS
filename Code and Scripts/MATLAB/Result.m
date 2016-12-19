dataElm=importdata('Al_0_Data_100.txt');
dataGen=importdata('AreaAtoms.txt');
K1=dataElm(:,2);
Theta=dataElm(:,1);
K1new=[0;K1(2:90);0];
%plot(Theta,K1new);
PureEng=-3.36;
n=dataGen(:,1);
A=dataGen(:,2);

TotalEng=K1.*A+PureEng.*n;

ActEng=TotalEng(1)/n(1);

K2=(TotalEng-ActEng.*n)./A;
plot(Theta,K1);
figure();
plot(Theta,K2);
figure();
plot(Theta,K1new);
%plot(Theta,K2,'b',Theta,K1,'r',Theta,K1new,'g');


