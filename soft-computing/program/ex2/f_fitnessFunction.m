% ------------------------------
% This is a fitness function for testing
% ------------------------------
function fitnessValue = f_fitnessFunction (generation)

binaryToDecimalMultiplier = 2 .^ [ 9 : -1 : 0 ]';

variable_x1 = generation(:,1:10);
variable_x2 = generation(:,11:20);

x1 = ( 6 / ( 2^10 - 1 )) * variable_x1 * binaryToDecimalMultiplier;
x2 = ( 6 / ( 2^10 - 1 )) * variable_x2 * binaryToDecimalMultiplier;

fitnessValue = 1./ (( ( x1.^2 + x2 - 11 ).^2 + ( x1 + x2.^2 - 7 ).^2 ) + 1 );

end