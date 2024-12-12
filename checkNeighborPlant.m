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

function count = checkNeighborPlant(x,y,i,direction,plantMap,count)

if direction==0
    x = x+1;
elseif direction==1
    y = y+1;
elseif direction==2
    x = x-1;
elseif direction==3
    y = y-1;
end

if plantMap(x,y,i)==1
    for dir=0:3
        count = count + checkNeighborPlant(x,y,i,dir,plantMap,count);
    end
end

end