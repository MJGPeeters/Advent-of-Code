function path = Astar(start,goal,mapArray)

path = [];
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
        path = reconstructPath(originDict, current);
    end
    
    % Remove current from open set
    openSet(:,currentIndex) = [];

    for change=1:3
        neighbor = current;
        if change==1
            if current(3)==1
                neighbor(3) = 4;
            else 
                neighbor(3) = neighbor(3)-1;
            end
        elseif change==2
            if current(3)==0
                neighbor(1) = neighbor(1)-1;
            elseif current(3)==1
                neighbor(2) = neighbor(2)+1;
            elseif current(3)==2
                neighbor(1) = neighbor(1)+1;
            else
                neighbor(2) = neighbor(2)-1;
            end
        else
            if current(3)==4
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
  
        if tentativeGScore < gScore(neighbor(1),neighbor(2),neighbor(3))
            originDict(1e4*neighbor(1)+10*neighbor(2)+neighbor(3)) = 1e4*current(1)+10*current(2)+current(3);
            gScore(neighbor(1),neighbor(2),neighbor(3)) = tentativeGScore;
            fScore(neighbor(1),neighbor(2),neighbor(3)) = tentativeGScore + abs(goal(1)-neighbor(1)) + abs(goal(2)-neighbor(2));

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