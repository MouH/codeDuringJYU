function value = f_objectFunction2(x)    
% ObjectFunction should be changed with different optimization problem

% x is two dimensional data

fileID = fopen('input.txt', 'w');
fprintf(fileID, '%f', x(1));
fprintf(fileID, '\n');
fprintf(fileID, '%f', x(2));

fclose(fileID);

%system('wine prob2.exe');
system('prob2.exe');


% read the output file
fileID = fopen('output.txt', 'r');
formatSpec = "%f";
A = fscanf(fileID, formatSpec);

value = A(1,:);

end 
