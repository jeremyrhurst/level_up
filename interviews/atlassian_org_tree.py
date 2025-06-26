"""
Imagine you are the team that maintains the Atlassian employee directory.

At Atlassian - there are multiple groups, and each can have one or more groups. Every employee is part of a group.

You are tasked with designing a system that could find the closest common parent group  given a target set of employees in the organization.

Tree Example

             [Company]
          /              \
        [HR]            [Engg]
      /   \          /          \
     Mona  Springs  [BE]         [FE]
                    /  \        / \
                  Alice Bob  Lisa Marley

Input Target employees (String) - Alice, Marley
Output (String/GroupNode): Engg

data class GroupNode (
    val groupName: String,
    val groups : Set<GroupNode> = emptySet(),
    var employeesInGroup : Set<Employee> = emptySet(),
)

data class Employee (
    val employeeId: UUID,
    val employeeName: String,
) 

"""
Class GroupNode(groupName, groups, employeesInGroup) (
    val groupName: String,
    val groups : Set<GroupNode> = emptySet(),
    var employeesInGroup : Set<Employee> = emptySet(),
)



def dfs(name, path, node):
    path.append(node.groupName)
    if name in node.employeesInGroup:
        return path
    for group in node.groups:
        return dfs(name, path, group)
   
# [Company]

#  names = Alice, Marley
def find_common(names, groupNode):
    paths = []
    for name in names:
        paths.append(dfs(name, [], groupNode)
   
    # [[company, engg, BE],[company, engg, FE] ,[company, HR]]]
    # Find closest to end similar for all paths
    shortest = len(paths[0])
    for item in paths:
        if len(item) < shortest:
            shortest = len(item)
   
    # Find the first group which is different and return the previous node
    for i in range(0, shortest):
        cur = paths[0][i]
        for path in paths:
            if path[i] != cur:
                return path[i-1]
    return("Not found")
   
   
    # Time complexity: N*M+X*Y = N*M = N^2