function value = f_objectFunction1(x)    
% ObjectFunction should be changed with different optimization problem

% x is a one dimension variable

fileID = fopen('input.txt', 'w');
fprintf(fileID, '%f', x);
fclose(fileID);

%system('wine prob1.exe');
system('prob1.exe');

% read the output file
fileID = fopen('output.txt', 'r');
formatSpec = "%f";
A = fscanf(fileID, formatSpec);

% requires no gradient info
value = A(1,:);


end
