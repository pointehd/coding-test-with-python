# TIL (Today I lean)

### 문자 입력받는법

- 일반 한줄 입력 받기 : `input()`
- 원하는 변수에 나눠받기 : `n, m, k = map(int, input().split()) ` (`5 8 3` -> n=5, m=8, k=3)
- 배열로 받기 : `list(map(int, input().split()))` (`5 8 3` -> [5, 8, 3])

### 정렬하는법

- 기본 리스트(arrays) 정렬 : `arrays.sort()` (기본 : 오름차순 정렬)

### python code vscode 자동 정렬하는법

- `.vscode/setting.json` 프로젝트 경로 파일 확인 (vscode global setting.json에 셋팅할 경우 글로벌로 설정됨.)
- vscode extensions python 설치
- vscode > file(파일) > user > Extensions > Python > Formatting:provider-black
- `pip install black` or `pip3 install black`
- 단축키 mac(`option + shift + F`), windows(`alt + shift + F`)
- 주의 .py 확장자만 적용됨.
- (해당 프로젝트만)
- autopep8, black, yapf 등의 규칙이 있다고 하니 관심있으면 확인하기 black으로 시작했으나 맘에들어서 다른것 테스트 X
