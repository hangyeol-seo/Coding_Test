def dfs(start,end,info,matrix,visited,route):
    visited[start]=1
    route.append(start)
    print(start,end,route)
    if start==end:
        print('end')
        return
    next_nodes=matrix[start]
    len_next_nodes=len(next_nodes)
    for i in range(len_next_nodes):
        if next_nodes[i]==1:
            if visited[i]==0:
                dfs(i,end,info,matrix,visited,route)
                
            else:
                if i in route:
                    position=route.index(i)
                    route=route[:position]
    
    
    
    
def make_route(info,matrix,visited):
    sheep_node=[]
    for i in range(1,len(info)):
        if info[i]==0:
            sheep_node.append(i)
    print(sheep_node)
    len_sheep_node=len(sheep_node)
    len_info=len(info)
    routes=[[] for _ in range(len_sheep_node)]
    for i in range(len_sheep_node):
        route=[]
        dfs(0,sheep_node[i],info,matrix,visited,route)
        visited=[0 for _ in range(len_info)]
        routes[i]=route
    return routes
        

def solution(info, edges):
    answer = 0
    len_info=len(info)
    matrix=[[0 for col in range(len_info)] for raw in range(len_info)]
    visited=[0 for _ in range(len_info)]
    
    for edge in edges:
        matrix[edge[0]][edge[1]]=1
        matrix[edge[1]][edge[0]]=1
    
    route=make_route(info,matrix,visited)
    print(route)
    return answer
