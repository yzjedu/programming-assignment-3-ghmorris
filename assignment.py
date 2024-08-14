# Programmer: Grace-Ann Morris 
# Course: CS701/GB-731, Dr. Yalew
# Date: August 13, 2024 
# Programming Assignment: 3
# Program Inputs: A string containing answers
# Program Outputs: Very Good! (If 100% correct) or You missed X questions: <incorrect answers> and Your score is: X percent

#Define the correct answers
CORRECT_ANSWERS = "adbdcacbdac"
#Input Validation
def get_user_answers():
    while True:
        #Ask the user for their answers
        user_answers = input("Enter your exam answers:")
        #Check answers for the exam 
        if len(user_answers) == len(CORRECT_ANSWERS):
            return user_answers
        else: #Show error that an incorrect number of answers were given
            print("Error: an incorrect number of answers given.")
            print(f"Enter your exam answers (e.g., 'abcabcabcbc'): ")

def grade_exam(user_answers):
    #Define variables for grading
    num_correct = 0
    results = ""
    #Compare user input with correct answers
    for i in range(len(CORRECT_ANSWERS)):
        if user_answers[i] == CORRECT_ANSWERS[i]:
            num_correct += 1
            results += user_answers[i]  #Show correct answer
        else:
            results += 'X'  #Show incorrect answer
    
    #Calculate the score percentage
    score_percentage = (num_correct / len(CORRECT_ANSWERS)) * 100
    #Round the percentage
    score_percentage_rounded = round(score_percentage)
    #Calculate the number of missed questions
    missed_questions = len(CORRECT_ANSWERS) - num_correct
    return results, score_percentage_rounded, missed_questions

#Show output of the users results 
def display_results(results, score_percentage, missed_questions):
    print(f"Answer Key: {results}")
    print(f"Your score is: {score_percentage} percent")
    #Provide feedback if the users score is 100 
    if score_percentage == 100:
        print("Very Good!") 
    else:
        print(f"You missed {missed_questions} questions: {results}")

def main():
    user_answers = get_user_answers()
    results, score_percentage, missed_questions = grade_exam(user_answers)
    display_results(results, score_percentage, missed_questions)
# Run the main function
if __name__ == "__main__":
    main()

