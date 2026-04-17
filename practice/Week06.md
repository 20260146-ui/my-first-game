# 6주차 실습 기록
## 사용한 에셋
- 이미지: (22-Breakout-Tiles, Breakout (Brick Breaker) Tile Set - Free)
(24-Breakout-Tiles, Breakout (Brick Breaker) Tile Set - Free)
(26-Breakout-Tiles, Breakout (Brick Breaker) Tile Set - Free)
(27-Breakout-Tiles, Breakout (Brick Breaker) Tile Set - Free)
(30, https://sut22.itch.io/color-hearts)

- 사운드: (mixkit-twig-breaking-2945, mixkit Twig breaking)
(A walk.mp3,itch.io 8-Bit Style Music Pack)

## 사용한 AI 프롬프트 (요약)
1. 충돌 처리 코드 요청
2. 블록을 색상이 아닌 이미지로 표현하는 방법 요청
3. HP 이미지를 스프라이트 이미지로 변경
3. HP 시스템 및 게임 오버 처리 수정 요청
4. 스킬 UI 위치를 화면 왼쪽 하단으로 이동하는 방법 요청
5. 여러 개의 블록 이미지를 랜덤으로 적용하는 방법 요청

## AI 답변에서 도움이 된 것
블록을 이미지로 출력하는 기본적인 구조 이해
여러 개의 블록 이미지를 랜덤으로 적용하는 방법
HP 시스템과 게임 오버가 연결되는 흐름
스킬 UI를 원하는 위치로 옮기는 방법
전체 게임 구조(메인 루프, 이벤트 처리 등)에 대한 참고

## AI 답변을 수정하거나 버린 것
일부 코드에서 들여쓰기 오류가 발생하여 직접 수정함
오류를 해결하며 코드 구조를 정리함
블록 이미지 딕셔너리에서 중복 키 문제를 직접 수정함
불필요한 조건문 및 중복 UI 코드 제거

## 적용 결과
- 잘 된 것:
    블록이 색상이 아닌 이미지로 출력되도록 구현 성공
    여러 종류의 블록 이미지가 랜덤으로 생성되도록 개선
    HP 시스템과 게임 오버가 정상적으로 동작
    스킬 UI를 왼쪽 하단으로 이동 완료
    하트 애니메이션을 통해 시각적 효과 강화
- 어려웠던 것:
    코드 자체의 처리 과정을 이해하는 것이 어려웠음
    게임이 실행되면서 어떤 순서로 기능이 동작하는지 파악하기 힘들었음
    들여쓰기의 위치와 코드의 위치

- 다음에 시도할 것 : 
    다양한 아이템(속도 증가, 패들 확장 등) 추가
    게임 시작/종료 UI 디자인 개선
    게임 레벨 변화