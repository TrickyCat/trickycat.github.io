---
layout: post
title: "Offline Lowest Common Ancestor in a Tree"
description: "Find the lowest common ancestor of pairs of nodes in the tree"
tags: ["graph", "tree", "rooted tree", "lca", "lowest common ancestor", "tarjan's offline lowest common ancestor", "algorithm", "code"]
comments: false
---

![Tree](/content/binary/img/tree.webp){:style="display:block; margin-left:auto; margin-right:auto; max-width: 70%;"}

Just a brief reminder post.

From time to time one faces the task of finding the lowest common ancestor (LCA) for given pairs of nodes in the rooted tree.

Let's name any such pair of nodes for which we're interested in finding the LCA for, a query.

And in case when those queries are offline we can use Tarjan's algorithm.

**:information_source: Note:**

> Offline queries = all queries are known ahead of time before the start of the algorithm.
>
> As opposed to online queries when, for example, there can be a graph and a stream of queries of unknown size and contents, and we have to answer the queries as they arrive.


So, Tarjan's algo is suitable for handling offline queries, as it answers them during the traversal of the tree based on the current intermediate state of the tree traversal process (which by definition changes over time during the tree visiting routine).


```csharp
interface DisjointSet
{
    void Union(int x, int y);
    int Find(int x);
}

class OfflineLcaTarjan
{
    List<int>[] adj;
    List<int>[] queries;
    int[] ancestor;
    bool[] visited;
    DisjointSet dSet;

    void Dfs(int u)
    {
        ancestor[u] = u;

        foreach (var v in adj[u])
        {
            // 💡 Since we're dealing with a tree we can leave out
            // the check that v is not visited (otherwise, there is a cycle => not a tree)

            Dfs(v);
            dSet.Union(u, v);
            ancestor[dSet.Find(u)] = u;
        }

        visited[u] = true;

        foreach (var otherNode in queries[u])
        {
            if (visited[otherNode])
            {
                var lca = ancestor[dSet.Find(otherNode)];
            }
        }
    }

    public void ComputeLCAs()
    {
        // Init n
        // Init tree's adjacency list
        // Init disjoint set
        // Init ancestor, visited, and queries

        // foreach (var (u, v) in raw_queries)
        // {
        //   queries[u].Add(v);
        //   queries[v].Add(u);
        // }

        // Start the DFS from some arbitrary node picked as the tree's root
        Dfs(0);
    }
}
```

:wink:
