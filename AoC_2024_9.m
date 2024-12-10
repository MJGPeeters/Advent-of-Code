%% Preamble
adventDay = 9;
testBool = 0;

if testBool
    fileName = "Test_2024_" + adventDay + ".txt";
else
    fileName = "Input_2024_" + adventDay + ".txt"; 
end

%% Read data
tic
fileID = fopen(fileName);
fileString = fgetl(fileID);
fclose(fileID);

fileID = 0;
index = 1;

originalFile = zeros(1e5,1);
diskSpaces = sscanf(fileString,'%1d');
fileDict = dictionary;
freeDict = dictionary;
indexFileDict = dictionary;
indexFreeDict = dictionary;

for i=1:numel(fileString)
    diskSpace = diskSpaces(i);

    if mod(i,2)==1
        originalFile(index:index+diskSpace-1) = fileID;
        fileDict(fileID) = diskSpace;
        indexFileDict(fileID) = index;
        fileID = fileID+1;
    else
        originalFile(index:index+diskSpace) = NaN;
        freeDict(fileID) = diskSpace;
        indexFreeDict(fileID) = index;
    end

    index = index+diskSpace;
end

arrayIndex = find(originalFile(10:end)==0,1);
originalFile = originalFile(1:arrayIndex+8);

%% Solve part I
leftIndex = 1;
rightIndex = numel(originalFile);
compactFile = zeros(numel(originalFile),1);

while leftIndex<(rightIndex+1)
    if isnan(originalFile(leftIndex))
        compactFile(leftIndex) = originalFile(rightIndex);
        rightIndex = rightIndex-12 + find(~isnan(originalFile(rightIndex-11:rightIndex-1)),1,'last');
    else
        compactFile(leftIndex) = originalFile(leftIndex);
    end
    leftIndex = leftIndex+1;
end

arrayIndex = find(compactFile(10:end)==0,1);
compactFile = compactFile(1:arrayIndex+8);

result1 = (0:numel(compactFile)-1)*compactFile;

time1 = toc;

%% Display results of part I
out1 = sprintf('The resulting checksum is %d.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
tic 

maxFileID = fileID-1;
compactFile = zeros(numel(originalFile),1);

for fileID=maxFileID:-1:0
    fileSize = fileDict(fileID);
    movedBool = 0;

    for freeID=1:fileID
        if freeDict(freeID) >= fileSize
            compactFile(indexFreeDict(freeID):indexFreeDict(freeID)+fileSize-1) = fileID;
            movedBool = 1;

            freeDict(freeID) = freeDict(freeID)-fileSize;
            indexFreeDict(freeID) = indexFreeDict(freeID)+fileSize;
            break
        end
    end

    if movedBool==0
        compactFile(indexFileDict(fileID):indexFileDict(fileID)+fileSize-1) = fileID;
    end
end

result2 = (0:numel(compactFile)-1)*compactFile;

time2 = toc;

%% Display results of part II
out2 = sprintf('The new checksum is %d', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)