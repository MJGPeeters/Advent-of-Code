function out = moveElement(startIndex, endIndex, array)

if startIndex==endIndex
    out = array;
elseif startIndex<endIndex
    out = [array(1:startIndex-1), array(startIndex+1:endIndex), array(startIndex), array(endIndex+1:end)];
else
    error('endIndex cannot be smaller than startIndex')
end

end