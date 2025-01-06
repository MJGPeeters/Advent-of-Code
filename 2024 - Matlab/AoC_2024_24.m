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

allOutputs = strings(222,1);
i = 1;
ind = 1;

while isempty(line) || all(line~=-1)
    if i<lineIndex
        tmp = strsplit(line,':');
        d(string(tmp{1})) = {double(string(tmp{2}))};
    elseif i>lineIndex
        tmp = strsplit(line);
        d(string(tmp{end})) = {{tmp{1}, tmp{2}, tmp{3}}};
        allOutputs(ind) = tmp{end};
        ind = ind+1;
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
switchableOutputs = allOutputs;
swapList = [];

carry = 'z45';

for z=44:-1:2
    [checkCarry,gates] = check_full_adder(z,d,carry);

    swapFlag = 0;
    
    % If it is the right FA, this part works, and the outputs in this gate can 
    % be removed from the list of all switchable outputs. 
    if isscalar(checkCarry)
        for n=numel(gates):-1:1
            if swapFlag==1
                break
            end

            swapGatesN = d(gates(n));
            outputN = gates(n);
            for m=1:numel(switchableOutputs)
                swapGatesM = d(switchableOutputs(m));

                dSwap = d;
                dSwap(outputN) = swapGatesM;
                dSwap(switchableOutputs(m)) = swapGatesN;

                [checkCarry,gates] = check_full_adder(z,dSwap,carry);

                if ~isscalar(checkCarry)
                    d = dSwap;
                    swapList = [swapList;outputN;switchableOutputs(m)];
                    swapFlag = 1;
                    break
                end
            end
        end
    end

    for i=1:numel(gates)
        switchableOutputs(switchableOutputs==gates(i)) = [];
    end

    carry = checkCarry;
end

result2 = join(sort(swapList),',');

%% Display results of part II
fprintf('The list of wires is %s.\n', result2);
toc