function [outputArray,route] = racetrackLength(start,goal,mapArray)

outputArray = NaN(size(mapArray,1));
route = zeros(2,1e5);
route(:,1) = [goal(1);goal(2)];

% We work backwards, so that goal has distance zero and start has the total
% distance. Therefore we initialize current as goal, and check in the while
% loop whether we are at start.
currentLength = 0;
outputArray(goal(1),goal(2)) = currentLength;
current = goal;
previous = current;

while ~all(current==start)
    nextUp = current + [-1,0];
    nextDo = current + [+1,0];
    nextLe = current + [0,-1];
    nextRi = current + [0,+1];

    if mapArray(nextUp(1),nextUp(2))==0 && any(nextUp~=previous)
        previous = current;
        current = nextUp;
    elseif mapArray(nextDo(1),nextDo(2))==0 && any(nextDo~=previous)
        previous = current;
        current = nextDo;
    elseif mapArray(nextLe(1),nextLe(2))==0 && any(nextLe~=previous)
        previous = current;
        current = nextLe;
    elseif mapArray(nextRi(1),nextRi(2))==0 && any(nextRi~=previous)
        previous = current;
        current = nextRi;
    end

    currentLength = currentLength+1;
    route(1,currentLength+1) = current(1);
    route(2,currentLength+1) = current(2);
    outputArray(current(1),current(2)) = currentLength;
end

route(:,~all(route,1) ) = [];

route = flip(route,2);

end