import google.generativeai as genai
import os
import PIL.Image

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
GOOGLE_API_KEY = "~~~~~~~~~~~~~~~~~~~~~~~~"

genai.configure(api_key = GOOGLE_API_KEY)
image_data = PIL.Image.open('/Users/parkseojin/Downloads/monalisa.jpg') # 모나리자 그림

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(["이 그림에 대해 한 문장으로 설명하세요.", image_data])

# 응답 구조
print(response._result)

# candidate 객체
print(f"건수: {len(response.candidates)}")
print("="*50)
for candidate in response.candidates:
    print(candidate)