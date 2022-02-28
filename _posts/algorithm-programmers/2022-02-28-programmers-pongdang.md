---
title:  "[programmers] 파이썬 징검다리 건너기"
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

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/64062)

풀이

``` python
def solution(stones, k):

    start = 0
    end = max(stones)
    while start <= end:

        mid = (start + end) // 2

        flag = operate(stones,k,mid)
        if flag:
            start = mid + 1
        else:
            end = mid - 1
            answer = end
    return answer + 1

def operate(stones, k, val):
    stones = stones[:]

    cnt = 0
    for stone in stones:
        if stone - val <= 0:
            cnt += 1
        else:
            cnt = 0

        if cnt >= k:
            return False

    return True


print(solution([20,8,8,8,9,9,9,8,8,8,8], 3))
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
```

문제에서, 효율성과 정확성을 언급했고 원소들의 값 범위가 200000000로 주어졌다.

문제 자체도 그렇고 조건도 그렇고 이분탐색 풀이를 생각해내는 것은 어렵지 않았으나 생각지 못한 문제로 애를 먹었다.

처음에 이분탐색을 하고 나서 값을 징검다리에 적용시킬때(operate 함수에서), 먼저 징검다리를 전부 순회하면서 값을 빼준 후(O(n)) 다시 리스트를 순회하며 건너뛰기 조건을 계산(O(n))했었다. 어짜피 똑같이 n번 리스트 순회를 2번 하는 것이므로, big-o 표기법에서는 같은 시간복잡도를 갖기때문에 괜찮을 것이라 생각했었다

하지만 계속 효율성 테스트에서 실패했다. 그래서 순회 한번에 두 작업을 모두 하게끔 수정했더니 통과.
프로그래머스 문제는 big-o 시간복잡잡도 뿐만 아니라 쓸데없는 연산은 최대한 줄여야하나 보다.