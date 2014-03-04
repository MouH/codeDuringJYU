% ------------------------------
% f_variablesGeneration is a function to generate optimal 
% variables for GA demo use.
%
% Input: 1. numbers of variables
%        2. population
%        3. genome length
%        
% ------------------------------
function varialbes = f_variablesGeneration (variablesNums, population, genomeLength)

varialbes = round(rand(population, variablesNums * genomeLength));

end