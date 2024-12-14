function numRegions = findRegions(array)

numRegions = 0;
regionMap = zeros(size(array));

while nnz(array)>nnz(regionMap)
    numRegions = numRegions+1;

    [x,y] = find((array==1).*(regionMap==0),1);

    regionMap(x,y) = numRegions;

    for direction=0:3
        regionMap = checkNeighborDirection(x,y,direction,regionMap,numRegions,array);
    end
end

end