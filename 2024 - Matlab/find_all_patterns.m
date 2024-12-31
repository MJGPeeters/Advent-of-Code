function [out,patternDict] = find_all_patterns(pattern,towels,patternDict)

numTowels = numel(towels);

if isscalar(pattern) && (pattern=='r' || pattern=='b' || pattern=='g')
    numOptions = 1;
elseif isscalar(pattern)
    numOptions = 0;
else
    numOptions = 0;

    for i=1:numTowels
        tmpOptions = 0;
        lenTowel = length(towels{i});

        if length(pattern)<lenTowel
            continue
        end
        
        startPattern = pattern(1:lenTowel);
        endPattern = pattern(lenTowel+1:end);

        if strcmp(startPattern,towels{i})
            if isempty(endPattern)
                tmpOptions = 1;
            elseif isKey(patternDict,string(endPattern))
                tmpOptions = patternDict(endPattern);
            else
                [tmpOptions,patternDict] = find_all_patterns(endPattern,towels,patternDict);
            end
        end
        
        numOptions = numOptions + tmpOptions;
    end

    patternDict(pattern) = numOptions;
end

out = numOptions;

end