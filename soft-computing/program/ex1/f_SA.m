function [final_x, total_steps] = f_SA(initial_x, initial_temperature, termination_factor, f_objectFunction, f_stepGenerate)
% simulated annealing

% initial variables
steps = 0;
temperature = initial_temperature;
x = initial_x;

% start
while (temperature>0)
	f1 = f_objectFunction(x);
	x_modify = f_stepGenerate(x);
	f2 = f_objectFunction(x_modify);
	
	f_different = f2 - f1;
	
	if f_different <= 0
		x = x_modify;
	else
		if rand() < exp( -f_different / temperature )
			x = x_modify;
		end
	end	
	
	temperature = temperature - termination_factor;
	steps = steps + 1;
	
end

% result
final_x = x;
total_steps = steps;

end