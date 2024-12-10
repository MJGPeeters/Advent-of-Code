%% Preamble
adventDay = 10;
testBool = 0;

if testBool
    fileName = "Test_2024_" + adventDay + ".txt";
    mapSize = 8;
else
    fileName = "Input_2024_" + adventDay + ".txt"; 
    mapSize = 45;
end

%% Read data
tic

mapArray = -1*ones(mapSize+2);

fileID = fopen(fileName);

for i=2:mapSize+1
    mapLine = fgetl(fileID);
    mapArray(i,2:mapSize+1) = sscanf(mapLine,'%1d')';
end

fclose(fileID);

%% Solve part I
[x0,y0] = find(mapArray==0);
result1 = 0;

% Go through all the zeros (beginnings of trailheads)
for i=1:numel(x0)
    xPos = x0(i);
    yPos = y0(i);
    elevation = 0;

    trailEndArray = zeros(mapSize+2);

    xIn = xPos;
    yIn = yPos;
    elevationIn = elevation;
    
    % Check all the possible routes that start at the trailhead
    while elevationIn<9
        [xOut,yOut,elevationOut] = checkNeighbors(xIn,yIn,elevationIn,mapArray);

        if isempty(xOut)
            break
        end

        xIn = xOut;
        yIn = yOut;
        elevationIn = elevationOut;
    end
    
    % Mark all the trail ends that can be visited it in trailEndArray
    for j=1:numel(xOut)
        trailEndArray(xOut(j),yOut(j)) = 1;
    end
    
    % After all trails at the trailhead have been searched, update result1
    result1 = result1 + sum(trailEndArray,'all');
end

time1 = toc;

%% Display results of part I
out1 = sprintf('The sum of all scores of the trailheads is %d.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
[x0,y0] = find(mapArray==0);
result2 = 0;

tic

% Go through all the zeros (beginnings of trailheads)
for i=1:numel(x0)
    xPos = x0(i);
    yPos = y0(i);
    elevation = 0;

    trailEndArray = zeros(mapSize+2);

    xIn = xPos;
    yIn = yPos;
    elevationIn = elevation;
    
    % Check all the possible routes that start at the trailhead
    while elevationIn<9
        [xOut,yOut,elevationOut] = checkNeighbors(xIn,yIn,elevationIn,mapArray);

        if isempty(xOut)
            break
        end

        xIn = xOut;
        yIn = yOut;
        elevationIn = elevationOut;
    end
    
    % After all trails at the trailhead have been searched, update result2
    result2 = result2 + numel(xOut); 
end

time2 = toc;

%% Display results of part II
out2 = sprintf('The new checksum is %d', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)