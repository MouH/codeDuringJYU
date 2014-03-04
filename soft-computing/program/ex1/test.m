clear;clc;
tic

% This is a test file for GoldenSection algorithm

% set initial variables
experiment_time = 20;
initial_x = [2.5, 2.5];
initial_temperature = 1 : experiment_time;
termination_factor = 0.001;

minimum = 1 : experiment_time;
final_x = ones( experiment_time, 2 );
% goldensection search
for i = 1 : experiment_time,
	[ final_x(i,:), total_steps ] = f_SA(initial_x, initial_temperature(i), termination_factor, @f_objectFunction, @f_stepGenerate);
	minimum(i) = f_objectFunction(final_x(i,:));
end

% print result

printf('The optimize value is\n');


plot(initial_temperature, minimum);
xlabel('Temperature');
ylabel('Objective Function Value');
axis([0,20,0,1]);



toc