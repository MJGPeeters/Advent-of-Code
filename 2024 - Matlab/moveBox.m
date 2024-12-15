function [spaceAvailable,boxArray] = moveBox(y,x,direction,wallArray,boxArray)

xCheck = x;
yCheck = y;

if direction==0
    yCheck = y-1;
elseif direction==1
    xCheck = x+1;
elseif direction==2
    yCheck = y+1;
else
    xCheck = x-1;
end

if wallArray(yCheck,xCheck)==1
    spaceAvailable = 0;
elseif boxArray(yCheck,xCheck)==0
    boxArray(yCheck,xCheck) = 1;
    boxArray(y,x) = 0;
    spaceAvailable = 1;
else
    [spaceAvailable,boxArray] = moveBox(yCheck,xCheck,direction,wallArray,boxArray);
    if spaceAvailable==1
        boxArray(yCheck,xCheck) = 1;
        boxArray(y,x) = 0;
    end
end

end