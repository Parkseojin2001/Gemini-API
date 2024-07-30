import google.generativeai as genai
import os

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
GOOGLE_API_KEY = "~~~~~~~~~~~~~~~~~~~"

genai.configure(api_key = GOOGLE_API_KEY)

generation_config = genai.GenerationConfig(candidate_count=1)
model = genai.GenerativeModel('gemini-pro', generation_config = generation_config)

response = model.generate_content("인공지능에 대해 한 문장으로 설명하세요.")

print(response.text)
print(f"cadidate 생성 건수: {len(response.candidates)}")