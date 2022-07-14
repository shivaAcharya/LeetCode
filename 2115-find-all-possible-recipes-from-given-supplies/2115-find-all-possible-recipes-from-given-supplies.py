class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        #build graph
        G = defaultdict(list)
        for i, ingredient in enumerate(ingredients):
            for ing in ingredient:
                G[ing].append(recipes[i])

        res = []
        indegrees = {}

        # initialize
            
        for i in range(len(supplies)):
            indegrees[supplies[i]] = 0

        for i, recipe in enumerate(recipes):
            indegrees[recipe] = indegrees.get(recipe, 0) + len(ingredients[i])

        Q = deque(supplies)


        while Q:
            cur = Q.popleft()
                
            for neighbor in G[cur]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    res.append(neighbor)
                    Q.append(neighbor)
        return res
                
