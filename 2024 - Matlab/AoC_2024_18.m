%% Preamble
adventDay = 18;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
    numBytes = 12;
    numBytesTotal = 25;
    mapSize = 7;
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
    numBytes = 1024;
    numBytesTotal = 3450;
    mapSize = 71;
end

%% Read data
tic

mapArray = zeros(mapSize,mapSize,numBytesTotal);
obstacles = zeros(numBytesTotal,2);

fileID = fopen(fileName);
for i=1:numBytesTotal
    tmp = fgetl(fileID);
    coordinateCell = split(tmp,',')';
    obstacleCol = double(string(coordinateCell{1}))+1;
    obstacleRow = double(string(coordinateCell{2}))+1;
    obstacles(i,:) = [obstacleCol-1, obstacleRow-1];

    mapArray(obstacleRow,obstacleCol,i:numBytesTotal) = 1;
end
fclose(fileID);

% Insert padding
mapPadding = ones(mapSize+2,mapSize+2,numBytesTotal);
mapPadding(2:mapSize+1,2:mapSize+1,:) = mapArray;

%% Solve part I

start = [2; 2];
goal  = [mapSize+1; mapSize+1];

path = AstarReg(start,goal,mapPadding(:,:,numBytes));

result1 = numel(path)-1;

time1 = toc;

%% Display results of part I
out1 = sprintf('The minimum number of steps is %d.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
tic 

numBytes = numBytesTotal+1;
path = [];

while isempty(path)
    numBytes = numBytes-1;
    start = [2; 2];
    goal  = [mapSize+1; mapSize+1];
    mapArray = mapPadding(:,:,numBytes);
    path = AstarReg(start,goal,mapArray);
end

result2 = sprintf('%d,%d',obstacles(numBytes+1,1),obstacles(numBytes+1,2));

time2 = toc;

%% Display results of part II
out2 = sprintf('The coordinates of the first byte that blocks the exit are %s', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)