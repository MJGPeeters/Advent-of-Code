%% Preamble
adventDay = 12;
testBool = 0;

if testBool
    fileName = "Test_2024_" + adventDay + "-2.txt";
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

tmpPlantMap = zeros(mapSize,mapSize,numel(uniquePlants));
plantMap = zeros(mapSize+2,mapSize+2,numel(uniquePlants));
price = 0;

for i=1:numel(uniquePlants)
    for n=1:mapSize
        tmpPlantMap(n,plantCell{n}==uniquePlants(i),i) = 1;
    end

    % Add padding
    plantMap(2:end-1,2:end-1,i) = tmpPlantMap(:,:,i);

    regionMap = zeros(mapSize+2);
    regionCount = 0;

    while nnz(plantMap(:,:,i))>nnz(regionMap)
        regionCount = regionCount+1;

        area = 1;
        perimeter = 0;
        [x,y] = find((plantMap(:,:,i)==1).*(regionMap==0),1);

        regionMap(x,y) = regionCount;
    
        for direction=0:3
            [area,perimeter,regionMap] = checkNeighborPlant(x,y,i,direction,plantMap,regionMap,area,perimeter,regionCount);
        end
        
        price = price + area*perimeter;
    end
end

result1 = price;

time1 = toc;

%% Display results of part I
out1 = sprintf('The total price of the fencing over all regions is %d.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
tic

tmpPlantMap = zeros(mapSize,mapSize,numel(uniquePlants));
plantMap = zeros(mapSize+2,mapSize+2,numel(uniquePlants));
price = 0;

for i=1:numel(uniquePlants)
    for n=1:mapSize
        tmpPlantMap(n,plantCell{n}==uniquePlants(i),i) = 1;
    end

    % Add padding
    plantMap(2:end-1,2:end-1,i) = tmpPlantMap(:,:,i);

    regionMap = zeros(mapSize+2);
    regionCount = 0;

    while nnz(plantMap(:,:,i))>nnz(regionMap)
        regionCount = regionCount+1;

        area   = 1;
        pUp    = zeros(mapSize+2);
        pDown  = zeros(mapSize+2);
        pLeft  = zeros(mapSize+2);
        pRight = zeros(mapSize+2);

        [x,y] = find((plantMap(:,:,i)==1).*(regionMap==0),1);

        regionMap(x,y) = regionCount;
    
        for direction=0:3
            [area,pUp,pDown,pLeft,pRight,regionMap] = checkNeighborPlantII(x,y,i,direction,plantMap,regionMap,area,pUp,pDown,pLeft,pRight,regionCount);
        end
        
        sidesU = findRegions(pUp);
        sidesD = findRegions(pDown);
        sidesL = findRegions(pLeft);
        sidesR = findRegions(pRight);

        sides = sidesU + sidesD + sidesL + sidesR;
        
        price = price + area*sides;
    end
end

result2 = price;

time2 = toc;

%% Display results of part II
out2 = sprintf('The new total price of the fencing over all regions is %d.', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)