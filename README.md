
## RTR의 백엔드 개발용 레포지토리

## RTR이란?
사용자가 입력한 리뷰에 대해 얼만큼의 가치가 있는지 평가하고, 가치에 따라 적립금을 산출하는 AI 프로젝트 입니다.
 
저희는 리뷰 평가 AI 모델을 보여드리기 위해 간단한 의류 쇼핑 어플리케이션을 제작하여 그 안에 AI모델을 탑재하였으며 해당 레포지토리는 해당 어플리케이션을 구동하기 위한 백엔드 레포지토리입니다.

## Framework
fastapi

## Database
sqlite

## backend structure


📦
├─ README.md
└─ polarstar
   ├─ .eslintrc.json
   ├─ .gitignore
   ├─ README.md
   ├─ next.config.js
   ├─ package-lock.json
   ├─ package.json
   ├─ postcss.config.js
   ├─ public
   │  ├─ images
   │  │  ├─ favicon.ico
   │  │  ├─ loading
   │  │  │  └─ north.png
   │  │  ├─ onboarding
   │  │  │  ├─ icon_1.png
   │  │  │  ├─ icon_2.png
   │  │  │  ├─ icon_3.png
   │  │  │  ├─ mainPageUpscaled.png
   │  │  │  ├─ north.png
   │  │  │  └─ polar-bear.png
   │  │  └─ qna
   │  │     ├─ arrow_next.png
   │  │     ├─ arrow_prev.png
   │  │     └─ close.png
   │  ├─ next.svg
   │  └─ vercel.svg
   ├─ src
   │  ├─ app
   │  │  ├─ dummyData.tsx
   │  │  ├─ globals.css
   │  │  ├─ layout.tsx
   │  │  ├─ page.tsx
   │  │  ├─ qna
   │  │  │  ├─ page.tsx
   │  │  │  ├─ qnaData.tsx
   │  │  │  ├─ skillStack.json
   │  │  │  └─ skillStackData.tsx
   │  │  ├─ ref.tsx
   │  │  └─ result
   │  │     ├─ jd
   │  │     │  └─ page.tsx
   │  │     └─ lec
   │  │        └─ page.tsx
   │  ├─ components
   │  │  ├─ bubble.tsx
   │  │  ├─ button.tsx
   │  │  ├─ curriCell.tsx
   │  │  ├─ fadeButton.tsx
   │  │  ├─ introduce.tsx
   │  │  ├─ jdRecommendCell.tsx
   │  │  ├─ jdRecommendSummary.tsx
   │  │  ├─ objective.tsx
   │  │  ├─ onboarding.tsx
   │  │  ├─ opacityAni.tsx
   │  │  ├─ recoil.tsx
   │  │  ├─ seo.tsx
   │  │  ├─ skill.tsx
   │  │  ├─ skillSearchDropdown.tsx
   │  │  └─ subjective.tsx
   │  ├─ global
   │  │  ├─ globalAtom.tsx
   │  │  └─ globalConstant.tsx
   │  └─ interfaces
   │     ├─ components.tsx
   │     └─ server.tsx
   ├─ tailwind.config.js
   └─ tsconfig.json

backend
├─ read.me

├─ data_prototype

│  ├─ cate_1.csv
│  ├─ cate_2.csv
│  ├─ product.csv
│  └─ reviews.csv
├─ domain
│  ├─ create_review.py
│  ├─ detail.py
│  ├─ goods_list.py
│  └─ review_schema.py
├─ migarations
├─ neural_networks
│  ├─ scorer.py
│  └─ vectorizer.py
├─ alembic.ini
├─ data_init.py
├─ database.py
├─ main.py
└─ models.py


## 핵심 구조 설명
data_prototype : 데이터베이스에 들어갈 초기 쇼핑몰 데이터가 들어있는 파일
domain : api를 생성하기 위한 라우터, 스키마 등의 모델이 들어있는 파일
neural_networks : 리뷰를 카테고리와 관련성에 따라 백터화하는 모델과 관련있는 리뷰를 3단계로 분류하는 모델이 들어있다.
data_init.py : data_prototype의 csv의 파일을 데이터 베이스에 넣는 파일이다.
models.py : 데이터 베이스의 스키마 파일이다.
main.py : domain에서 정의한 API 엔드포인트들이 애플리케이션에 등록되고 사용하게 하는 파일이다.


## 초기 시작 단계
1. 터미널에 `alembic upgrade head` 라고 친다.
2. 생성된 db에 들어가 데이터 베이스가 생성되었는지 확인한다.
3. 터미널에` python data_init.py`을 실행시켜 쇼핑몰 데이터를 넣는다.
4. 터미널에 `uvicorn main:app --reload`을 실행시켜 서버를 연다.
