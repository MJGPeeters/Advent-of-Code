%% Preamble
testFileName  = "Test_2024_05.txt";
inputFileName = "Input_2024_05.txt";

fileName     = inputFileName;
numRules     = 1176;
startUpdates = numRules+2;
endUpdates   = 1377;

%% Read data
fileID = fopen(fileName,'rt');

% Rules
rules = zeros(numRules,2);

for i=1:numRules
    tmp = split(fgetl(fileID),'|');
    rules(i,:) = [str2double(tmp{1}),str2double(tmp{2})];
end

% Updates
updates = cell(endUpdates-startUpdates+1,1);
n = 1;

while 1
    tmp = fgetl(fileID);
    if tmp==-1
        break
    elseif ~isempty(tmp)
        tmp = str2double(split(tmp,','))';
        updates{n} = tmp;
        n = n+1;
    end
end

fclose(fileID);

%% Solve part I
result1 = 0;

ruleArray = zeros(length(rules));

for i=1:length(rules)
    if any(ruleArray(:,1)==rules(i,1))
        tmpIndex = find(ruleArray(:,1)==rules(i,1));
        tmpNumRules = nnz(ruleArray(tmpIndex,:));
        ruleArray(tmpIndex,tmpNumRules+1) = rules(i,2);
    else
        tmpIndex = find(ruleArray(:,1)==0,1);
        ruleArray(tmpIndex,1) = rules(i,1);
        ruleArray(tmpIndex,2) = rules(i,2);
    end
end

d = dictionary;

for i=1:nnz(ruleArray(:,1))
    d{ruleArray(i,1)} = ruleArray(i,2:nnz(ruleArray(i,:)~=0));
end

k = 1;
incorrectUpdates = {};

for i=1:numel(updates)
    valid = 1;

    for j=1:numel(updates{i})
        tmp = updates{i}(j);
        if isKey(d,tmp)
            for n=1:j-1
                if any(updates{i}(n)==cell2mat(d(updates{i}(j))))
                    valid = 0;
                end
            end
        end
    end

    % If the update is valid, find the middle number, add to running tally
    if valid==1
        result1 = result1 + updates{i}(ceil(numel(updates{i})/2));
    else
        incorrectUpdates{k} = updates{i};
        k = k+1;
    end
end

%% Display results of part I
out1 = sprintf('The total sum is %d.', result1);
disp(out1)

%% Solve part II
result2 = 0;

for i=1:numel(incorrectUpdates)
    sortedUpdate = incorrectUpdates{i};
    changes = 1;

    while changes>0
        changes = 0;
        for j=1:numel(sortedUpdate)
            tmp = sortedUpdate(j);
            if isKey(d,tmp)
                for n=j-1:-1:1
                    if any(sortedUpdate(n)==cell2mat(d(tmp)))
                        sortedUpdate = moveElement(n,j,sortedUpdate);
                        changes = changes+1;
                    end
                end
            end
        end
    end
    result2 = result2 + sortedUpdate(ceil(numel(sortedUpdate)/2));
end

%% Display results of part II
out2 = sprintf('The total sum for the resorted updates is %d.', result2);
disp(out2)