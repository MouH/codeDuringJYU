function value = f_objectFunction3(x)    
% ObjectFunction should be changed with different optimization problem

% x is two dimensional data
global r;
fileID = fopen('input.txt', 'w');
fprintf(fileID, '%f', x(1));
fprintf(fileID, '\n');
fprintf(fileID, '%f', x(2));

fclose(fileID);

system('wine prob3.exe');

% read the output file
fileID = fopen('output.txt', 'r');
formatSpec = '%f';
A = fscanf(fileID, formatSpec);
fclose(fileID);

value1 = A(1,:);
value2 = cstr(x);



% 
value = value1 + r*value2;
% value = ( x(1)^2 + x(2) - 11 ) ^ 2 + ( x(2) ^ 2 + x(1) -7 ) ^ 2;
% value = ( x(1)-1)^2 +( x(2)-1)^2+( x(3)-1)^2;

end 