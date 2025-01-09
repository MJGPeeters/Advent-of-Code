function dict = button_presses_initialization(array)

dict = dictionary;

for startIndex=1:numel(array)
    for goalIndex=1:numel(array)
        % Check if either start or end is not a valid entry
        if array(startIndex)=="-1" || array(goalIndex)=="-1"
            continue
        end
        
        % Convert index to row and column value for array
        [rs,cs] = ind2sub(size(array),startIndex);
        [rg,cg] = ind2sub(size(array),goalIndex);
        
        dr = rg - rs;
        dc = cg - cs;

        if dr>0
            rowDir = "v";
        else
            rowDir = "^";
        end

        % Find best path. If goal column is higher than (or the same as)
        % start column, first go to correct column, then to correct row. 
        % Otherwise, the other way around. 

        % If the numDict is used, use this priority
        if numel(array)>25
            if dc<=0 && array(rs,cs+dc)~="-1"
                route = join([repmat("<",[1,abs(dc)]),repmat(rowDir,[1,abs(dr)]),"A"],"");
            elseif dc<=0
                route = join([repmat(rowDir,[1,abs(dr)]),repmat("<",[1,abs(dc)]),"A"],"");
            elseif array(rs+dr,cs)~="-1"
                route = join([repmat(rowDir,[1,abs(dr)]),repmat(">",[1,abs(dc)]),"A"],"");
            else
                route = join([repmat(">",[1,abs(dc)]),repmat(rowDir,[1,abs(dr)]),"A"],"");
            end
        % Else use the other priority
        else
            if dc>=0
                route = join([repmat(">",[1,abs(dc)]),repmat(rowDir,[1,abs(dr)]),"A"],"");
            else
                route = join([repmat(rowDir,[1,abs(dr)]),repmat("<",[1,abs(dc)]),"A"],"");
            end
        end
        
        % Store route in dictionary
        dict(string(array(startIndex))+string(array(goalIndex))) = route;
    end
end

end