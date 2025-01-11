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

tic

% Find how to get from one place to another in the fastest way for both the
% numeric keypad and the directional keypad
numDict = button_presses_initialization(numPad);
dirDict = button_presses_initialization(dirPad);

numRobots = 2;
complexity = 0;
    
for n=1:numel(importCodes)
    code = string(importCodes{n});

    [presses,counts] = button_presses(code,1,numDict);

    for i=1:numRobots
        [presses,counts] = button_presses(presses,counts,dirDict);
    end

    numPresses = strlength(presses)*counts;
    code = char(code);

    complexity = complexity + numPresses*double(string(code(1:end-1)));
end

result1 = complexity;

%% Display results of part I
fprintf('The sum of the complexities is %d.\n', result1);
toc

%% Solve part II

tic

minComplexity = 10^15;
numRobots = 25;

for d=0:15
    tmpDirDict = dirDict;
    k = ["vA","Av","^>",">^"];
    p = [">^A","^>A";
        "v<A","<vA";
        ">vA","v>A";
        "^<A","<^A"];

    num = dec2bin(d,4);

    for j=1:4
        tmpDirDict(k(j)) = p(j,double(string(num(j)))+1);
    end

    complexity = 0;

    for n=1:numel(importCodes)
        code = string(importCodes{n});

        [presses,counts] = button_presses(code,1,numDict);

        for i=1:numRobots
            [presses,counts] = button_presses(presses,counts,tmpDirDict);
        end

        numPresses = strlength(presses)*counts;
        code = char(code);

        complexity = complexity + numPresses*double(string(code(1:end-1)));
    end

    if complexity<=minComplexity
        minComplexity = complexity;
    end
end

result2 = minComplexity;

%% Display results of part I
fprintf('The sum of the complexities is %d.\n', result2);
toc