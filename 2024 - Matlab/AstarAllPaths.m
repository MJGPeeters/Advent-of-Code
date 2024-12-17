function pathArray = AstarAllPaths(start,goal,mapArray)

pathArray = zeros(size(mapArray));
pathArray(start(1),start(2)) = 1;
pathArray(goal(1),goal(2)) = 1;

openSet = [start(1);start(2);start(3)];

originDict = dictionary;
mapSize = [size(mapArray,1),size(mapArray,2),4];

gScore = Inf(mapSize(1),mapSize(2),mapSize(3));
gScore(start(1),start(2),start(3)) = 0;

fScore = Inf(mapSize(1),mapSize(2),mapSize(3));
fScore(start(1),start(2),start(3)) = abs(goal(1)-start(1)) + abs(goal(2)-start(2));

while ~isempty(openSet)
    openSetSize = size(openSet,2);
    fScores = zeros(openSetSize,1);

    for i=1:openSetSize
        fScores(i) = fScore(openSet(1,i),openSet(2,i),openSet(3,i));
    end

    [~,currentIndex] = min(fScores);
    current = [openSet(1,currentIndex);openSet(2,currentIndex);openSet(3,currentIndex)];

    if current(1)==goal(1) && current(2)==goal(2)
        pathArray = reconstructAllPaths(originDict, 1e4*current(1)+10*current(2)+current(3),zeros(size(mapArray)));
        return
    end
    
    % Remove current from open set
    openSet(:,currentIndex) = [];

    for change=1:3
        neighbor = current;
        if change==1
            if neighbor(3)==1
                neighbor(3) = 4;
            else 
                neighbor(3) = neighbor(3)-1;
            end
        elseif change==2
            if neighbor(3)==1
                neighbor(1) = neighbor(1)-1;
            elseif neighbor(3)==2
                neighbor(2) = neighbor(2)+1;
            elseif neighbor(3)==3
                neighbor(1) = neighbor(1)+1;
            else
                neighbor(2) = neighbor(2)-1;
            end
        else
            if neighbor(3)==4
                neighbor(3) = 1;
            else 
                neighbor(3) = neighbor(3)+1;
            end
        end

        if mapArray(neighbor(2),neighbor(1))==1
            continue
        end

        openSetSize = size(openSet,2);

        if change==2
            % Penalty for moving
            tentativeGScore = gScore(current(1),current(2),current(3)) + 1; 
        else
            % Penalty for rotating
            tentativeGScore = gScore(current(1),current(2),current(3)) + 1000; 
        end

        % If tentativeGScore is equal to other gScore, check previous two
        % locations between current line and previous line. If they are 
        % different, they come from a different square, if not they just
        % rotated around a few times to the same position. 
  
        if tentativeGScore <= gScore(neighbor(1),neighbor(2),neighbor(3))
            if tentativeGScore == gScore(neighbor(1),neighbor(2),neighbor(3))
                tmp = originDict(1e4*neighbor(1)+10*neighbor(2)+neighbor(3));
                tmp = tmp{1};
                newDictEntry = {[tmp, 1e4*current(1)+10*current(2)+current(3)]};
                originDict(1e4*neighbor(1)+10*neighbor(2)+neighbor(3)) = newDictEntry;
            else
                originDict(1e4*neighbor(1)+10*neighbor(2)+neighbor(3)) = {1e4*current(1)+10*current(2)+current(3)};
                gScore(neighbor(1),neighbor(2),neighbor(3)) = tentativeGScore;
                fScore(neighbor(1),neighbor(2),neighbor(3)) = tentativeGScore + abs(goal(1)-neighbor(1)) + abs(goal(2)-neighbor(2));
            end

            if openSetSize==0
                openSet = neighbor;
            else
                neighborInOpenSet = 0;
                for i=1:openSetSize-1
                    if all(openSet(:,i)==neighbor)
                        neighborInOpenSet = 1;
                        continue
                    end
                end
    
                if neighborInOpenSet==0
                    openSet = [openSet,neighbor];
                end
            end
        end
    end
end