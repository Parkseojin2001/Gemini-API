import google.generativeai as genai
import os

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
GOOGLE_API_KEY = "~~~~~~~~~~~~"

genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("당신은 뛰어난 연극 배우입니다. 화난 대사를 읊어보세요.")  
print(response._result)