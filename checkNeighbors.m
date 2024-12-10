function [xOut,yOut,elevationOut] = checkNeighbors(xIn,yIn,elevationIn,mapArray)

inputSize = numel(xIn);
xOut = [];
yOut = [];
elevationOut = elevationIn+1;

for i=1:inputSize
    if mapArray(xIn(i)+1,yIn(i))==elevationOut
        xOut = [xOut xIn(i)+1];
        yOut = [yOut yIn(i)];
    end
    if mapArray(xIn(i)-1,yIn(i))==elevationOut
        xOut = [xOut xIn(i)-1];
        yOut = [yOut yIn(i)];
    end
    if mapArray(xIn(i),yIn(i)+1)==elevationOut
        xOut = [xOut xIn(i)];
        yOut = [yOut yIn(i)+1];
    end
    if mapArray(xIn(i),yIn(i)-1)==elevationOut
        xOut = [xOut xIn(i)];
        yOut = [yOut yIn(i)-1];
    end
end

end