---
title:  "[programmers] 파이썬 늑대와양"
layout: single
categories: 

  - programmers

tags:
  - [Algorithm, programmers]

toc: true
toc_sticky: true

date: 2022-03-05
last_modified_at: 2022-03-05
---


[문제링크](https://programmers.co.kr/learn/courses/30/lessons/92343)


풀이

```python
import sys
sys.setrecursionlimit(10**4)
def solution(info, edges):
    graph = [[]for _ in range(len(info))]
    for edge in edges:
        f,e = edge
        graph[f].append(e)
    global answer
    answer = 0

    def trav(current, sheep, wolf, router):
        global answer
        if info[current] == 0:
            sheep += 1
        else:
            wolf += 1
        if answer < sheep:
            answer = sheep
        if wolf >= sheep:
            return
        for next in graph[current]:
            router.append(next)


        for next in router:
            router_ = router[:]
            router_.remove(next)

            trav(next, sheep, wolf, router_ )

    trav(0,0,0, [])
    

    return answer

```

어려웠던 문제. 기존에 dfs 유형과는 약간 달랐다.

이 문제의 핵심 아이디어는 `지나갔던 정점은 다시 방문하더라도 아무 변화가 없다` 라는 점 이다.

최초 방문시 해당 정점에 있었던 늑대/양이 따라온다고 표현되었다. 결국 같은 정점을 다시 방문해도 결국에는 의미가 없다.

각 정점을 방문할 때 마다 양과 늑대 둘 중 한마리를 얻게 될 것이고 이는 앞으로 방문할 수 있는 정점을 결정짓는 조건이 된다. 정점을 방문할때 마다 조건은 바뀌게 된다.

그러므로 매 정점을 방문할 때마다(dfs 호출시) 다음 차례에 이동 가능한 정점을 따로 담아서 dfs를 수행하면 정답이다.(위 코드에서 router)