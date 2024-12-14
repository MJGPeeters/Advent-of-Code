%% Preamble
adventDay = 8;
testBool = 0;

if testBool
    fileName = "Test_2024_" + adventDay + ".txt";
else
    fileName = "Input_2024_" + adventDay + ".txt"; 
end

%% Read data

% Make cell array with every cell a regular array with the locations of the
% antennas for one specific frequency. 

tmp = importdata(fileName);
mapSize = length(tmp);

els = '';

% Find unique characters in the map, remove '.'
for i=1:mapSize
    els = [els unique(tmp{i})]; %#ok<AGROW> 
end

els = unique(els);
numFrequencies = numel(els)-1;
mapCell = {};

for i=1:numFrequencies
    mapCell{i} = zeros(mapSize); %#ok<SAGROW> 
    for j=1:mapSize
        mapCell{i}(j,:) = tmp{j}==els(i+1);
    end
end

%% Solve part I
tic 

antinodeArray = zeros(mapSize);

% For every frequency, go through all the pairs of antennas
for i=1:numFrequencies
    [xList,yList] = find(mapCell{i}==1);
    numAntennas = numel(xList);

    for n=1:numAntennas
        for m=1:n-1
            dx = xList(m)-xList(n);
            dy = yList(m)-yList(n);

            antinodePos = [xList(n)-dx yList(n)-dy];
            antinodeNeg = [xList(m)+dx yList(m)+dy];

            if antinodePos(1)>0 && antinodePos(1)<mapSize+1 && antinodePos(2)>0 && antinodePos(2)<mapSize+1
                antinodeArray(antinodePos(1),antinodePos(2)) = 1;
            end

            if antinodeNeg(1)>0 && antinodeNeg(1)<mapSize+1 && antinodeNeg(2)>0 && antinodeNeg(2)<mapSize+1
                antinodeArray(antinodeNeg(1),antinodeNeg(2)) = 1;
            end            
        end
    end

end

result1 = sum(antinodeArray,'all');

time1 = toc;

%% Display results of part I
out1 = sprintf('There are %d unique locations that contain an antinode.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
tic 

antinodeArray = zeros(mapSize);

% For every frequency, go through all the pairs of antennas
for i=1:numFrequencies
    [xList,yList] = find(mapCell{i}==1);
    numAntennas = numel(xList);

    for n=1:numAntennas
        for m=1:n-1
            dx = xList(m)-xList(n);
            dy = yList(m)-yList(n);

            antinodePos = [xList(n)+dx yList(n)+dy];
            antinodeNeg = [xList(n)-dx yList(n)-dy];

            antinodeArray(xList(n),yList(n)) = 1;

            while antinodePos(1)>0 && antinodePos(1)<mapSize+1 && antinodePos(2)>0 && antinodePos(2)<mapSize+1
                antinodeArray(antinodePos(1),antinodePos(2)) = 1;
                antinodePos = [antinodePos(1)+dx antinodePos(2)+dy];
            end

            while antinodeNeg(1)>0 && antinodeNeg(1)<mapSize+1 && antinodeNeg(2)>0 && antinodeNeg(2)<mapSize+1
                antinodeArray(antinodeNeg(1),antinodeNeg(2)) = 1;
                antinodeNeg = [antinodeNeg(1)-dx antinodeNeg(2)-dy];
            end            
        end
    end

end

result2 = sum(antinodeArray,'all');

time2 = toc;

% Display results of part II
out2 = sprintf('Including harmonics, there are %d unique locations that contain an antinode.', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)