function regionMap = checkNeighborDirection(x,y,direction,regionMap,regionCount,array)

if direction==0
    x = x+1;
elseif direction==1
    y = y+1;
elseif direction==2
    x = x-1;
elseif direction==3
    y = y-1;
end

if array(x,y)==1 && regionMap(x,y)==0
    regionMap(x,y) = regionCount;
    for dir=0:3
        regionMap = checkNeighborDirection(x,y,direction,regionMap,regionCount,array);
    end
end

end