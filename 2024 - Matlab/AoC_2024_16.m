%% Preamble
adventDay = 16;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + "-2.txt";
    mapSize = 17;
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
    mapSize = 140;
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
        start = [tmp1;i;3];
    elseif ~isempty(tmp2)
        goal = [tmp2;i];
    end
end

%% Solve part I

path = Astar(start,goal,mapArray);
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

    % tmp = path(i);
    % pathArray(i,3) = mod(tmp,10);
    % 
    % tmp = (tmp - mod(tmp,10))/10;
    % pathArray(i,1) = mod(tmp,1000);
    % pathArray(i,2) = (tmp - mod(tmp,1000))/1000;
    % 
    % solutionMap(pathArray(i,1),pathArray(i,2)) = 0.7;
end

result1 = score;

time1 = toc;

%% Display results of part I
out1 = sprintf('The sum of all the GPS coordinates is %d.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
tic 

pathArray = AstarAllPaths(start,goal,mapArray);

result2 = sum(pathArray,'all');

time2 = toc;

%% Display results of part II
out2 = sprintf('%d tiles are part of at least one of the best paths.', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)