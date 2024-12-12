%% Preamble
adventDay = 12;
testBool = 1;

if testBool
    fileName = "Test_2024_" + adventDay + ".txt";
    mapSize = 10;
else
    fileName = "Input_2024_" + adventDay + ".txt"; 
    mapSize = 140;
end

%% Read data
tic

plantCell = cell(mapSize,1);
uniquePlants = [];

fileID = fopen(fileName);
for i=1:mapSize
    plantCell{i} = fgetl(fileID);
    uniquePlants = [uniquePlants unique(plantCell{i})];
end
fclose(fileID);

uniquePlants = unique(uniquePlants);


%% Solve part I

result1 = 0;

% For every plant type, make an array with all the plant locations (ones in
% an array of zeros)

tmpPlantMap = zeros(mapSize,mapSize,numel(uniquePlants));
plantMap = zeros(mapSize+2,mapSize+2,numel(uniquePlants));
price = 0;

for i=1%:numel(uniquePlants)
    for n=1:mapSize
        tmpPlantMap(n,plantCell{n}==uniquePlants(i),i) = 1;
    end

    % Add padding
    plantMap(2:end-1,2:end-1,i) = tmpPlantMap(:,:,i);

    regionMap = zeros(mapSize+2);
    regionCount = 0;

    % % Find different regions, keep track of perimeter
    % while nnz(plantMap(:,:,i))>nnz(regionMap)
    %     regionCount = regionCount+1;
    % 
    %     perimeter = 0;
    %     area = 0;
    % 
    %     % Recursively go through region, update regionArray
    %     [x,y] = find(plantMap(:,:,i)==1,1);
    %     x = 6;
    %     y = 5;
    %     regionMap(x,y) = regionCount;
    %     area = area+1;
    % 
    %     [perimeterOut,areaOut,regionMapOut] = checkPlants(x,y,i,perimeter,area,regionMap,plantMap);
    count = 0;
    for direction=0:3
        count = count + checkNeighborPlant(x,y,i,direction,plantMap,count);
    end









        % plantMap(x-1,y,i)==1
        % plantMap(x,y+1,i)==1
        % plantMap(x,y-1,i)==1

        % price = price + area*perimeter;
    % end



    % Determine price for every region, add to running tally


end

result1 = price;

% Within this array, find the different regions. 
% - Start with the first plant, mark it as region 1 in a specific array. Go 
% through all of the neighbors of that plant. If they are not the same 
% plant, ignore. If they are the same plant and are already designated as 
% being in the same region, ignore. If they are the same plant and are not 
% yet designated a region, mark them in the same region and continue with 
% them. For every cell, every neighbor that does not belong to the region
% adds 1 to the perimeter of that region (including edges). 
% - Then check if there are plants of the same type that are not in the
% region. If so, continue same procedure as above. 

% For every region, determine area and perimeter, and multiply to get the
% price. Add price to running tally.
% - Area is simply the number of cells in that region
% - Perimeter is calculated during determination of the regions. 

time1 = toc;

%% Display results of part I
out1 = sprintf('The total price of the fencing over all regions is %d.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

% %% Solve part II
% tic
% 
% result2 = 0;
% 
% time2 = toc;
% 
% %% Display results of part II
% out2 = sprintf('After seventy-five blinks you will have %d stones.', result2);
% tim2 = sprintf('Calculation took %f seconds.', time2);
% disp(out2)
% disp(tim2)