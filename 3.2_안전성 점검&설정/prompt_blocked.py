import google.generativeai as genai
import os

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
GOOGLE_API_KEY = "~~~~~~~~~~~~~~~~~~~~~~~~"

genai.configure(api_key = GOOGLE_API_KEY)

safety_settings=[
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
]

model = genai.GenerativeModel('gemini-pro', safety_settings)

response = model.generate_content("나는 네가 싫어!")  
#print(response._result)
if response.prompt_feedback.block_reason:
    print(f"사용자 입력에 다음의 문제가 발생하여 응답이 중단되었습니다: {response.prompt_feedback.block_reason.name}")
else:
    print(response.text)