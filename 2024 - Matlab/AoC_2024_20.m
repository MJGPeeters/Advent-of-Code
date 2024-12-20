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
        current = [i+1,tmp1+1];
    elseif ~isempty(tmp2)
        goal = [i+1,tmp2+1];
    end
end

% Padding
mapArray = ones(mapSize+2);
mapArray(2:mapSize+1,2:mapSize+1) = tmpArray;

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
out1 = sprintf('There are %d cheats that save at least one hundred ps.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

% %% Solve part II
% tic 
% 
% pathArray = AstarAllPaths(start,goal,mapArray);
% 
% solutionMap = ones(size(mapArray));
% solutionMap(mapArray==1) = 0;
% 
% imagesc(mapArray + 0.5*pathArray)
% colormap gray
% 
% result2 = 0;
% 
% time2 = toc;
% 
% %% Display results of part II
% out2 = sprintf('%d tiles are part of at least one of the best paths.', result2);
% tim2 = sprintf('Calculation took %f seconds.', time2);
% disp(out2)
% disp(tim2)