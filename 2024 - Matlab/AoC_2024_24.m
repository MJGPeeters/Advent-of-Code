%% Preamble
adventDay = 24;
testBool = 1;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
    zMax = 12;
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
    zMax = 45;
end

%% Read data
fileID = fopen(fileName);
line = fgetl(fileID);

d = dictionary;

i = 1;

while isempty(line) || all(line~=-1)
    if i<11
        tmp = strsplit(line,':');
        d(string(tmp{1})) = {double(string(tmp{2}))};
    elseif i>11
        tmp = strsplit(line);
        d(string(tmp{end})) = {{tmp{1}, tmp{2}, tmp{3}}};
    end

    i = i+1;
    line = fgetl(fileID);
end

%% Solve part I

tic

zValues = zeros(1,zMax+1);




for i=0:zMax
    zValues(i+1) = logicGate(sprintf('z%02d',i),d);
end

result1 = 0;

%% Display results of part I
fprintf('%d pairs fit without overlapping.\n', result1);
toc

% %% Solve part II
% 
% tic
% 
% 
% 
% result2 = 0;
% 
% %% Display results of part II
% fprintf('Now, the sum of the complexities is %d.\n', result2);
% toc