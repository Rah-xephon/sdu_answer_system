import os
import openai
import yaml


# 调用Chat-GPT API
engine = "text-davinci-003"

def chat(prompt,temperature=0.4):  # chatgpt调用函数
 try:
  answer=[]
  response = openai.Completion.create(
   model=engine,
   prompt=prompt,
   temperature=temperature,
   max_tokens=2500,
   # frequency_penalty=0.0,
   # presence_penalty=0.0,
   stop=["\nYOU:", "\nkiller:"],
   n=1
  )
  # print(response)
  a = response.choices[0].text
  answer.append(a)

  return answer
 except Exception as exc:
  # print("error-log:" + prompt + "exception:" + str(exc))
  return "broken:" + "error-log:" + prompt + "exception:" + str(exc)


# 调用GPT3 API进行对话
if __name__ == "__main__":

 # 获取api_key：
 with open(os.path.expanduser("config.yaml"), "r") as config:
  code=yaml.load(config, Loader=yaml.FullLoader)
  openai.api_key = code["OPENAI_API_KEY"]
  # openai.organization = code["Organization_ID"]
  query="用amos软件在验证性因子分析在计算d-separation花费了大量时间，为什么会这样？怎么做才能缩短时间"

  a=chat(query,0.3)
  print(a)

