function [area,perimeter,regionMap] = checkNeighborPlant(x,y,plantType,direction,plantMap,regionMap,area,perimeter,regionCount)

if direction==0
    x = x+1;
elseif direction==1
    y = y+1;
elseif direction==2
    x = x-1;
elseif direction==3
    y = y-1;
end

if plantMap(x,y,plantType)==0
    perimeter = perimeter+1;
elseif regionMap(x,y)==0
    regionMap(x,y) = regionCount;
    area = area+1;
    for dir=0:3
        [area,perimeter,regionMap] = checkNeighborPlant(x,y,plantType,dir,plantMap,regionMap,area,perimeter,regionCount);
    end
end

end