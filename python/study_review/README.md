---
title: 'Chai calculator'
date: '2021-05-06'
---

# Study review

매일 공부한걸 복습할 수 있게 해주는 프로젝트.

> 1, 4, 7, 14, 30일 누적 복습법. 누적 복습 방법으로서 당일 진도를 나가기 전에 전날분 진도와 해당 날짜에서 -3 -6 -13 -29를 해준 날짜의 진도를 함께 복습하는 방법


## 기능 기획

- 공부 기록하기
  - 지금 쓰고 있는 vimwiki(TIL)을 최대한 활용
  - 기록하는 방법
    - 매일 `날짜.md` 파일에 기록하는 방법
      - 장점; 매일 공부한 내용을 복습할때 보여주기 편리함. 범용성이 늘어남
      - 단점; 공부한 내용이 정리되지 않는 문제
    - 지금처럼 주제별로 기록하는 방법
      - 장점; 기록하기 편리함
      - 단점; 매일 공부한 내용을 보여주기가 애매함. commit 기준으로 해야될듯. 서비스의 범용성이 떨어짐
    - 주제별로 기록하고 매일 diary 형태로 해당 주제 link를 기록하는 방법
      - 장점; 구현하기가 쉬워짐. 매일 해당 link만 제공해주면 됨.
      - 단점; 써야될게 늘어남
- 공부한 기록을 가져오기
- 매일 복습해야 할 내용을 보여주기

- 나중에는 블로그와 통합하면 좋을듯 (next.js로 블로그 구현 + 해당 서비스 붙이기)

### 기획

작게 시작하기; 간단하게 시작해서 완성 후 나중에 기능 추가
- github commit 기준으로 공부한 내용 보여주기

- [ ] github api? -> 특정 repository의 commit 보는 api 탐색하기
  - github api: https://docs.github.com/en/rest/reference/repos#commits
  - github graphql: https://docs.github.com/en/graphql/overview/explorer
  - 둘 다 diff에 바로 접근은 힘들고 commitUrl 제공 -> 변경된 부분만 보면 되니깐 일단 commitUrl을 열어서 공부한 내용을 확인하는 방향으로 구현

```
# Type queries into this side of the screen, and you will 
# see intelligent typeaheads aware of the current GraphQL type schema, 
# live syntax, and validation errors highlighted within the text.

# We'll get you started with a simple query showing your username!
query { 
  repository (name: "til", owner:"bartkim0426") {
    ref(qualifiedName: "master") {
      target {
        ... on Commit {
          id
          history(first: 5) {
            pageInfo {
              hasNextPage
            }
            edges {
              node {
                messageHeadline
                oid
                message
                changedFiles
                commitUrl
                committedDate
              }
            }
          }
        }
      }
    }
  }
}
```

### spec (v1)

- function: get commit url from TIL repository

- web application
  - django (full stack) ? -> 딱히 backend 영역이 아예 없기 때문에 그냥 frontend로 구현
  - react or next.js -> vercel

### 목표
- 5/8~5/15: 날짜별로 git commit 한거 화면에 띄워주기
