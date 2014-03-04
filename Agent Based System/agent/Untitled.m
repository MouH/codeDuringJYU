% Simulation of Agent-Based System
clear; close all; clc;

% Generate normal distribution data
data = normrnd(5,1,10000,10);

% Alarm
alarm = zeros(10000, 10);

% Judge the alarm point
for i = 11:10000
    for j = 1:10
        alarm(i,j) = is_alarm(data(i-10:i-1,j), data(i,j));
    end
end

% sum
full_point = sum(alarm, 2);

% plot
n = hist(full_point)
