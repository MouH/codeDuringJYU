function alarm = is_alarm(previous_data, data)
    if data - mean(previous_data) >= std(previous_data) * 1
        alarm = 1;
    else
        alarm = 0;
    end
end