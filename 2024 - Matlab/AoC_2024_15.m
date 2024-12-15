%% Preamble
adventDay = 15;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + "-2.txt";
    mapSize = 10;
    numMoves = 70;
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
    mapSize = 50;
end

%% Read data
tic

importMap = importdata(fileName);
wallArray = zeros(mapSize);
boxArray  = zeros(mapSize);
moveArray = [];

for i=1:numel(importMap)
    if i<=mapSize
        boxArray(i,importMap{i}=='O')  = 1;
        wallArray(i,importMap{i}=='#') = 1;
        
        startIndex = find(importMap{i}=='@');

        if startIndex
            x = startIndex;
            y = i;
        end
    else
        tmp = zeros(1,numMoves);
        tmp(importMap{i}=='^') = 0;
        tmp(importMap{i}=='>') = 1;
        tmp(importMap{i}=='v') = 2;        
        tmp(importMap{i}=='<') = 3; 
        moveArray = [moveArray tmp];
    end
end

%% Solve part I

for i=1:numel(moveArray)
    direction = moveArray(i);
    
    xCheck = x;
    yCheck = y;

    if direction==0
        yCheck = yCheck-1;
        firstWallIndex = find(wallArray(1:y,x)==1,1,'last') + 1;
        emptySpace = find(boxArray(yCheck:-1:firstWallIndex,x)==0,1);
        xEmpty = x;
        yEmpty = y - emptySpace;
    elseif direction==1
        xCheck = xCheck+1;
        firstWallIndex = x + find(wallArray(y,xCheck:end)==1,1,'first') - 1;
        emptySpace = find(boxArray(y,xCheck:firstWallIndex)==0,1);
        xEmpty = x + emptySpace;
        yEmpty = y;
    elseif direction==2
        yCheck = yCheck+1;
        firstWallIndex = y + find(wallArray(yCheck:end,x)==1,1,'first') - 1;
        emptySpace = find(boxArray(yCheck:firstWallIndex,x)==0,1);
        xEmpty = x;
        yEmpty = y + emptySpace;
    else
        xCheck = xCheck-1;
        firstWallIndex = find(wallArray(y,1:x)==1,1,'last') + 1;
        emptySpace = find(boxArray(y,xCheck:-1:firstWallIndex)==0,1);
        xEmpty = x - emptySpace;
        yEmpty = y;    
    end

    if wallArray(yCheck,xCheck)==1
        continue
    elseif boxArray(yCheck,xCheck)==0
        x = xCheck;
        y = yCheck;
    else
        if isempty(emptySpace)
            continue
        else
            boxArray(yCheck,xCheck) = 0;
            boxArray(yEmpty,xEmpty) = 1;
            x = xCheck;
            y = yCheck;
        end
    end
end

% Calculate GPS coordinates
horGPS = repmat(0:1:mapSize-1,mapSize,1);
verGPS = repmat((0:100:100*(mapSize-1))',1,mapSize);
coordinates = horGPS + verGPS;

result1 = sum(boxArray.*coordinates,'all');

time1 = toc;

%% Display results of part I
out1 = sprintf('The sum of all the GPS coordinates is %d.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
tic 

% Only difference wrt part I is when you want to move up or down and a box
% is in the way. Now probably need recursive method, first to check all
% boxes if there is a wall in the way. If there is no wall in the way, mark
% all the boxes that will be pushed. When moving, move all the marked boxes
% one step up or down, and move yourself as well. 

result2 = 0;

time2 = toc;

%% Display results of part II
out2 = sprintf('The new checksum is %d', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)