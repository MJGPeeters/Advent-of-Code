%% Preamble
adventDay = 25;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
end

%% Read data
% fileID = fopen(fileName);
% 
% line = fgetl(fileID);
% 
% while line~=-1
% 
% 
% end

importData = importdata(fileName);
numElements = length(importData);

lockArray = [];
keyArray = [];

for i=1:7:numElements
    tmpTotal = zeros(1,5);
    for j=1:5
        tmp = importData{i+j};
        tmpTotal = tmpTotal + double(tmp=='#');
    end
    
    if importData{i}(1)=='#'
        lockArray = [lockArray; tmpTotal];
    else
        keyArray = [keyArray; tmpTotal];
    end
end

%% Solve part I

tic

numLocks = size(lockArray,1);
numKeys  = size(keyArray,1);

possiblePairs = 0;

for i=1:numKeys
    testKeys = repmat(keyArray(i,:),numLocks,1);
    test = lockArray + testKeys;

    tmp = test<6;
    tmp2 = all(tmp==1,2);
    possiblePairs = possiblePairs + sum(tmp2);
end

%% Display results of part I
fprintf('%d pairs fit without overlapping.\n', possiblePairs);
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