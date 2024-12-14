%% Read data
testData = importdata("Test_2024_03.txt");
inputData = importdata("Input_2024_03.txt");

%% Solve part I
result1 = 0;

inputString = [];

for n=1:size(inputData,1)
    inputString = [inputString inputData{n}];
end

% Find all instances of 'mul(' in the large string. 
indArray = strfind(inputString,'mul(')';
indArray = [indArray, zeros(1,numel(indArray))'];

numOptions = length(indArray);

% For every instance of 'mul(', find the first subsequent instance of ')'.
for i=1:numOptions
    tmp = indArray(i)-1 + strfind(inputString(indArray(i):end),')');

    if isempty(tmp)
        indArray(i,:) = [];
        numOptions = numOptions - 1;
    end

    indArray(i,2) = tmp(1);
end

% For the elements between 'mul(' and ')', check if there is exactly one
% comma. If so, look at parts left and right of comma. 
for i=1:numOptions
    commas = indArray(i,1)-1 + strfind(inputString(indArray(i,1):indArray(i,2)),',');
    if numel(commas)==1
        tmp1 = double(string(inputString(indArray(i,1)+4:commas-1)));
        tmp2 = double(string(inputString(commas+1:indArray(i,2)-1)));

        if (tmp1>0 && tmp1<1000) && (tmp2>0 && tmp2<1000)
            result1 = result1 + tmp1*tmp2;
        end
    end
end

%% Display results of part I
out1 = sprintf('The sum of all multiplications is %d.', result1);
disp(out1)

%% Solve part II

result2 = 0;
inputString = [];

for n=1:size(inputData,1)
    inputString = [inputString inputData{n}];
end

% Find all instances of 'mul(' in the large string. 
indArray = strfind(inputString,'mul(')';
indArray = [indArray, zeros(1,numel(indArray))'];

% Start with all ones, meaning all elements are active
activeArray = ones(numel(inputString),1);

% Find locations of all do() and don't() instructions
doInd = strfind(inputString,'do()');
dontInd = strfind(inputString,"don't()");

x = 1;

while 1
    if x<=numel(dontInd)
        tmpDont = dontInd(x);
    else
        break
    end

    tmpDo = doInd(find(doInd>tmpDont,1));

    if isempty(tmpDo)
        activeArray(tmpDont:end) = 0;
        break
    else
        activeArray(tmpDont:tmpDo) = 0;
        x = x+1;
    end
end

% Check all 'mul(' elements, if they are a passive element, ignore them
for i=length(indArray):-1:1
    if activeArray(indArray(i,1))==0
        indArray(i,:) = [];
    end
end

numOptions = length(indArray);

% For every instance of 'mul(', find the first subsequent instance of ')'.
for i=1:numOptions
    tmp = indArray(i)-1 + strfind(inputString(indArray(i):end),')');

    if isempty(tmp)
        indArray(i,:) = [];
        numOptions = numOptions - 1;
    end

    indArray(i,2) = tmp(1);
end

% For the elements between 'mul(' and ')', check if there is exactly one
% comma. If so, look at parts left and right of the comma. 
for i=1:numOptions
    commas = indArray(i,1)-1 + strfind(inputString(indArray(i,1):indArray(i,2)),',');
    if numel(commas)==1
        tmp1 = double(string(inputString(indArray(i,1)+4:commas-1)));
        tmp2 = double(string(inputString(commas+1:indArray(i,2)-1)));

        if (tmp1>0 && tmp1<1000) && (tmp2>0 && tmp2<1000)
            result2 = result2 + tmp1*tmp2;
        end
    end
end

%% Display results of part II
out2 = sprintf('The sum of all multiplications with new instructions is %d.', result2);
disp(out2)