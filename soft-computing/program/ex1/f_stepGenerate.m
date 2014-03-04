function x_modify = f_stepGenerate(x)
% This is a function use to modify x one step further

% assume on every dimension of x, xi is changing at random at range (0, 0.1)
i = -0.05;
j = -1/(2*i);
change_length =  i + rand(size(x)(1), size(x)(2)) / j;

x_modify = x + change_length;

% boundary check
if x_modify(1) > 5
	x_modify(1) = 5;
elseif x_modify(1) < 0
	x_modify(1) = 0;
end

if x_modify(2) > 5
	x_modify(2) = 5;
elseif x_modify(2) < 0
	x_modify(2) = 0;
end

end