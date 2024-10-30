import html

class QuestionFormat:
    def __init__(self,ques_text: str, ans_text: str):
        self.text = ques_text
        self.answer = ans_text

class QuizMaster:

    def __init__(self,ques_list: list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0
        self.current_question = None
    
    def ques_left(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number+=1
        question_t = html.unescape(self.current_question.text)
        return f"Q{self.question_number}: {question_t} "
    
    def check_answer(self,user_answer: str) -> bool :
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score+=1
            return True
        
        else:
            return False



        

    
        
        
    
        

