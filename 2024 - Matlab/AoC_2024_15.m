%% Preamble
adventDay = 15;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + "-3.txt";
    mapSize = 7;
    numMoves = 7;
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
    mapSize = 50;
    numMoves = 1000;
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
            x0 = startIndex;
            y0 = i;
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

startingBoxArray = boxArray;

%% Solve part I

x = x0;
y = y0;

for i=1:numel(moveArray)
    direction = moveArray(i);
    
    xCheck = x;
    yCheck = y;

    if direction==0
        yCheck = yCheck-1;
    elseif direction==1
        xCheck = xCheck+1;
    elseif direction==2
        yCheck = yCheck+1;
    else
        xCheck = xCheck-1;
    end

    if wallArray(yCheck,xCheck)==1
        continue
    elseif boxArray(yCheck,xCheck)==0
        x = xCheck;
        y = yCheck;
    else
        [spaceAvailable,boxArray] = moveBox(yCheck,xCheck,direction,wallArray,boxArray);
        if spaceAvailable==1
            x = xCheck;
            y = yCheck;
        else
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

boxArray = startingBoxArray;

boxWideArray  = zeros(mapSize,2*mapSize);
wallWideArray = zeros(mapSize,2*mapSize);

% Redo map
for i=1:mapSize
    boxWideArray(:,2*i-1) = boxArray(:,i);
    boxWideArray(:,2*i) = 2*boxArray(:,i);

    wallWideArray(:,2*i-1) = wallArray(:,i);
    wallWideArray(:,2*i) = wallArray(:,i);
end

x = 2*x0-1;
y = y0;

for i=1:numel(moveArray)
    direction = moveArray(i);
    
    xCheck = x;
    yCheck = y;

    if direction==0
        yCheck = yCheck-1;
    elseif direction==1
        xCheck = xCheck+1;
    elseif direction==2
        yCheck = yCheck+1;
    else
        xCheck = xCheck-1;
    end

    if wallWideArray(yCheck,xCheck)==1
        continue
    elseif boxWideArray(yCheck,xCheck)==0
        x = xCheck;
        y = yCheck;
    else
        [spaceAvailable,boxWideArray] = moveWideBox(yCheck,xCheck,direction,wallWideArray,boxWideArray);
        if spaceAvailable==1
            x = xCheck;
            y = yCheck;
        else
        end
    end
end

% Calculate GPS coordinates
hor2GPS = repmat(0:1:2*mapSize-1,mapSize,1);
ver2GPS = repmat((0:100:100*(mapSize-1))',1,2*mapSize);
coordinates2 = hor2GPS + ver2GPS;

result2 = sum((boxWideArray==1).*coordinates2,'all');

time2 = toc;

%% Display results of part II
out2 = sprintf('The new checksum is %d', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)