%
% First exercises: Introduction to data stuff using Matlab
% GOAL: Go through the macro below line-by-line, see what happens and
%  then study the documentation of the corresponding commands so that
%  you are ready to use them yourself in what follows
%
clear, close all %Clarify the workspace and close all windows for fresh start
%Consult: http://en.wikipedia.org/wiki/Fisher%27s_iris
load fisheriris %Load sample data file (Matlab's internal sample)
doc load %Let's open documentation window for the previous command
DataName = 'Iris'; %String for data name
X = meas; %Allocate new variable for input data matrix
min(X), max(X) %Minimums and maximums of varibles/attributes in input;
% observe the columwise behavior of the previous command, in comparison to
min(min(X)), max(max(X))
[N,n] = size(X) %New variables for amount of observations and size of vectors
% Notice that without ';' at the end of line the result of operation is shown
%
% One can separate parts of macro using double %%, and then use Cntr+Enter
%  to run the macro in blocks that have been defined
%
% The next comment with double %%+space' ' creates a break and block sections
% in this macro; the blocks can be run sequentially one by one with
% the shortcut Ctrl+Enter. Try this!
%% Writing formatted data into screen (i.e. standard output)
fprintf('%s data set: Nbr obs = %3d, size of inputs = %2d\n\n',DataName,N,n);
%% 
Classes = zeros(N,1); %Initializing new variable; should do this always before use
%
% This is the loop way, typical for procedural programming languages
for i=1:N %Loop to encode class label strings into numbers
    if (strcmp(species(i),'setosa')) Classes(i) = 1;
    elseif (strcmp(species(i),'versicolor')) Classes(i) = 2;
    elseif (strcmp(species(i),'virginica')) Classes(i) = 3;
    end
end
%
% This is the Matlab style, uses vectorial structures and their operations directly
Classes2(strcmp(species,'setosa')) = 1;
Classes2(strcmp(species,'versicolor')) = 2;
Classes2(strcmp(species,'virginica')) = 3;
norm(Classes-Classes2') %Check whether we obtain same results, up to transpose
whos %Current variables in workspace ("Workspace" in Matlab main window)
clear meas %free memory by clearing variable allocations
ncls = max(Classes);
for c=1:ncls
    Xcls = X(Classes == c,:); %This is direct way to obtain subset of data
    I = find(Classes == c); %Indeces representing class c
    min(X(I,:)) %or min(Xcls)
    [Y,J] = min(X(I,3)); %Value and index of class c's third variable's min
    clssize = length(I); %Size of class c = length of index vector I,
                         % or size(Xcls,1) 
    fprintf('Class %1d: abs freq = %2d, rel freq = %4.2f\n',c,clssize,...
        100*clssize/N);
    %If you understand this subindecing example you are almost MATLAB pro
    fprintf('Class %1d: min for variable 3 = %4.2f in index %2d\n',c,Y,I(J));    
end
%
% And then to visualizations, one of main reasons for popularity of Matlab
%
titstr = strcat(DataName,': histogram of 3rd variable'); %Creating title with name of data
hist(X(:,3)) %Histogram for third variable: discrete distribution of values
title(titstr)
% Next plot draws all input values separately into same window
figure, plot(X), title('Input variables'),...
    legend('Var 1','Var 2','Var 3','Var 4','Location','NorthWest')
% NOTE: From Figure window you can change values of all the properties;
%  E.g. Increase the font in axis tick labels into 25 (Edit/Axes Properties/More Properties)
% Let's scale the input and draw individual plots with different colors
%
lstyles = {'bx-','g+:','r*-.','co--'}; %Own linestyle for each variable, set of strings
Z = zscore(X); %Normalizing the input variables using linear scaling
figure
for i=1:n
    subplot(4,1,i), plot(Z(:,i),lstyles{i})
end
mean(Z) %Compute and plot means of scaled data
%
% Other way round, i.e. let's study observations through variables
labels = {'Sepal Length','Sepal Width','Petal Length','Petal Width'};
figure, parallelcoords(X,'group',species,'labels',labels);
% If you are interested, you can also study other Multivariate Plots
%  provided by Matlab using doc/help window
% 
% From one dimensional plots to two dimensional scatterings
Colors = lines(ncls); %Own color for each class
markers = {'x','+','*'}; %Own marker for each class
figure
for c=1:ncls
    I = find(Classes == c);
    scatter(X(I,1),X(I,3),88,markers{c},'CData',Colors(c,:)), hold on
end
legend('Class 1','Class 2','Class 3') %Not fancy version, 
% include sufficient amount of these namestrings by hand
title('Scattered values of 1st and 3rd coordinates')
%
% With not-too-many variables both one and two dimensional plots can be
% obtained with only one command:
figure, plotmatrix(X)
%
% Is there still time left? If so find your own data to play aroung, e.g.,
% from UCI Machine Learning Repository (Search it): load and save it locally,
% and then load it in Matlab. Then repeat the analysis as below to get
% to know that particular data:
% - What were the questions that were answered through the manipulations
% and illustrations below?
% - If difficulties in choosing own data continue with
%   "seeds" Data Set from UCI... (look the file first, do something along saving, 
%    use load to bring into workspace and... ride on)
