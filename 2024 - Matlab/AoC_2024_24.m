%% Preamble
adventDay = 24;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
    zMax = 12;
    lineIndex = 11;
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
    zMax = 45;
    lineIndex = 91;
end

%% Read data
fileID = fopen(fileName);
line = fgetl(fileID);

d = dictionary;

i = 1;

while isempty(line) || all(line~=-1)
    if i<lineIndex
        tmp = strsplit(line,':');
        d(string(tmp{1})) = {double(string(tmp{2}))};
    elseif i>lineIndex
        tmp = strsplit(line);
        d(string(tmp{end})) = {{tmp{1}, tmp{2}, tmp{3}}};
    end

    i = i+1;
    line = fgetl(fileID);
end

%% Solve part I

tic

zValues = zeros(2,zMax+1);

for i=0:zMax
    tmp = logicGate(d(sprintf('z%02d',i)),d);
    zValues(1,i+1) = tmp{1};
    zValues(2,i+1) = 2^i;
end

result1 = sum(prod(zValues,1));

%% Display results of part I
fprintf('The decimal output is %d.\n', result1);
toc

%% Solve part II

tic
swapString = [];

for i=0:zMax
    % For every z-value (z00, z01 etc.)

    % Find the complete logic tree
    [tmp,treeOutputs] = logicGateOrigin(d(sprintf('z%02d',i)),d,'',"");

    % Check if it is the right length
    if i==1
        lengthGoal = 3;
    elseif i==2
        lengthGoal = 7;
    else
        lengthGoal = 15 + 8*(i-3);
    end

    % If not, start swapping inputs (only the ones that are part of this
    % logic tree) until it is the right length   
    flag = 1;

    if numel(tmp)~=lengthGoal
        for n=1:numel(treeOutputs)
            if flag==0
                break
            end
            for m=1:numel(allOutputs)
                % Swap two inputs
                tmpGate = d(treeOutputs(n));
                d(treeOutputs(n)) = d(allOutputs(m));
                d(allOutputs(m))  = tmpGate;

                % Find new complete logic tree
                [stringOutput,treeOutputs] = logicGateOrigin(d(sprintf('z%02d',i)),d,'',"");
        
                % Check length
                if numel(stringOutput)==lengthGoal
                    % If a good swap is found, log the two inputs that are swapped
                    swapString = [swapString;treeOutputs(n);allOutputs(m)];
                    flag = 0;
                    break
                end
            end
        end
    end
    
    %% Possible pitfalls/improvements
    % Now it is assumed that there is only one swap for every z-value. If
    % after going through all the swaps no valid solution is found, two
    % swaps might be tried.

    % Not it is assumed that only checking the length is enough. Maybe more
    % is needed, such as checking if all lower values are incorporated





    % tmp = logicGateOrigin(d(sprintf('z%02d',i)),d,'');
    % tmp(tmp=="") = [];
    % cells{i+1} = tmp;
    % 
    % correct = 1;
    % 
    % for n=0:i-1
    %     if ~any(tmp==sprintf('x%02d',n))
    %         correct = 0;
    %         break
    %     end
    % end
    % 
    % if correct==0
    %     disp(i)
    % end
end

result2 = 0;

%% Display results of part II
fprintf('Now, the sum of the complexities is %d.\n', result2);
toc