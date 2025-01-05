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

allOutputs = [];
i = 1;

while isempty(line) || all(line~=-1)
    if i<lineIndex
        tmp = strsplit(line,':');
        d(string(tmp{1})) = {double(string(tmp{2}))};
    elseif i>lineIndex
        tmp = strsplit(line);
        d(string(tmp{end})) = {{tmp{1}, tmp{2}, tmp{3}}};
        allOutputs = [allOutputs; tmp{end}];
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

compareInputs = ["x00";"y00"];
for i=1:zMax
    compareInputs = [compareInputs;sprintf('x%02d',i);sprintf('y%02d',i)];
end

for i=0:zMax
    if numel(swapString)==8
        break
    end
    % For every z-value (z00, z01 etc.)
    
    % Find the complete logic tree
    [tmp,treeOutputs,~] = logicGateOrigin(d(sprintf('z%02d',i)),d,'',"", "");

    % Check if it is the right length
    lengthGoal = 3 + 4*i;

    % If not, start swapping inputs (only the ones that are part of this
    % logic tree) until it is the right length   
    flag = 1;

    if numel(tmp)~=lengthGoal
        for n=1:numel(treeOutputs)
            tmp1 = d(treeOutputs(n));

            if flag==0 
                break
            end
            for m=1:size(allOutputs,1)

                tmpDict = d;

                % Swap two inputs
                tmp2 = tmpDict(allOutputs(m,:));

                tmpDict(treeOutputs(n)) = tmp2;
                tmpDict(allOutputs(m,:)) = tmp1;

                % Find new complete logic tree
                [stringOutput,tmpTreeOutputs,tmpInputsAll] = logicGateOrigin(d(sprintf('z%02d',i)),tmpDict,'',"","");
                
                tmpInputsAll = sort(tmpInputsAll(2:end));
                tmpInputsX = tmpInputsAll(1:end/2);
                tmpInputsY = tmpInputsAll(end/2+1:end);

                numInputs = numel(tmpInputsX);

                tmpInputs = strings(2*numInputs,1);
                for k=1:numInputs
                    tmpInputs(2*k-1) = tmpInputsX(k);
                    tmpInputs(2*k)   = tmpInputsY(k);
                end

                % Check length
                if numel(stringOutput)==lengthGoal && all(tmpInputs==compareInputs(1:2*(i+1)))
                    previousFlag = 1;
                    for p=0:i
                        [pStringOutput,~,pInputs] = logicGateOrigin(d(sprintf('z%02d',p)),tmpDict,'',"", "");
                        pInputs = sort(pInputs(2:end));
                        pInputsX = pInputs(1:end/2);
                        pInputsY = pInputs(end/2+1:end);
        
                        numInputs = numel(pInputsX);
        
                        tmpInputs = strings(2*numInputs,1);
                        for k=1:numInputs
                            tmpInputs(2*k-1) = pInputsX(k);
                            tmpInputs(2*k)   = pInputsY(k);
                        end

                        if numel(pStringOutput)~=lengthGoal || ~all(tmpInputs==compareInputs(1:2*(p+1)))
                            previousFlag = 0;
                            break
                        end
                    end

                    if previousFlag==1
                        % If a good swap is found, log the two inputs that are swapped
                        swapString = [swapString;tmpTreeOutputs(n);allOutputs(m,:)];
                        disp(swapString)
                        d = tmpDict;
                        flag = 0;
                        break
                    end
                end
            end
        end
    end

    %% Possible pitfalls/improvements
    % Now it is assumed that there is only one swap for every z-value. If
    % after going through all the swaps no valid solution is found, two
    % swaps might be tried.
end

result2 = join(sort(swapString),',');

%% Display results of part II
fprintf('%s.\n', result2);
toc

for i=0:zMax
    % Find the complete logic tree
    [tmp,treeOutputs,~] = logicGateOrigin(d(sprintf('z%02d',i)),d,'',"","");

    cells{i+1} = tmp;

    % Check if it is the right length
    lengthGoal = 3 + 4*i;

    if numel(tmp)~=lengthGoal
        disp(i)
    end
end
