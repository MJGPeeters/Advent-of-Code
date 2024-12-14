function out = importDataArray(fileLoc, arraySize)

fileID=fopen(fileLoc,'rt');
formatSpec='%d';

out = NaN(arraySize);

for i=1:arraySize(1)
    tmp = str2double(strsplit(fgetl(fileID)));
    out(i,1:numel(tmp)) = tmp;
end

end