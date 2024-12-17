%% Preamble
adventDay = 16;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + "-2.txt";
    mapSize = 17;
%     numMoves = 7;
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
    mapSize = 140;
%     numMoves = 1000;
end

%% Read data
tic

importMap = importdata(fileName);
mapArray = zeros(mapSize);

for i=1:numel(importMap)
    mapArray(i,importMap{i}=='#') = 1;
    
    tmp1 = find(importMap{i}=='S');
    tmp2 = find(importMap{i}=='E');

    if ~isempty(tmp1)
        start = [i;tmp1;3];
    elseif ~isempty(tmp2)
        goal = [i;tmp2];
    end
end

goal = [2;139];

%% Solve part I

% Option: Use a regular pathfinding algorithm (probably Dijkstra). When
% saving the score for every cell, also save the direction from which the
% reindeer came. Can do that e.g. by saving the score for a cell as 
%   x = 100*dir + xCoordinate, y = 100*dir + yCoordinate,
% with dir = {0,1,2,3}, such that mod(x or y,100) equals the actual 
% coordinate, from the remainder you can see the direction. 
% - Not sure if this will actually work

% Option: Use a regular pathfinding algorithm, but start from the end. 
% - Don't think this matters, it's the exact same problem as the regular
%   version

% Option: Check all possibilities, as in all possible path between start 
% and end. Not sure how you actually make sure that you get all 
% possibilities, but this way you are sure to find the shortest path. 

% Option: Make changing direction a specific step in the algorithm. So your
% list of steps is not just a list of coordinates you visited, but also
% takes into account the direction you are facing at that moment. 
% - This seems like the most viable option. Maybe store it as a 3D grid,
%   with direction as the third dimension? 

[path,f,g] = Astar(start,goal,mapArray);
pathArray = zeros(numel(path),2);

solutionMap = ones(size(mapArray));
solutionMap(mapArray==1) = 0;

score = -1;
pos = 0;

test = numel(path);

for i=1:numel(path)
    posPrev = pos;
    pos = (path(i) - mod(path(i),10))/10;

    if pos==posPrev
        score = score+1000;
    else
        score = score+1;
    end

    tmp = path(i);
    pathArray(i,3) = mod(tmp,10);

    tmp = (tmp - mod(tmp,10))/10;
    pathArray(i,1) = mod(tmp,1000);
    pathArray(i,2) = (tmp - mod(tmp,1000))/1000;

    solutionMap(pathArray(i,1),pathArray(i,2)) = 0.7;
end



imshow(solutionMap)

%% TO DO

% Make Part I return the correct answer

% Optimize speed for Part I, use profiler to see what takes so long

% Solve Part II

result1 = score;

time1 = toc;

%% Display results of part I
out1 = sprintf('The sum of all the GPS coordinates is %d.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
tic 

% in Astar function, do something when tentativeGScore equals the gScore of
% the neighbor. That means that a path is found with the same score, so
% another best path. Maybe just change < to =, and save a list of all the
% visited squares instead of a dict (the order is not important now). Maybe
% just keep a map-like array with all zeros, and mark with ones the squares
% that are visited. At the end, sum all the ones. Or even simply keep a
% counter of the number of visited squares. Then double-counting is a risk.

result2 = 0;

time2 = toc;

%% Display results of part II
out2 = sprintf('%d tiles are part of at least one of the best paths.', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)