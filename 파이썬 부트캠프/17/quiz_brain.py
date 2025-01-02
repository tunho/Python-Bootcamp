class QuizBrain : 
    def __init__(self, question_list):
        self.question_number = -1
        self.question_list = question_list
        self.answer = ""
        self.score = 0
    
    def next_question(self) :
        self.question_number += 1
        self.answer = input(f"Q.{self.question_number}: {self.question_list[self.question_number].Q} (True/False) :  ").strip()
        
    def still_has_question(self) :
        return self.question_number < len(self.question_list)-1  
    def check_answer(self, user_answer, correct_answer) :
        if user_answer.lower() == correct_answer.lower() :
            print("You got it right!")
            self.score += 1
        else : 
            print("That's wrong")
             
        print(f"The correct answer was : {correct_answer}.")    
        print(f"Your current is : {self.score}/{self.question_number+1}")   
    
         



        
    