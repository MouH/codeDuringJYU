% ==================================================================
%  
%   Programming Assignment
%   TIES483 - Nonlinear Optimization
% 
%   Author: Mou Hao
% 
%  ==================================================================


%% ============ Conjugate Gradient Method =================

function [x, iteration, fval, flag] = f_conjugateGradient (fun, x0, eps)
%  ==================================================================
%  Conjugate Gradients method.
%
%    Input parameters: 
%         fun : objective function
%          x0 : starting point
%         eps : tolerance
%         
%    Output parameters:
%           x : minimizer
%   iteration : iteration times
%        fval : objective value of minimizer
%        flag : 1 if convergence criteria specified by TOL could
%               not be fulfilled within the specified maximum
%               number of iterations, 0 otherwise (= iteration
%               successful).
%
%    >> [minimizer, faval, flag] = f_conjugateGradient(@myfun, x0, eps);
%
%  ==================================================================

% set parameter of subproblem which using golden section
a_initial = -10;
b_initial = 10;
final_interval = 0.05;

% initial
h = 1; % iteration times
yi = x0;
xi = yi;
j = 1;
[n,m] = size(x0(:)); % size of x

[objectValue, gradient1] = fun(yi);
d = - gradient1;

while norm(gradient1) > eps
    % minimizer = f_goldenSection(a_initial, b_initial, final_interval, @(a) fun( yi + a * d ))
    minimizer = f_goldenSection(a_initial, b_initial, final_interval, @(a) f_helpCG( yi, a, d ))
    yi = yi + minimizer * d;

    if j == n
    	xi = yi;
    	j = 1;
    	h = h + 1;
    	continue;
    else
    	[objectValue, gradient2] = fun(yi);
    	d = -gradient2 + norm(gradient2) ^ 2 / ( norm(gradient1) ^ 2 ) * d;
    	j = j + 1;
    	gradient1 = gradient2;
    end
end

iteration = h;
x = xi;
fval = objectValue;
flag = 1;

end