function [perimeter,area,regionMapOut] = checkPlants(x,y,plantType,perimeter,area,regionMap,plantMap)

if plantMap(x+1,y,plantType)==0
    perimeter = perimeter+1;
    regionMapOut = regionMap;
elseif regionMap(x+1,y)==0
    regionMap(x+1,y) = regionCount;
    regionMapOut = regionMap;
    area = area+1;
    [perimeter,area,regionMapOut] = checkPlants(x+1,y,plantType,perimeter,area,regionMapOut,plantMap);
else
    regionMapOut = regionMap;
end

end