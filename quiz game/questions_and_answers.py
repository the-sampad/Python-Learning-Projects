class QuestionsAndAnswers:
    quesions = {
        "Tony Stark is Iron Man. ":'Yes',
        "Jarvis is more powerful and intelligent than Ultron. ":'No',
        "You are an Eternal.":'No',
        "Eternals are robots.":'Yes',
        "Spiderman is an Avenger":'Yes',
        "Something bad happens for a good yet to happen.":'Yes'
    }
    
    def ask_question(self,i):
        question_list = list(self.quesions)
        self.ask = question_list[i]
        return self.ask
    
    def is_answer_correct(self,answer):
        ans = self.quesions[self.ask].lower()
        if answer == ans:
            print('Correct Answer')
            return True
        else:
            print('Wrong Answer')
            return False
            


