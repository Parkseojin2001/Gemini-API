import google.generativeai as genai
import os

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
GOOGLE_API_KEY = "~~~~~~~~~~~~~~~~~~~~~~~~"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = genai.GenerationConfig(max_output_tokens=20)
model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)

user_message = "인공지능에 대해 한 문장으로 설명하세요."

response = model.generate_content(user_message)

print(response.text)
print(response._result)

