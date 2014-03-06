% ==================================================================
%  
%   Programming Assignment
%   TIES483 - Nonlinear Optimization
% 
%   Author: Mou Hao
% 
%  ==================================================================


%% ============ Nelder Mead Method (Downhill simplex)=================

function [x, fval, flag] = f_nelderMead(fun, x0, max_iteration, eps)

%% ==================================
  % f_nelderMead() function takes 
  
  % 4 inputs:
  %   - fun, an objective function
  %   - x0, a start point
  %   - max_iteration, maximum iteration time, defalut to be 10000
  %   - eps, tolerance for terminate, defalut to be 1e-5
  % in which, the frist two parameters are required.
  
  % return:
  %   - x, minimizer value
  %   - fval, objective of minimizer
  %   - flag, tag for wether a minimier is found with this algorithm, where 1 means true, 0 means false

  % >>[minimizer, fval, flag] = f_nelderMead(@f_objectFunction, x0);
%% ==================================

% parameter check
if nargin < 2
	error('please pass at least 2 parameters');
end

% defalut value
if nargin < 3
	max_iteration = 10000;
end
if nargin < 4
	eps = 1e-5; % tolerance
end

% initialize
n = length(x0); % number of dimension
x0 = x0(:)'; % change x0 to column vector

% construct initial simplex
% the i'th row is the i'th simplex
simplex = [x0];
value_of_simplex = [fun(x0)];
for i = 1 : n
	x = x0;
	if x(i) == 0
		x(i) = 0.00025;
	else
		x(i) = x(i) * 1.05;
	end
	value_of_simplex = [value_of_simplex; fun(x)];
    simplex = [simplex; x];
end

% combine the value and simplex together
mat = [value_of_simplex, simplex];

% start iteration
while max_iteration > 0

    % sort the value in mat from low to high
    mat = sortrows(mat, 1);

	% convergence test
	% if the objective value for every simplex is all most the same
	if max( mat(:,1) ) - min( mat(:,1) ) < eps
		break
	end

    % generate the middle point
	middle_point = mean(mat(1:n,2:end), 1); % middle point without worst value x(n+1)
	
    % generate the reflect point and its value
	reflect_point = 2 * middle_point - mat(n+1, 2:end);
    value_reflect_point = fun(reflect_point);

    % minus iteration_time
    max_iteration = max_iteration - 1;

    if mat(1,1) <= value_reflect_point && value_reflect_point < mat(n,1)
    	% determine wether to accept reflect point
    	mat(n+1,:) = [value_reflect_point, reflect_point]; 
    	continue
    elseif value_reflect_point < mat(1,1)
    	% generate the expand point
    	expand_point = middle_point + 2 * ( middle_point - mat(n+1, 2:end) );
    	value_expand_point = fun(expand_point);

    	if value_expand_point < value_reflect_point
    		% determine wether to accept expand point
    		mat(n+1,:) = [value_expand_point, expand_point];
    		continue
    	else
    		% otherwise accept reflect point
    		mat(n+1,:) = [value_reflect_point, reflect_point];
    		continue
    	end
    else
        % perform a contract
    	% to choose wether an outside contract or an inside contract
    	if value_reflect_point < mat(n+1,1)
    		% generate an outside contract
    		outside_contract_point = ( middle_point + reflect_point ) / 2;
    		value_outside_contract_point = fun(outside_contract_point);

    		if value_outside_contract_point < value_reflect_point
    			% accept outside contract point
    			mat(n+1,:) = [value_outside_contract_point, outside_contract_point];
    			continue
    		end
    	else
    		% generate inside contract point
    		inside_contract_point = ( middle_point + mat(n+1, 2:end) ) / 2;
    		value_inside_contract_point = fun(inside_contract_point);

    		if value_inside_contract_point < mat(n+1,1)
    			% accept inside contract point
    			mat(n+1,:) = [value_inside_contract_point, inside_contract_point];
    			continue
    		end
    	end
    end

    % do a shrink if above if-else statement do not terminate the iteration
    shrink = (mat(2:end, 2:end) + (diag(mat(1,2:end))*ones(size(mat(2:end, 2:end)))')') / 2;
    mat = [ mat(:,1), [ mat(1,2:end); shrink ] ];		

end
% iteration ends

% assignment the rentrun value
x = mat(1, 2:end);
fval = mat(1,1);

if max_iteration > 0
	flag = 1; % find a minimier
else
	flag = 0; % not find a minimier
end

end