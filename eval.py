#This script is used for subjective evaluation to different answers.
#Author by anony
#start_time: 2023.7.15
#end_time: 2024.1.9
#This assessment has two types of score,
# 1. The score from human this part will be example for llm'score(the second)
# 2. The score from GPT-4 or other LLMs
##被评估的模型可以分为本地测试与网络接口测试
#被评估的模型可以分为利用本地权重进行测试与利用开放的网络接口测试，主要针对开源模型与闭源模型
#The evaluated model can be divided into local testing and network interface testing
##评估流程:1.先获取问题的答案。2.将部分答案交予人类专家进行评估。3.将人类评估作为评估样例，输入gpt4。利用LLMs进行自动化评估。
# Assessment process:
# 1. Obtain the differen answer to the question first.
# 2. Submit some of the answers to human experts for evaluation.
# 3. Use human assessment as an evaluation example and input it into gpt4. Utilize LLMs for automated evaluation.
##getanswer.py获取问题的答案
##getscore.py获取问题的
from tool import get_question
def build_prompt(question,query1,query2):
    prompt=f"现在需要请你作为中医药方面的专家，对问题"
def eval_by_gpt4():
    #获取同一个问题的答案
    question=get_question(sample=False)
    question_answer=get_question(sample=False)
    compared_=get_question(sample=False)
    build_prompt(question["question_content"],question_answer["answer"],compared_["answer"])
