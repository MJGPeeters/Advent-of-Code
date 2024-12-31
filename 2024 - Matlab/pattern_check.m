function possible = pattern_check(pattern,towels)

numTowels = numel(towels);
possible = 0;

if ~strcmp(pattern(end-1:end),'br')
    possible = 1;
else
    for i=1:numTowels
        towelPattern = towels{i};
        endPattern = pattern(end-length(towelPattern)+1:end);
        if strcmp(endPattern,towelPattern)
            possible = pattern_check(pattern(1:end-length(towelPattern)),towels);
        end
    end
end

end