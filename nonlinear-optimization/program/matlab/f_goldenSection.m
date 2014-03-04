% ==================================================================
%  
%   Programming Assignment
%   TIES483 - Nonlinear Optimization
% 
%   Author: Mou Hao
% 
%  ==================================================================


%% ============Golden Section Method=================

function [minimizer, h] = f_goldenSection(a, b, L, f_objectFunction)
% f_goldenSection function is a implementation of line search
% Passing a initial interval [a,b], final interval length L
% and a f_onjectFunction

% Golden ratio
C = ( sqrt(5) - 1 ) / 2;

% initial
ai = a;
bi = b;
xi = ai + ( 1 - C ) * ( bi - ai );
yi = ai + C * ( bi - ai );
h = 1; %iteration times

% compute initial objectFunction of xi and yi
cost_xi = f_objectFunction(xi);
cost_yi = f_objectFunction(yi);

% start elimination
while ( bi - ai ) > L
	if cost_xi <= cost_yi
		% ai not change
		bi = yi;
		yi = xi;
		xi = ai + ( 1 - C ) * ( bi - ai );
		cost_yi = cost_xi;
		cost_xi = f_objectFunction(xi);
		h = h + 1;
	else
		% bi not change
		ai = xi;
		xi = yi;
		yi = ai + C * ( bi - ai);
		cost_xi = cost_yi;
		cost_yi = f_objectFunction(yi);
		h = h + 1;
	end
end

a_final = ai;
b_final = bi;
minimizer = ( ai + bi ) / 2;

end 