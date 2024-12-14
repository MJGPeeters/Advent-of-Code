function [area,pUp,pDown,pLeft,pRight,regionMap] = checkNeighborPlantII(x,y,plantType,direction,plantMap,regionMap,area,pUp,pDown,pLeft,pRight,regionCount)

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
    if direction==0
        pRight(x-1,y) = 1;
    elseif direction==1
        pDown(x,y-1) = 1;
    elseif direction==2
        pLeft(x+1,y) = 1;
    elseif direction==3
        pUp(x,y+1) = 1;
    end
elseif regionMap(x,y)==0
    regionMap(x,y) = regionCount;
    area = area+1;
    for dir=0:3
        [area,pUp,pDown,pLeft,pRight,regionMap] = checkNeighborPlantII(x,y,plantType,dir,plantMap,regionMap,area,pUp,pDown,pLeft,pRight,regionCount);
    end
end

end