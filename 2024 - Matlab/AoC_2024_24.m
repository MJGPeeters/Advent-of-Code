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

goalInputsX = strings(zMax+1,1);
goalInputsY = strings(zMax+1,1);

for i=0:zMax
    goalInputsX(i+1) = sprintf('x%02d',i);
    goalInputsY(i+1) = sprintf('y%02d',i);
end

% For every value of zXX (z00, z01, etc.)
for i=0:zMax
    zName = sprintf('z%02d',i);

    [inputs,outputs,~] = outputOrigins(d(zName),d,"","",999,0);
    inputs = sort(inputs);

    inputGoalLength = 2*(i+1);
    goalInputs = [goalInputsX(1:i+1);goalInputsY(1:i+1)];

    % Check if it's ok (check all the xXX and yXX inputs, see if they are all
    % there and the right amount)
    if numel(inputs)==inputGoalLength && all(goalInputs==inputs)
        continue
    end

    swapFlag = 0;

    for n=1:size(outputs,1)
        if swapFlag==1
            break
        end
        swapGatesN = d(outputs(n));

        for m=1:size(allOutputs,1)
            swapGatesM = d(allOutputs(m));

            % If not, swap one of the outputs related to zXX with another output
            dSwap = d;
            dSwap(outputs(n)) = swapGatesM;
            dSwap(allOutputs(m)) = swapGatesN;
            
            % Check if now the inputs are ok, for zXX and all the smaller zXX
            swapBool = 1;
    
            for j=0:i
                zNameSwap = sprintf('z%02d',j);
                
                tmpGoalLength = 2*(j+1);
                tmpGoalInputs = [goalInputsX(1:j+1);goalInputsY(1:j+1)];

                try
                    [inputsSwap,~,~] = outputOrigins(dSwap(zNameSwap),dSwap,"","",tmpGoalLength,0);
                    inputsSwap = sort(inputsSwap);
                catch
                    disp('test')
                end

                if numel(inputsSwap)~=tmpGoalLength || ~all(tmpGoalInputs==inputsSwap)
                    swapBool = 0;
                    break
                end
            end
            
            % If inputs are all ok, log the switch, and update the dictionary
            if swapBool
                disp('Swap!')
                swapList(2*swapCount-1) = outputs(n);
                swapList(2*swapCount)   = allOutputs(m);
                swapCount = swapCount+1;
                d = dSwap;
                swapFlag = 1;
                break
            end
        end
    end

    if swapCount==4
        break
    end    
end

result2 = join(sort(swapList),',');

%% Display results of part II
fprintf('%s.\n', result2);
toc