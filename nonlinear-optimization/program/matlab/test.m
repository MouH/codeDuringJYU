% ==================================================================
%  
%   Programming Assignment
%   TIES483 - Nonlinear Optimization
% 
%   Author: Mou Hao
% 
%  ==================================================================
%
% In the exercise contains the following optimization function
%

% Initialization
clear; close all; clc

%% =================Line Search=================
fprintf('Test of line search method \n');
fprintf('Press enter to continue\n');
pause;

%% =================Golden Section=================
% golden section
fprintf('\n1. Testing Golden Section method\n ');
% set initial interval
a_initial = -10;
b_initial = 10;
final_interval = 0.05;

% print initial info
fprintf('\nInitial interval is [ %f, %f ]\n', a_initial, b_initial);
fprintf('Target final interval range is %f\n\n', final_interval);
fprintf('Objective Function: y = ( x - 2 ) ^ 2\n\n');
fprintf('Implement GoldenSection search method.........\n\n');

% goldensection search
[minimizer, iterations] = f_goldenSection(a_initial, b_initial, final_interval, @f_objectFunction1);

% print result
fprintf('The minimizer is %f\n', minimizer);
fprintf('The total iteration is %d \n\n', iterations);

fprintf('Press enter to continue\n');
pause;


clc
%% =================Unconstrained Optimization=================
% Nelder Mead Method

% set initial point
x0 = [1,1];

fprintf('\n2. Testing Nelder Mead Method\n\n');
fprintf('Objective Function: y = ( x(1)^2 + x(2) - 11 ) ^ 2 + ( x(2) ^ 2 + x(1) -7 ) ^ 2\n');
fprintf('Initial point at\n');
x0
fprintf('Implement Nelder Mead search method.........\n\n');

[minimizer, fval, flag] = f_nelderMead(@f_objectFunction2, x0);
if flag == 1
	fprintf('Find a optimization point\n\n');
	minimizer
    fprintf('The objective value is %d \n\n', fval);
else
	fprintf('Unable to find a optimization point\n');
end


fprintf('Press enter to continue\n');
pause;

%% =================Constrained Optimization=================