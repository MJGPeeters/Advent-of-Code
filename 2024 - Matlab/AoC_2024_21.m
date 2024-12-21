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

time1 = toc;

%% Display results of part I
fprintf('The sum of the complexities is %d.\n', result1);
fprintf('Calculation took %f seconds.\n', time1);

% %% Solve part II
% 
% tic
% 
% result1 = 0;
% 
% time1 = toc;
% 
% %% Display results of part II
% fprintf('With the new rules, there are %d cheats that save at least 50 ps.\n', result1);
% fprintf('Calculation took %f seconds.\n', time1);