function path = AstarReg(start,goal,mapArray)

path = [];
openSet = [start(1);start(2)];

originDict = dictionary;
mapSize = size(mapArray);

gScore = Inf(mapSize);
gScore(start(1),start(2)) = 0;

fScore = Inf(mapSize);
fScore(start(1),start(2)) = abs(sum(goal-start));

while ~isempty(openSet)
    
    openSetSize = size(openSet,2);
    fScores = zeros(openSetSize,1);

    for i=1:openSetSize
        fScores(i) = fScore(openSet(1,i),openSet(2,i));
    end

    [~,currentIndex] = min(fScores);
    current = [openSet(1,currentIndex);openSet(2,currentIndex)];

    if all(current==goal)
        path = reconstructPath(originDict, current);
    end
    
    % Remove current from open set
    openSet(:,currentIndex) = [];

    for direction=0:3
        neighbor = current;
        if direction==0
            neighbor(1) = neighbor(1)+1;
        elseif direction==1
            neighbor(2) = neighbor(2)+1;
        elseif direction==2
            neighbor(1) = neighbor(1)-1;
        else
            neighbor(2) = neighbor(2)-1;
        end

        if mapArray(neighbor(2),neighbor(1))==1
            continue
        end

        openSetSize = size(openSet,2);

        tentativeGScore = gScore(current(1),current(2)) + 1; % Distance between current and neighbor
        if tentativeGScore < gScore(neighbor(1),neighbor(2))
            originDict(neighbor(1)+100*neighbor(2)) = current(1)+100*current(2);
            gScore(neighbor(1),neighbor(2)) = tentativeGScore;
            fScore(neighbor(1),neighbor(2)) = tentativeGScore + abs(sum(goal-neighbor));

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
