function [spaceAvailable,boxArray] = moveWideBox(y,x,direction,wallArray,boxArray)

if direction==0
    if boxArray(y,x)==2
        x = x-1;
    end

    if wallArray(y-1,x)==1 || wallArray(y-1,x+1)==1
        spaceAvailable = 0;
    elseif boxArray(y-1,x)==0 && boxArray(y-1,x+1)==0
        spaceAvailable = 1;
    elseif boxArray(y-1,x)==1
        [spaceAvailable,boxArray] = moveWideBox(y-1,x,direction,wallArray,boxArray);
    elseif boxArray(y-1,x)==2 && boxArray(y-1,x+1)==0
        [spaceAvailable,boxArray] = moveWideBox(y-1,x-1,direction,wallArray,boxArray);
    elseif boxArray(y-1,x)==0 && boxArray(y-1,x+1)==1
        [spaceAvailable,boxArray] = moveWideBox(y-1,x+1,direction,wallArray,boxArray);
    elseif boxArray(y-1,x)==2 && boxArray(y-1,x+1)==1
        boxArraySave = boxArray;
        [spaceAvailable,boxArray] = moveWideBox(y-1,x-1,direction,wallArray,boxArray);
        if spaceAvailable
            [spaceAvailable,boxArray] = moveWideBox(y-1,x+1,direction,wallArray,boxArray);
        end
        if ~spaceAvailable
            boxArray = boxArraySave;
        end
    end
    % If there is space, move the box
    if spaceAvailable==1
        boxArray(y-1,x:x+1) = [1 2];
        boxArray(y,x:x+1) = [0 0];
    end  
    
elseif direction==1
    if wallArray(y,x+2)==1
        spaceAvailable = 0;
    elseif boxArray(y,x+2)==0
        spaceAvailable = 1;
        boxArray(y,x:x+2) = [0 1 2];
    else
        [spaceAvailable,boxArray] = moveWideBox(y,x+2,direction,wallArray,boxArray);
        if spaceAvailable==1
            boxArray(y,x:x+2) = [0 1 2];
        end
    end

elseif direction==2
    if boxArray(y,x)==2
        x = x-1;
    end

    if wallArray(y+1,x)==1 || wallArray(y+1,x+1)==1
        spaceAvailable = 0;
    elseif boxArray(y+1,x)==0 && boxArray(y+1,x+1)==0
        spaceAvailable = 1;
    elseif boxArray(y+1,x)==1
        [spaceAvailable,boxArray] = moveWideBox(y+1,x,direction,wallArray,boxArray);
    elseif boxArray(y+1,x)==2 && boxArray(y+1,x+1)==0
        [spaceAvailable,boxArray] = moveWideBox(y+1,x-1,direction,wallArray,boxArray);
    elseif boxArray(y+1,x)==0 && boxArray(y+1,x+1)==1
        [spaceAvailable,boxArray] = moveWideBox(y+1,x+1,direction,wallArray,boxArray);
    elseif boxArray(y+1,x)==2 && boxArray(y+1,x+1)==1
        boxArraySave = boxArray;
        [spaceAvailable,boxArray] = moveWideBox(y+1,x-1,direction,wallArray,boxArray);
        if spaceAvailable
            [spaceAvailable,boxArray] = moveWideBox(y+1,x+1,direction,wallArray,boxArray);
        end
        if ~spaceAvailable
            boxArray = boxArraySave;
        end
    end
    % If there is space, move the box
    if spaceAvailable==1
        boxArray(y+1,x:x+1) = [1 2];
        boxArray(y,x:x+1) = [0 0];
    end  

else
    if wallArray(y,x-2)==1
        spaceAvailable = 0;
    elseif boxArray(y,x-2)==0
        spaceAvailable = 1;
        boxArray(y,x-2:x) = [1 2 0];
    else
        [spaceAvailable,boxArray] = moveWideBox(y,x-2,direction,wallArray,boxArray);
        if spaceAvailable==1
            boxArray(y,x-2:x) = [1 2 0];
        end
    end
end

end