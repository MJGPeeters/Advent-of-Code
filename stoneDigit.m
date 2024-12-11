function numStonesOut = stoneDigit(digitIn,stepsIn,digitMap,digitSteps,numStonesIn)

stepsAfter = stepsIn + digitMap{digitIn+1}(1);
digitsAfter = digitMap{digitIn+1}(2:end);
numStonesOut = numStonesIn;

if stepsAfter>=75
    numStonesOut = numStonesIn + digitSteps{digitIn+1}(75-stepsIn);
else
    for i=1:numel(digitsAfter)
        numStonesOut = numStonesOut + stoneDigit(digitsAfter(i),stepsAfter,digitMap,digitSteps,numStonesIn);
    end
end

end


%% Single digit (in seperate function)

% Check if steps until maxSteps (75) is smaller than stepsAfter. If so,
% add number of stones at maxSteps to running tally (does that work
% recursively?). If not, continue recursively and add the appropriate
% number of steps to the stepCounter. 

%% Multiple digits (in regular code)

% Use regular rules. For every stone after one blink, check if it has only
% one digit. If so, continue to Single digit rules (see above). If not,
% continue using Multiple digits rules (this part). 