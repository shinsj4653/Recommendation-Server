# Recommendation-Server
> TF-IDF 이론을 기반으로 한 콘텐츠 필터링 추천 알고리즘 구현

**사용자가 찜한 도서의 ISBN 값을 담은 배열 및 추천 결과의 수를 입력받을 시, 해당 도서와 유사한 도서들을 추천 결과로 반환해 주는 로직에 해당하는 코드를 작성**했습니다.

CSV 파일로부터 책 데이터를 불러와서 데이터프레임 형태로 저장해 줬습니다. 책의 작가 이름이 완전히 같은 경우를 체크하기 위해 ‘same_author’ 열을 추가해 줬습니다. 작가 이름이 일치하지 않는 경우, 도서의 제목, 출판사, 그리고 장르를 고려하여 content 열을 만들었습니다. **TfidfVectorizer를 활용하여 ‘content’ 열의 데이터를 TF-IDF 벡터 형태로 변환해 줬고, TF-IDF 행렬을 사용하여 책들 간의 코사인 유사도를 계산**하였습니다. 사용자가 찜한 책들의 ISBN 값을 입력받아, 해당 책들의 인덱스 값을 indices 배열에 저장해 줬습니다. 찜한 책들로 다른 책들 간의 유사도 점수를 계산한 후, 유사도 높은 순으로 n개 만큼 결과를 반환하도록 해줬습니다.

TF-IDF 알고리즘을 파이썬 환경에서 적용할 수 있는 방법에 대해 학습할 수 있었고, 기회가 된다면 **콘텐츠 필터링 추천 알고리즘 활용 역량을 향후 사용자에게 맞는 금융 상품 추천 기능 구현에 활용**해 보고 싶습니다.

### pip install --upgrade pandas
### pip install -U scikit-learn
### 설치해야 합니다.

## 참고링크
https://eda-ai-lab.tistory.com/525
