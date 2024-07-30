# 마침표나 느낌표가 등장하면 언어 생성을 중지시키는 코드
import google.generativeai as genai
import os

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
GOOGLE_API_KEY = "~~~~~~~~~~~~~~~~~~~~"

genai.configure(api_key = GOOGLE_API_KEY)

generation_config = genai.GenerationConfig(stop_sequences=[".","!"])
model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)
response = model.generate_content("인공지능에 대해  한 문장으로 설명하세요.")

print(response.text)

# 토큰의 수 확인
tokens = model.count_tokens("Learn about language model tokenization.")
print(tokens)