% function [perimeter,area,regionMapOut] = checkPlants(x,y,plantType,perimeter,area,regionMap,plantMap)
% 
% if plantMap(x+1,y,plantType)==0
%     perimeter = perimeter+1;
%     regionMapOut = regionMap;
% elseif regionMap(x+1,y)==0
%     regionMap(x+1,y) = regionCount;
%     regionMapOut = regionMap;
%     area = area+1;
%     [perimeter,area,regionMapOut] = checkPlants(x+1,y,plantType,perimeter,area,regionMapOut,plantMap);
% else
%     regionMapOut = regionMap;
% end
% 
% end

function [area,perimeter,regionMap] = checkNeighborPlant(x,y,plantType,direction,plantMap,regionMap,area,perimeter,regionCount)

% global REGIONMAP

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