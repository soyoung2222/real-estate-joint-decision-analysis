# Trade-off 설명 패턴 — 부동산 밖에서 찾기

*조사일 2026-08-19 · 소스 12 · 신뢰도 중상*
*`04-benchmarks.md`의 "충돌 표현 — 국내 부동산에는 참조할 것이 없다" 공백을 메우기 위한 조사*

> **도구 제약** — firecrawl·exa MCP가 없어 WebSearch/WebFetch로 수행했습니다.
> 학술 DB 전문 접근이 아니라 공개 논문·초록 기준입니다.

---

## 요약

**참조군은 부동산이 아니라 의료에 있었습니다.** 두 개 이상의 선택지 간 trade-off를
총점 없이 제시하는 문제는 **환자 의사결정보조자료(Patient Decision Aid, PtDA)** 분야에서
20년 넘게 표준화되어 왔고, **IPDAS**라는 국제 표준과 **Option Grid**라는 구체적 화면 형식이 있습니다.

그리고 우리가 "안 하기로 한 것"들에는 이미 정확한 학술 명칭이 있습니다 —
group recommender systems의 **집계 전략(aggregation strategy)** 계열입니다.

| 우리 결정 | 학술적 위치 | 상태 |
|---|---|---|
| 총점을 만들지 않는다 | IPDAS balanced information | ✅ 표준이 지지 |
| A/B를 나란히 놓는다 | side-by-side format | ✅ 실증 근거 있음 |
| 양쪽 완화안을 같이 낸다 | "does not favor one option over another" | ✅ 표준의 정의 자체 |
| 조건별 순위만 매기고 합치지 않는다 | Least Misery / Additive Utilitarian **회피** | ⚠️ 우리가 그 계열이 아님을 명시해야 함 |

---

## 1. IPDAS — 균형 있는 정보 제시의 국제 표준

International Patient Decision Aid Standards. 2021년 갱신된 정의는 다음과 같습니다.

> Objective, complete, salient, transparent, evidence-informed, and unbiased presentation of
> text and visual information about the condition and all relevant options
> — **in a way that does not favor one option over another** —
> and enables individuals to focus attention on important elements and process this information.
> ([Martin et al., *Medical Decision Making*, 2021](https://journals.sagepub.com/doi/full/10.1177/0272989X211021397))

핵심 논거는 **불균형한 제시가 인지 편향을 자극해 실제 선택을 바꾼다**는 것입니다.
실증 사례로, 불균형 정보를 받은 집단은 자궁경부암 위험을 과대추정했고 백신 접종 의향도 높아졌습니다.

### 우리 설계에 그대로 적용되는 권고

| IPDAS 권고 | 우리 화면에서 | 상태 |
|---|---|---|
| **Side-by-side 제시** — 40개 연구 중 28개가 사용, 균형 인식률 70~96% | 09번 Hero의 A/B 좌우 배치 | ✅ 이미 적용 |
| **개인 가치 우선 순서** — 중요하게 여기는 속성을 먼저 제시하면 가치일치 선택이 **70% → 90%** | 조건 표시를 **예산 → 통근 → 필수 → 확인** 순서로 고정 | ✅ 적용됨 |
| **모든 합리적 옵션 제시** (아무것도 하지 않는 선택 포함) | `둘 다 불충족`도 숨기지 않고 표시. "더 찾아보기" 경로 유지 | ⚠️ **경로 추가 검토** |
| **손실/이득 프레임 균형** — 한쪽 프레임만 쓰면 특정 선택 유도 | 양보 문장이 `잃는 것 + 얻는 것` 2단 구조 | ⚠️ **순서 고정 주의** ↓ |
| **평가적 조건화 금지** — 사진·증언이 옵션을 좋아 보이게 함 | 매물 사진을 판정 화면에서 강조하지 않음 | ⚠️ **검토 필요** |
| **사회적 증거 조작 금지** — "대부분의 사람들이 선택하는" | 인기순·추천순 표기를 쓰지 않음 | ✅ 계획에 없음 |
| **주의 조작 금지** — 중요 정보를 뒤에 배치하거나 강조를 차등 적용 | A와 B의 조건 블록을 **동일한 시각 비중**으로 | ⚠️ **명시 필요** |

### 여기서 나온 새 판단 셋

**① 조건 표시 순서를 고정한다.**
"개인 가치 우선 순서"가 가치일치 선택을 70%→90%로 올렸다는 건 큰 효과입니다.
우리는 필수 조건을 먼저 받으므로 데이터는 이미 있고, **화면에서 필수를 맨 위에 두는 것을 규칙으로 못박습니다.**

**② 양보 문장의 순서 자체가 프레이밍이다.**
현재 템플릿은 `[잃는 것] → [얻는 것]`으로 손실이 항상 먼저 옵니다.
손실 프레임이 앞에 오면 그 옵션을 회피하게 만들 수 있습니다.
→ **A안과 B안의 문장에서 손실·이득 순서를 동일하게 유지**하고, 한쪽만 손실을 먼저 쓰는 일이 없게 합니다.

**③ A와 B 블록의 시각 비중을 같게 한다.**
"주의 조작" 항목에 걸립니다. 초대자(A)의 조건이 더 크거나 위에 있으면 그 자체가 편향입니다.

---

## 2. Option Grid — 구체적 화면 형식

IPDAS를 실제 한 페이지 화면으로 구현한 형식입니다.

- **1페이지 표.** 행 = 사용자가 실제로 묻는 질문, 열 = 2~3개 선택지
- 각 칸에는 그 질문에 대한 **각 옵션의 답**. 점수·순위·추천 표시 없음
- 임상 전문용어를 빼고 **읽기 연령 10~12세** 기준으로 작성
- 의도적으로 짧게 유지 — 정보량 차이(1,565 vs 846단어)가 지식 변화에 유의미한 영향을 주지 않았다는 실증이 있음
  ([Option Grid 개요](https://intuitionlabs.ai/software/patient-education-engagement/shared-decision-making-tools/option-grid), [무릎 골관절염 Option Grid 프로토콜](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3986464/))

### 우리와 다른 점 하나 — 열이 무엇인가

```
Option Grid   열 = 선택지 (수술 / 물리치료 / 경과관찰)
우리          열 = 사람 (A / B)          ← 축이 다르다
```

Option Grid는 **한 사람이 여러 선택지를 비교**하고, 우리는 **두 사람이 한 선택지를 본다**.
따라서 형식은 빌려오되 **행에 무엇을 둘지는 우리가 정해야 합니다** — 우리 행은 "조건"입니다.

정보량 실증은 그대로 적용됩니다. **길게 쓴다고 더 이해되지 않습니다.**

---

## 3. 우리가 안 쓰기로 한 것들의 정확한 이름

Group Recommender Systems 분야에서 여러 사람의 선호를 하나로 합치는 방법들입니다.
([Sacharidis, *Top-N Group Recommendations with Fairness*](http://www.ec.tuwien.ac.at/~dimitris/publications/SAC19.pdf),
[group recommender 개요](https://towardsdatascience.com/an-introduction-to-group-recommender-systems-8f942a06db56/))

| 전략 | 계산 | 우리 판단 |
|---|---|---|
| **Additive Utilitarian** | 개인 점수의 **합** | ✗ 총점. `0001`이 금지한 바로 그것 |
| **Least Misery** | 개인 점수의 **최솟값** — 가장 불만족한 사람 기준 | △ 부분 채택 ↓ |
| **Most Pleasure** | 개인 점수의 **최댓값** | ✗ 한쪽을 무시함 |
| **Majority / Approval Voting** | 투표 | ✗ 2인에서 무의미 (1:1이면 항상 동점) |
| **Fairness** | 번갈아 만족시키기 | ✗ 집을 번갈아 고를 수 없음 |

### 우리 판정은 Least Misery의 이진 버전에서 한 걸음 더 간다

```
Least Misery       min(A, B) 만 남기고 나머지 탈락
                   → "한쪽만 충족"인 후보는 그냥 떨어진다

우리               min(A, B) 로 등급을 나누되
                   <한쪽만 충족>을 탈락이 아니라 <설명 대상>으로 승격
                   → 왜 min이 낮은지를 문장으로 되돌려준다
```

**이게 차별점의 정확한 학술적 위치입니다.** 우리는 집계 전략을 고르는 게 아니라
**집계를 거부하고 그 자리에 설명을 넣습니다.**

발표에서 "우리는 Least Misery를 쓰지 않습니다"가 아니라
**"집계 자체를 하지 않고 차이를 그대로 보여줍니다"** 로 말해야 정확합니다.

> 관련 최신 연구: [With Friends Like These, Who Needs Explanations?](https://arxiv.org/pdf/2505.04273) (2026)
> — 그룹 추천의 **설명이 사용자 이해에 실제로 도움이 되는가**를 평가.
> PDF 본문 파싱 실패로 결론 미확인. **후속 확인 필요.**

---

## 4. 채용 오퍼 비교 — 대부분 총점을 쓴다

| 도구 | 방식 |
|---|---|
| LoopCV | **100점 만점 스코어** + 카테고리별 분해 |
| AIApply | 모든 오퍼 분석 후 **best option 하이라이트** |
| MaxOfJob | 항목별 side-by-side (급여·에쿼티·PTO·보험·학습비) — 총점 없음 |
| Career Opportunity Calculator | 스프레드시트형 항목별 비교 |

([LoopCV](https://www.loopcv.pro/tools/job-offer-comparison/), [AIApply](https://tools.aiapply.co/job-offer-comparison-calculator), [MaxOfJob](https://maxofjob.com/job-comparison-tool))

**집노트와 같은 위치입니다.** 총점을 쓰는 게 기본이고 안 쓰는 게 예외라는 증거이며,
동시에 `decisions/0001`이 시장 관행에 역행하는 결정이라는 사실을 확인해 줍니다.
Tier 1 반대 사례 목록에 **LoopCV·AIApply를 추가**할 수 있습니다.

---

## 5. 보험 비교 UX — 방향은 같으나 근거는 약함

> 핵심 UX 과제는 **사용자를 대신해 결정하지 않으면서 trade-off를 이해시키는 것**이다.
> 어떤 플랜이 제시되는지만이 아니라 **왜 적합한지, 그리고 그것을 고르면 무엇을 포기하는지**를
> 알 수 있어야 한다. ([Lollypop, Insurance App Design, 2026](https://lollypop.design/blog/2026/august/insurance-app-design/))

우리 방향과 일치하지만 **업계 블로그 수준이라 근거 강도가 낮습니다.**
발표 인용은 IPDAS로 하고 이건 보조로만 씁니다.

---

## 반영할 것

| # | 조치 | 어디에 |
|---|---|---|
| 1 | ~~조건 표시 순서를 필수 → 선호 → 확인으로 고정~~ → ✅ **적용됨.** 최종 순서는 **예산 → 통근 → 필수 → 확인**이고, 선호는 비교표에서 빠져 사람 단위 카드가 됐다 | `08` 2부 · G10 |
| 2 | **A/B 블록의 시각 비중을 동일하게** | 09·14번 화면 |
| 3 | **양보 문장의 손실·이득 순서를 양쪽 동일하게** | FT5 명세 |
| 4 | **매물 사진을 판정 화면에서 강조하지 않음** (평가적 조건화) | 14번 |
| 5 | `둘 다 불충족`도 숨기지 않고 표시 + "더 찾아보기" 경로 | 14번 |
| 6 | **"집계를 하지 않는다"로 표현 통일** (Least Misery를 안 쓴다가 아니라) | 10·12번 |
| 7 | Tier 1 반대 사례에 LoopCV·AIApply 추가 | 12번 |
| 8 | 참조 서비스 "충돌 표현" 칸에 **IPDAS / Option Grid** 등재 | 12번 |

---

## 확인하지 못한 것

| 항목 | 상태 |
|---|---|
| arXiv 2505.04273 본문 (그룹 추천 설명의 효과) | ❌ PDF 파싱 실패 — 후속 확인 필요 |
| Option Grid 실제 화면 캡처 | ❌ 미확인 — 구조 서술만 확보 |
| 국내 의료 shared decision making 도구 | ❌ 미조사 |
| 통신 요금제 비교 UI | ❌ 유의미한 소스 없음 |
| IPDAS 체크리스트 원문 전체 | ❌ 요약 논문만 확인 |

---

## 조사 방법

WebSearch 5회, WebFetch 3회 (2회 성공). 하위 질문 5개:
① 의료 PtDA의 trade-off 제시 표준 ② 편향 없는 옵션 제시 설계 권고
③ 채용 오퍼 비교 도구 ④ 그룹 추천의 선호 집계와 공정성 ⑤ 보험·요금제 비교 UI
