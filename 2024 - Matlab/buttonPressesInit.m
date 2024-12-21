function dict = buttonPressesInit(array)

dict = dictionary;

for startIndex=1:numel(array)
    for goalIndex=1:numel(array)
        % Check if either start or end is not a valid entry
        if array(startIndex)==-1 || array(goalIndex)==-1
            continue
        end
        
        % Convert index to row and column value for array
        [rs,cs] = ind2sub(size(array),startIndex);
        [rg,cg] = ind2sub(size(array),goalIndex);
        
        dr = rg - rs;
        dc = cg - cs;

        if dr>0
            rowDir = 2;
        else
            rowDir = 8;
        end

        % Find best path. If goal column is higher than (or the same as)
        % start column, first go to correct column, then to correct row. 
        % Otherwise, the other way around. 

        % If the numDict is used, use this priority
        if numel(array)>25
            if dc<=0 && array(rs,cs+dc)~=-1
                route = [repmat(4,[1,abs(dc)]), repmat(rowDir,[1,abs(dr)])];
            elseif dc<=0
                route = [repmat(rowDir,[1,abs(dr)]), repmat(4,[1,abs(dc)])];
            elseif array(rs+dr,cs)~=-1
                route = [repmat(rowDir,[1,abs(dr)]), repmat(6,[1,abs(dc)])];
            else
                route = [repmat(6,[1,abs(dc)]), repmat(rowDir,[1,abs(dr)])];
            end
        % Else use the other priority
        else
            if dc>=0
                route = [repmat(6,[1,abs(dc)]), repmat(rowDir,[1,abs(dr)])];
            else
                route = [repmat(rowDir,[1,abs(dr)]), repmat(4,[1,abs(dc)])];
            end
        end
        
        % Store route in dictionary
        dict(10*array(startIndex)+array(goalIndex)) = {route};
    end
end

end