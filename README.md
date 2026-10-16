# Yahoo! Auctions Japan - Music Gear Monitor

매시간 일본 야후옥션 악기 신규 매물을 검색합니다. GitHub Actions에서 실행하고, 새로운 매물은 상품명을 제목으로 GitHub Issue를 만듭니다.

## 검색 조건
- 키워드: Tyler, Gibson, PRS, Fender, Nord, Helix, Quad Cortex, Fractal
- 가격: 100,000엔 초과 ~ 1,000,000엔 미만
- Fender: USA 계열(아라이 카즈키 예외)
- Gibson: Epiphone / Orville 제외
- 액세서리 단독 매물 제외
- 야후옥션 상품 ID 기준 중복 알림 방지
- 검색결과 상위 최대 6페이지 확인

## 실행
- Actions → Yahoo Auctions Monitor → Run workflow
- 매시간 47분(UTC 기준, 한국/일본에서도 매시간 47분)에 자동 실행
- 첫 실행은 기존 매물을 기준점으로 저장하고 알림을 보내지 않습니다.
- 이후 새 상품을 찾으면 GitHub Issues에 **상품명, 가격, 원본 URL**을 기록합니다.
- 실패하거나 사이트 레이아웃이 변경된 경우 Actions의 실행 로그를 확인하세요.

## 주의
공개 저장소이므로 코드와 Issues는 모두 공개됩니다. 인증정보를 커밋하지 마세요.
공개 저장소의 기본 GitHub-hosted runner 실행 시간은 무료이지만 일반 플랫폼 제한과 야후옥션의 접속 제한은 여전히 적용됩니다.
