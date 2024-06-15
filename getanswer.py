#this is an auto script for getting answers from diferent LLMs
#Author by .heyizhang.TJU.TJUDB
#start_time: 2023.7.15
#end_time: 2024.1.9
#overwrited for subjective evaluation
import requests
from tool import getsubquestions,saveanswer
questions=getsubquestions()
answers=[]
#获取问题列表
print(questions)
messages = []
for question in questions:
    query=question["question_content"]
    print(query)
    messages.append({'role': 'user', 'content': query})
    r = requests.post('http://127.0.0.1:8100/', json={"prompt": query, "history": []},headers={'Content-Type':'application/json'})
    print(r.json())
    response=r.json()["response"]
    answers.append(response)
    print(answers)
saveanswer(answers,'./answer.json')

print("OK")

