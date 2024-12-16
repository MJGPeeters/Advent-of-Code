%% Preamble
adventDay = 16;
testBool = 1;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + "-1.txt";
    mapSize = 15;
%     numMoves = 7;
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
%     mapSize = 50;
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
        start = [i;tmp1;2];
    elseif ~isempty(tmp2)
        goal = [i;tmp2];
    end
end

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

path = Astar(start,goal,mapArray);
pathArray = zeros(numel(path),2);

solutionMap = mapArray;

% for i=1:numel(path)
%     pathArray(i,1) = mod(path(i),100);
%     pathArray(i,2) = (path(i) - mod(path(i),100))/100;
% 
%     solutionMap(pathArray(i,2),pathArray(i,1)) = 2;
% end





result1 = 0;

time1 = toc;

%% Display results of part I
out1 = sprintf('The sum of all the GPS coordinates is %d.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

% %% Solve part II
% tic 
% 
% boxArray = startingBoxArray;
% 
% boxWideArray  = zeros(mapSize,2*mapSize);
% wallWideArray = zeros(mapSize,2*mapSize);
% 
% % Redo map
% for i=1:mapSize
%     boxWideArray(:,2*i-1) = boxArray(:,i);
%     boxWideArray(:,2*i) = 2*boxArray(:,i);
% 
%     wallWideArray(:,2*i-1) = wallArray(:,i);
%     wallWideArray(:,2*i) = wallArray(:,i);
% end
% 
% x = 2*x0-1;
% y = y0;
% 
% for i=1:numel(moveArray)
%     direction = moveArray(i);
%     
%     xCheck = x;
%     yCheck = y;
% 
%     if direction==0
%         yCheck = yCheck-1;
%     elseif direction==1
%         xCheck = xCheck+1;
%     elseif direction==2
%         yCheck = yCheck+1;
%     else
%         xCheck = xCheck-1;
%     end
% 
%     if wallWideArray(yCheck,xCheck)==1
%         continue
%     elseif boxWideArray(yCheck,xCheck)==0
%         x = xCheck;
%         y = yCheck;
%     else
%         [spaceAvailable,boxWideArray] = moveWideBox(yCheck,xCheck,direction,wallWideArray,boxWideArray);
%         if spaceAvailable==1
%             x = xCheck;
%             y = yCheck;
%         else
%         end
%     end
% end
% 
% % Calculate GPS coordinates
% hor2GPS = repmat(0:1:2*mapSize-1,mapSize,1);
% ver2GPS = repmat((0:100:100*(mapSize-1))',1,2*mapSize);
% coordinates2 = hor2GPS + ver2GPS;
% 
% result2 = sum((boxWideArray==1).*coordinates2,'all');
% 
% time2 = toc;
% 
% %% Display results of part II
% out2 = sprintf('The new checksum is %d', result2);
% tim2 = sprintf('Calculation took %f seconds.', time2);
% disp(out2)
% disp(tim2)