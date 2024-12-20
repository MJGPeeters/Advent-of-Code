%% Preamble
adventDay = 20;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
    mapSize = 15;
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
    mapSize = 141;
end

%% Read data
importMap = importdata(fileName);
tmpArray = zeros(mapSize);

for i=1:numel(importMap)
    tmpArray(i,importMap{i}=='#') = 1;
    
    tmp1 = find(importMap{i}=='S');
    tmp2 = find(importMap{i}=='E');

    if ~isempty(tmp1)
        current = [i+20,tmp1+20];
    elseif ~isempty(tmp2)
        goal = [i+20,tmp2+20];
    end
end

% Padding
mapArray = ones(mapSize+40);
mapArray(21:mapSize+20,21:mapSize+20) = tmpArray;

%% Solve part I

tic

minTimeSave = 100;
timeSaves = 0;
diff = [1,0;-1,0;0,1;0,-1];

[timeArray,route] = racetrackLength(current,goal,mapArray);

% For every step along the route, check all four directions for possible
% cheats. If a cheat is possible, determine time saved due to cheat. 
for i=1:size(route,2)
    if timeArray(route(1,i),route(2,i))<=minTimeSave
        break
    end
    
    for j=1:4
        timeSave = 0;
        pos  = [route(1,i),route(2,i)];
        pos1 = [pos(1)+diff(j,1),pos(2)+diff(j,2)];
        pos2 = [pos1(1)+diff(j,1),pos1(2)+diff(j,2)];

        if mapArray(pos1(1),pos1(2))==1 && mapArray(pos2(1),pos2(2))==0
            timeSave = timeArray(pos(1),pos(2)) - timeArray(pos2(1),pos2(2)) - 2;
        end

        if timeSave>=minTimeSave
            timeSaves = timeSaves+1;
        end
    end
end

result1 = timeSaves;

time1 = toc;

%% Display results of part I
fprintf('There are %d cheats that save at least 100 ps.\n', result1);
fprintf('Calculation took %f seconds.\n', time1);

%% Solve part II

tic

minTimeSave = 100;
timeSaves = 0;

% List of all possible cheats with length of at most 20
diff = zeros(2,841);
n = 1;

for i=-20:20
    for j=-20:20
        if abs(i)+abs(j)<=20
            diff(1,n) = i;
            diff(2,n) = j;
            n = n+1;
        end
    end
end

% For every step along the route, check all possible cheats. If a cheat is 
% possible, determine time saved due to cheat. 
for i=1:size(route,2)
    if timeArray(route(1,i),route(2,i))<minTimeSave
        break
    end
    
    for j=1:length(diff)
        timeSave = 0;
        pos  = [route(1,i),route(2,i)];
        posEnd = [pos(1)+diff(1,j),pos(2)+diff(2,j)];

        if mapArray(posEnd(1),posEnd(2))==0
            timeSave = timeArray(pos(1),pos(2)) - timeArray(posEnd(1),posEnd(2)) - sum(abs(diff(:,j)));
        end

        if timeSave>=minTimeSave
            timeSaves = timeSaves+1;
        end
    end
end

result1 = timeSaves;

time1 = toc;

%% Display results of part I
fprintf('With the new rules, there are %d cheats that save at least 50 ps.\n', result1);
fprintf('Calculation took %f seconds.\n', time1);