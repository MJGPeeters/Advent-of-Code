function pathArray = reconstructAllPaths(originDict,current,pathArray)

while isKey(originDict,current)
    current = originDict(current);
    current = current{1};

    if numel(current)>1
        for i=1:numel(current)
            pathArray = reconstructAllPaths(originDict,current(i),pathArray);
        end
    else 
        tmp = (current - mod(current,10))/10;
        tmp1 = mod(tmp,1000);
        tmp2 = (tmp - mod(tmp,1000))/1000;

        pathArray(tmp1,tmp2) = 1;
    end
end

end