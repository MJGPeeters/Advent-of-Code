function out = check_all_connections(members,dict)

% Input
% Members - String array of all members in alphabetical order
% Dict    - Dictionary with all connections, in alphabetical order

% Output
% out - 1 if all members are connected, zero otherwise

numMembers = numel(members);

for i=1:numMembers-1
    member1 = members(i);
    if isKey(dict,member1) 
        memberList = dict(member1);
        memberList = memberList{1};
        for j=i+1:numMembers
            member2 = members(j);
            if ~any(memberList==member2)
                out = 0;
                return
            end
        end
    else
        out = 0;
        return
    end
end

out = 1;

end