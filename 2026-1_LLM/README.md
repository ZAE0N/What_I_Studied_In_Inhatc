# LLM 실습 기록

OpenAI API를 중심으로 진행한 LLM 실습 코드 모음입니다. 프롬프트 엔지니어링부터 Function Calling, STT/TTS, 이미지 분석, PDF 요약까지 주제별로 정리했습니다.

---

## 목차

### 1. OpenAI API 기초
| 파일 | 내용 |
|---|---|
| [Start_GPTAPI.py](Start_GPTAPI.py) | API 첫 호출 — 클라이언트 생성과 chat completion |
| [OpenAI_standard.py](OpenAI_standard.py) | Chat Completions API 표준 사용법 |
| [OpenAI_legacy.py](OpenAI_legacy.py) | 구형 Completions API (`gpt-3.5-turbo-instruct`) 비교 |
| [OpenAI_Response.py](OpenAI_Response.py) | 응답 객체 구조 파헤치기 |
| [SecureCoding_GPTAPI.py](SecureCoding_GPTAPI.py) | 시큐어 코딩 관점의 API 활용 |

### 2. 프롬프트 엔지니어링
| 파일 | 내용 |
|---|---|
| [Prompt_engineering1.py](Prompt_engineering1.py) | 프롬프트 기본 패턴 |
| [Prompt_engineering_2.py](Prompt_engineering_2.py) | 프롬프트 패턴 심화 |
| [FewShot_Prompt.py](FewShot_Prompt.py) | Few-shot 프롬프팅 |
| [Single_Turn_01.py](Single_Turn_01.py) | 싱글턴 대화 |
| [Multi_Turn_01.py](Multi_Turn_01.py) | 멀티턴 대화 — 대화 히스토리 관리 |

### 3. Function Calling
| 파일 | 내용 |
|---|---|
| [GPT_Date_Function.py](GPT_Date_Function.py) | 현재 시각 함수 + tools 스키마 정의 |
| [GPT_FunctionCall.py](GPT_FunctionCall.py) | Function Calling 기본 흐름 |
| [GPT_Timezone_Function.py](GPT_Timezone_Function.py) | 타임존 변환 함수 정의 |
| [GPT_Timezone_FunctionCall.py](GPT_Timezone_FunctionCall.py) | 타임존 함수를 붙인 호출 |
| [GPT_MultiTimezone_FunctionCall.py](GPT_MultiTimezone_FunctionCall.py) | 다중 함수 호출 처리 |
| [GPT_Streamlit_FunctionCall.py](GPT_Streamlit_FunctionCall.py) | Streamlit UI + Function Calling |

### 4. STT / TTS (음성)
| 파일 | 내용 |
|---|---|
| [STT_Whisper.ipynb](STT_Whisper.ipynb) | Whisper API로 음성 → 텍스트 |
| [Huggingface_whisper.ipynb](Huggingface_whisper.ipynb) | 로컬 Whisper 모델 (transformers) |
| [LLM_TTS.ipynb](LLM_TTS.ipynb) | TTS API로 텍스트 → 음성 |
| [TTS_JSON_Speech.ipynb](TTS_JSON_Speech.ipynb) | JSON 대본 기반 음성 생성 |
| [STT_Audio_Chunks.csv](STT_Audio_Chunks.csv) | 음성 청크 분할 결과 |

### 5. 이미지 분석 (Vision)
| 파일 | 내용 |
|---|---|
| [Image_description.ipynb](Image_description.ipynb) | 이미지 설명 생성 |
| [Image_Analyzer.ipynb](Image_Analyzer.ipynb) | 이미지 분석 파이프라인 |
| [Image_Quiz.ipynb](Image_Quiz.ipynb) | 이미지 기반 퀴즈 자동 출제 |
| [Image_Quiz_01.ipynb](Image_Quiz_01.ipynb) | 퀴즈 생성 개선 |
| [Image_Quiz_Eng.ipynb](Image_Quiz_Eng.ipynb) | 영문 퀴즈 생성 |
| [Image_Quiz_EngListening.ipynb](Image_Quiz_EngListening.ipynb) | 영어 듣기 문제 생성 |

### 6. PDF 처리 / 요약
| 파일 | 내용 |
|---|---|
| [PDFfile_Text.py](PDFfile_Text.py) | PyMuPDF로 PDF 텍스트 추출 |
| [PDFfile_Preprocessing.py](PDFfile_Preprocessing.py) | 추출 텍스트 전처리 |
| [PDF_Summary.py](PDF_Summary.py) | PDF 논문 요약 |
| [Text_Summary.py](Text_Summary.py) | 텍스트 요약 |

### 7. 기타
| 파일 | 내용 |
|---|---|
| [Streamlit_Basic.py](Streamlit_Basic.py) | Streamlit 기본 |
| [Welcome.py](Welcome.py) | 첫 실행 확인용 |

---

## 실행 환경 설정

### 1. 가상환경 및 패키지

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

> `transformers` / `torch` 는 설치 용량이 큽니다. 로컬 Whisper 실습([Huggingface_whisper.ipynb](Huggingface_whisper.ipynb))을 하지 않을 거라면 [requirements.txt](requirements.txt)에서 해당 줄을 빼고 설치하세요.

### 2. API 키 설정

[.env.example](.env.example)을 `.env`로 복사한 뒤 본인 키를 채웁니다.

```bash
copy .env.example .env
```

```
OPENAI_API_KEY=sk-proj-...
```

키는 [platform.openai.com/api-keys](https://platform.openai.com/api-keys)에서 발급합니다. `.env`는 [.gitignore](.gitignore)에 등록되어 있어 커밋되지 않습니다. **소스코드에 키를 직접 적지 마세요.**

### 3. ffmpeg 설치 (음성 실습에만 필요)

Whisper / TTS 관련 코드는 ffmpeg를 사용합니다. 저장소에는 바이너리를 포함하지 않았으니 직접 설치하세요.

- 다운로드: <https://www.gyan.dev/ffmpeg/builds/> (Windows full build)
- 압축을 푼 뒤 `bin` 폴더를 시스템 PATH에 등록

```bash
ffmpeg -version
```

### 4. 실행

```bash
python Start_GPTAPI.py
```

Streamlit 예제는 다음과 같이 실행합니다.

```bash
streamlit run GPT_Streamlit_FunctionCall.py
```

---

## 저장소에 포함하지 않은 파일

실습에 쓴 원본 데이터 중 일부는 저작권 또는 개인정보 문제로 저장소에서 제외했습니다. 아래 코드를 그대로 실행하려면 해당 파일을 직접 준비해 경로에 맞게 넣어야 합니다.

| 필요한 파일 | 사용하는 코드 | 대체 방법 |
|---|---|---|
| `Data/KSCI_Paper.pdf` (논문 원문) | [PDFfile_Text.py](PDFfile_Text.py), [PDFfile_Preprocessing.py](PDFfile_Preprocessing.py), [PDF_Summary.py](PDF_Summary.py), [Text_Summary.py](Text_Summary.py) | 아무 PDF 논문으로 대체 가능 |
| `Audio_Boohwal.mp3`, `Data/STT_Audio_58s.mp3` (음원) | [STT_Whisper.ipynb](STT_Whisper.ipynb), [Huggingface_whisper.ipynb](Huggingface_whisper.ipynb) | 직접 녹음한 음성 파일로 대체 |
| `Data/Audio/Eng_Listening_1.mp3`, `_2.mp3` | [TTS_JSON_Speech.ipynb](TTS_JSON_Speech.ipynb) | 노트북 내 TTS로 직접 생성 가능 |
| `Data/Images/Team_Jeju_Image.jpg` (인물 사진) | [Image_Quiz.ipynb](Image_Quiz.ipynb) | `Data/Images/Image_Sample.jpg`로 교체되어 있음 |

`Data/Images/Image_Sample.jpg`, `Image_Sample_01.jpg`, `Data/Audio/LLM_TTS_Sample*.mp3`(TTS로 생성한 결과물)는 저장소에 포함되어 있어 바로 실행할 수 있습니다.

## 참고

노트북은 저장 용량과 개인정보 문제로 **실행 결과(output)를 일부 비운 상태**입니다. 직접 실행해 결과를 확인하세요.
