%% Preamble
adventDay = 14;
testBool = 0;

if testBool
    fileName = "Test_2024_" + adventDay + ".txt";
    numRobots = 12;
    xMapSize = 7;
    yMapSize = 11;
else
    fileName = "Input_2024_" + adventDay + ".txt"; 
    numRobots = 500;
    xMapSize = 103;
    yMapSize = 101;
end

%% Solve part I
tic

endTime = 100;

xMidPoint = floor(xMapSize/2);
yMidPoint = floor(yMapSize/2);
quadrant = zeros(4,1);

fileID = fopen(fileName);

for i=1:numRobots
    line = fgetl(fileID);
    tmp = sscanf(line,'p=%d,%d v=%d,%d');
    y0 = tmp(1);
    x0 = tmp(2);
    vy = tmp(3);
    vx = tmp(4);

    xPos = mod(x0+endTime*vx,xMapSize);
    yPos = mod(y0+endTime*vy,yMapSize);

    if xPos<xMidPoint && yPos<yMidPoint
        quadrant(1) = quadrant(1)+1;
    elseif xPos<xMidPoint && yPos>yMidPoint
        quadrant(2) = quadrant(2)+1;
    elseif xPos>xMidPoint && yPos<yMidPoint
        quadrant(3) = quadrant(3)+1;
    elseif xPos>xMidPoint && yPos>yMidPoint
        quadrant(4) = quadrant(4)+1;
    end

end

fclose(fileID);

result1 = quadrant(1)*quadrant(2)*quadrant(3)*quadrant(4);

time1 = toc;

%% Display results of part I
out1 = sprintf('The safety factor is %d.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
tic

endTime = 100;
x0 = zeros(numRobots,1);
y0 = zeros(numRobots,1);
vx = zeros(numRobots,1);
vy = zeros(numRobots,1);

% Read initial positions and speeds from input
fileID = fopen(fileName);
for i=1:numRobots
    line = fgetl(fileID);
    tmp = sscanf(line,'p=%d,%d v=%d,%d');
    y0(i) = tmp(1);
    x0(i) = tmp(2);
    vy(i) = tmp(3);
    vx(i) = tmp(4);
end
fclose(fileID);

% For every time step, save a picture of the locations of the robots
t = 0;
while 1
    t = t+1;
    mapArray = zeros(xMapSize,yMapSize);

    xPos = mod(x0+t*vx,xMapSize)+1;
    yPos = mod(y0+t*vy,yMapSize)+1;

    linIndex = sub2ind([xMapSize,yMapSize],xPos,yPos);
    mapArray(linIndex) = mapArray(linIndex)+1;
    
    flippedMapArray = flip(mapArray,2);

    if sum(mapArray.*flippedMapArray,'all')>100
        imagesc(mapArray)
        break
    end
end

result2 = t;

time2 = toc;

%% Display results of part I
out2 = sprintf('The christmas tree appears after %d seconds.', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)