clc;
clear;
close all;
Dataset=load('mydataset.txt');
InputsData=Dataset(:,1:end-1);
OutputData=Dataset(:,end);
% inp=Dataset.dataset;
 x=InputsData';
t=OutputData';
a=1;
b=13;
c=14;
data.x=x;
data.t=t;
data.nx=size(x,1);
data.nt=size(t,1);
data.nSample=size(x,2);
nVar=data.nx;       

print("this is azaduniver branch")