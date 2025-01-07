%% Preamble
clear all
adventDay = 21;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
end

%% Read data
importCodes = importdata(fileName);

%% Solve part I

tic

% Initialize keypads
numPad = [-1,-1,-1,-1,-1;
    -1,7,8,9,-1;
    -1,4,5,6,-1;
    -1,1,2,3,-1;
    -1,-1,0,100,-1;
    -1,-1,-1,-1,-1];
dirPad = [-1,-1,-1,-1,-1;
    -1,-1,8,100,-1;
    -1,4,2,6,-1;
    -1,-1,-1,-1,-1];

% Find how to get from one place to another in the fastest way for both the
% numeric keypad and the directional keypad
numDict = buttonPressesInit(numPad);
dirDict = buttonPressesInit(dirPad);

complexity = 0;
numRobots = 2;
for n=1:numel(importCodes)
    code = importCodes{n};
    code = '029A';

    for i=1:numel(code)
        if code(i)=='A' codeArray(i) = 100; else codeArray(i) = double(string(code(i))); end 
    end

    presses = buttonPresses(codeArray,numDict);

    for i=1:numRobots
        presses = buttonPresses(presses,dirDict);
    end
       
    complexity = complexity + length(presses)*double(string(code(1:end-1)));
end

result1 = complexity;

%% Display results of part I
fprintf('The sum of the complexities is %d.\n', result1);
toc

%% Solve part II

% Initialize keypads
numPad = string([-1,-1,-1,-1,-1;
    -1,7,8,9,-1;
    -1,4,5,6,-1;
    -1,1,2,3,-1;
    -1,-1,0,"A",-1;
    -1,-1,-1,-1,-1]);
dirPad = string([-1,-1,-1,-1,-1;
    -1,-1,"^","A",-1;
    -1,"<","v",">",-1;
    -1,-1,-1,-1,-1]);

% Find how to get from one place to another in the fastest way for both the
% numeric keypad and the directional keypad
numDictString = buttonPressesInitString(numPad);
dirDictString = buttonPressesInitString(dirPad);

tic

complexity = 0;
numRobots = 3;

for n=1:numel(importCodes)
    code = char(['A',importCodes{n}]);
    code = '029A';

    pressesString = buttonPressesString(code,numDictString);

    % Divide into groups of movement between subsequent A presses. E.g.
    % >>A - ^A - A - >A - A - >A - <A
    AIndices = [0,find(pressesString=='A')];
    numGroups = numel(AIndices)-1;
    groupArray = strings(1,numGroups);

    for i=1:numGroups
        groupArray(i) = join(pressesString(AIndices(i)+1:AIndices(i+1)),"");
    end

    % For every unique group of movements, go one level (robot) deeper, and
    % see what presses are needed there. Keep track of the count.
    newGroupArray = strings(size(groupArray));
    newGroupArraySplit = [];

    for i=1:numel(groupArray)
        newGroupArray(i) = buttonPressesString(char(groupArray(i)),dirDictString);
        
        tmp = buttonPressesString(char(groupArray(i)),dirDictString);
        AIndices = [0,find(tmp=='A')];
        numGroups = numel(AIndices)-1;

        for j=1:numGroups
            newGroupArraySplit = [newGroupArraySplit, string(join(tmp(AIndices(j)+1:AIndices(j+1)),""))];
        end
    end

    [a,b] = findgroups(newGroupArraySplit);
    countArray = histcounts(a);



    for j=1:numRobots
        presses = buttonPresses(presses,dirDict);
    end
       
    complexity = complexity + sum(presses(2,:))*double(string(code(1:end-1)));
end

result2 = complexity;

%% Display results of part II
fprintf('Now, the sum of the complexities is %d.\n', result2);
toc