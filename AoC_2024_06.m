%% Preamble
testFileName  = "Test_2024_06.txt";
inputFileName = "Input_2024_06.txt";

testMapSize  = 10;
inputMapSize = 130;

% Change between test and input
fileName = inputFileName;
mapSize  = inputMapSize;

%% Read data
fileID = fopen(fileName,'rt');

% Initialize cell array zeros everywhere, including padding
guardMapOriginal = cell(mapSize+2,mapSize+2);
guardMapOriginal(cellfun(@isempty,guardMapOriginal)) = {0};

% Read map
for i=2:mapSize+1
    row = fgetl(fileID);
    for j=1:numel(row)
        guardMapOriginal{i,j+1} = row(j);
    end
end

fclose(fileID);

%% Solve part I
tic
guardMap = guardMapOriginal;

% Find starting location
[xPos,yPos] = find(strcmp(guardMap,'^'));

while 1
    % Check if the guard is out of bounds
    if guardMap{xPos,yPos}==0
        break
    end

    % Check if there is an obstacle in front of the guard
    if guardMap{xPos-1,yPos}=='#'
        guardMap = rot90(guardMap,1);

        xTmp = xPos;
        xPos = mapSize+3 - yPos;
        yPos = xTmp;

        continue
    else
        guardMap{xPos,yPos} = 'X';
        xPos = xPos-1;
    end
end

% Count up all the visited squares
result1 = sum(strcmp(guardMap,'X'),'all');

time1 = toc;

%% Display results of part I
out1 = sprintf('The guard will visit %d distinct positions.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
tic

result2 = 0;
guardMap = guardMapOriginal;
guardMapArrayOriginal = zeros(length(guardMap));
[xPos0,yPos0] = find(strcmp(guardMap,'^'));

for i=1:size(guardMap,1)
    for j=1:size(guardMap,2)
        if guardMap{i,j}=='#'
            guardMapArrayOriginal(i,j) = 9;
        elseif guardMap{i,j}==0
            guardMapArrayOriginal(i,j) = 0;
        elseif guardMap{i,j}=='^'
            guardMapArrayOriginal(i,j) = 3;
        else
            guardMapArrayOriginal(i,j) = 1;
        end
    end
end

for i=2:mapSize+1
    for j=2:mapSize+1
        xPos = xPos0;
        yPos = yPos0;

        path = zeros(150*150*10,1);
        direction = 0;

        guardMapArray = guardMapArrayOriginal;
        
        if guardMapArray(i,j)~=9 && guardMapArray(i,j)~=3
            guardMapArray(i,j) = 9;
        end

        while 1
            % Check if the guard is in a loop
            if path(150*10*xPos + 10*yPos + direction)==1
                result2 = result2+1;
                break
            end

            % Check if the guard is out of bounds
            if guardMapArray(xPos,yPos)==0
                break
            end
        
            if direction==0
                if guardMapArray(xPos-1,yPos)==9
                    path(150*10*xPos + 10*yPos + direction) = 1;
                    direction = 1;
                    continue
                else
                    path(150*10*xPos + 10*yPos + direction) = 1;
                    guardMapArray(xPos,yPos) = 2;
                    xPos = xPos-1;
                end
            elseif direction==1
                if guardMapArray(xPos,yPos+1)==9
                    path(150*10*xPos + 10*yPos + direction) = 1;
                    direction = 2;
                    continue
                else
                    path(150*10*xPos + 10*yPos + direction) = 1;
                    guardMapArray(xPos,yPos) = 2;
                    yPos = yPos+1;
                end
            elseif direction==2
                if guardMapArray(xPos+1,yPos)==9
                    path(150*10*xPos + 10*yPos + direction) = 1;
                    direction = 3;
                    continue
                else
                    path(150*10*xPos + 10*yPos + direction) = 1;
                    guardMapArray(xPos,yPos) = 2;
                    xPos = xPos+1;
                end
            else
                if guardMapArray(xPos,yPos-1)==9
                    path(150*10*xPos + 10*yPos + direction) = 1;
                    direction = 0;
                    continue
                else
                    path(150*10*xPos + 10*yPos + direction) = 1;
                    guardMapArray(xPos,yPos) = 2;
                    yPos = yPos-1;
                end
            end
        end
    end
end
time2 = toc;

%% Display results of part II
out2 = sprintf('There are %d possible positions for the obstacle.', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)