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

swapList = "";
swapCount = 1;

goalInputsX = "x00";
goalInputsY = "y00";

for i=1:zMax
    goalInputsX = [goalInputsX;sprintf('x%02d',i);sprintf('x%02d',i)];
    goalInputsY = [goalInputsY;sprintf('y%02d',i);sprintf('y%02d',i)];
end

correctOutputs = ["z00";"z01"];

% For every value of zXX (z00, z01, etc.)
for i=2:zMax
    zName = sprintf('z%02d',i);

    [inputs,outputs,~] = outputOrigins(d(zName),d,"","",999,0);
    inputs = sort(inputs);
    if isempty(outputs)
        outputs = string(zName);
    else
        outputs = [outputs;string(zName)];
    end

    inputGoalLength = 4*i;
    goalInputs = [goalInputsX(1:2*i);goalInputsY(1:2*i)];

    % Check if it's ok (check all the xXX and yXX inputs, see if they are all
    % there and the right amount)
    if numel(inputs)==inputGoalLength && all(goalInputs==inputs)
        correctOutputs = [correctOutputs;outputs(1:6);string(zName)];
        continue
    end

    swapFlag = 0;

    for n=1:size(outputs,1)
        if swapFlag==1
            break
        end
        swapGatesN = d(outputs(n));

        if contains(correctOutputs,outputs(n))
            continue
        end

        for m=1:size(allOutputs,1)
            swapGatesM = d(allOutputs(m));

            if contains(correctOutputs,allOutputs(m))
                continue
            end

            % If not, swap one of the outputs related to zXX with another output
            dSwap = d;
            dSwap(outputs(n)) = swapGatesM;
            dSwap(allOutputs(m)) = swapGatesN;
            
            % Check if now the inputs are ok, for zXX and all the smaller zXX
            [inputsSwap,outputsSwap,~] = outputOrigins(dSwap(zName),dSwap,"","",inputGoalLength,0);
            inputsSwap = sort(inputsSwap);
            
            % If inputs are all ok, log the switch, and update the dictionary
            if numel(inputsSwap)==inputGoalLength && all(goalInputs==inputsSwap)
                disp('Swap!')
                swapList(2*swapCount-1) = outputs(n);
                swapList(2*swapCount) = allOutputs(m);
                swapCount = swapCount+1;
                d = dSwap;
                swapFlag = 1;
                correctOutputs = [correctOutputs;outputsSwap(1:6);string(zName);outputs(n);allOutputs(m)];
                % break
            end
        end
    end

    if swapCount==5
        break
    end    
end

result2 = join(sort(swapList),',');

%% Display results of part II
fprintf('%s.\n', result2);
toc