%% Preamble
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

    for i=1:numel(code)
        if code(i)=='A' codeArray(i) = 100; else codeArray(i) = double(string(code(i))); end %#ok<SEPEX>
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

tic

complexity = 0;
numRobots = 3;

for n=1:numel(importCodes)
    code = ['A',importCodes{n}];

    for i=1:numel(code)
        if code(i)=='A' codeArray(i) = 100; else codeArray(i) = double(string(code(i))); end %#ok<SEPEX>
    end

    presses = [100,buttonPresses(codeArray,numDict)];
    
    % Go from individual presses to movement between two subsequent presses
    tmpPresses = ones(2,numel(presses)-1);
    for i=1:numel(presses)-1
        start = presses(i);
        goal  = presses(i+1);

        tmpPresses(1,i) = 10*start+goal;
    end

    % Count unique instances of movements
    for i=length(tmpPresses):-1:1
        idxs = find(tmpPresses(1,:)==tmpPresses(1,i));
        tmpPresses(2,idxs(1)) = tmpPresses(2,idxs(1)) + numel(idxs)-1;
        if numel(idxs)>1
            tmpPresses(:,idxs(end)) = [];
        end
    end

    presses = tmpPresses;

    presses = buttonPressesFast(presses,dirDict);


    for i=1:numRobots
        presses = buttonPresses(presses,dirDict);
    end
       
    complexity = complexity + sum(presses(2,:))*double(string(code(1:end-1)));
end

result2 = complexity;

%% Display results of part II
fprintf('Now, the sum of the complexities is %d.\n', result2);
toc