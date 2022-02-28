---
title:  "[programmers] 파이썬 불량사용자"
layout: single
categories: 

  - programmers

tags:
  - [Algorithm, programmers]

toc: true
toc_sticky: true

date: 2022-02-28
last_modified_at: 2022-02-28
---
 [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/64064_)


 풀이

 ```python

def solution(user_id, banned_id):
    global ans
    ans = set()
    trav(0,user_id,banned_id,[False for _ in range(len(user_id))], [])


    return len(ans)

def trav(cnt, user_id, banned_id,visited, picked):
    global ans
    if cnt == len(banned_id):
        if check(picked, banned_id):
            ans.add(tuple(sorted(picked)))
        return
    else:
        for i in range(len(user_id)):
            if not visited[i]:
                picked.append(user_id[i])
                visited[i] = True
                trav(cnt + 1, user_id, banned_id, visited, picked)
                picked.pop()
                visited[i] = False

def check(picked, banned_id):
    for i in range(len(picked)):
        object_id = picked[i]
        mask = banned_id[i]
        if len(object_id) != len(mask):
            return False
        for idx in range(len(mask)):
            if mask[idx] == "*":
                continue
            else:
                if mask[idx] != object_id[idx]:
                    return False
    return True




user_ids = [["frodo", "fradi", "crodo", "abc123", "frodoc"],["frodo", "fradi", "crodo", "abc123", "frodoc"],["frodo", "fradi", "crodo", "abc123", "frodoc"]]
banned_ids = [["fr*d*", "abc1**"],["*rodo", "*rodo", "******"],["fr*d*", "*rodo", "******", "******"]]



for i in range(len(user_ids)):
    print(solution(user_ids[i], banned_ids[i]))

 ```


 전체 유저들의 아이디와 불량사용자 마스킹 아이디를 주면 가능한 불량 사용자의 리스트 수를 반환하는 문제

 우선 정답 리스트의 요소의 수는 결국 불량 사용자 마스킹 아이디의 수와 같을 것이다.
 
 따라서 전체 아이디에서 불량 사용자 마스킹 아이디의 요소 수만큼 순열로 뽑아준다. (백트래킹 이용) 

 순열로 뽑은 아이디 목록을 불량 사용자 마스킹 아이디와 대조해준다.

 문제에서 `제재 아이디 목록들을 구했을 때 아이디들이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.` 라고 했으니 set을 이용해 중복을 제거해주면 정답
