class Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers  # This is a list of possible answers.
        self.correct_answer = correct_answer  # This is the index of the correct answer in the list.

    def ask_question(self):
        print(self.question)
        for i, answer in enumerate(self.answers, 1):
            print(f"{i}. {answer}")
        user_answer = int(input("Enter the answer number: "))
        return user_answer == self.correct_answer
questions = [
    Question("The owner of Disney ?", ["Answer1", "Robert Iger", "Answer3", "Answer4"], 2),
    Question("The publish year of Shrek ?", ["2001", "Answer2", "Answer3", "Answer4"], 1),
    Question("Who made Cinderella story ?", ["Answer1", "Charles Perrault", "Answer3", "Answer4"], 2),
    Question("The important time for Cinderella ?", ["Answer1", "Answer2", "12PM", "Answer4"], 3),
    Question("Name of the lover of Rapunzel ?", ["Answer1", "Flynn Rider", "Answer3", "Answer4"], 2),
    Question("Name of the sword of King Arthur ?", ["Answer1", "Answer2", "Answer3", "Excalibur"], 4),
    Question("The Beauty got love with ?", ["Answer1", "beast", "Answer3", "Answer4"], 2),
    Question("Cinderella published in ?", ["Answer1", "Answer2", "Answer3", "1697"], 4),
    Question("Eddi  murphy was talked as ?", ["Donkey", "Answer2", "Answer3", "Answer4"], 1),
    Question("Who was singer in Snowwhite Story?", ["Adriana Caselotti", "Answer2", "Answer3", "Answer4"], 1),
    # ... add more questions/ I did not write wrong answer to check it be more easy.
]
def play_game(questions):
    scores = [0, 0]  # Player 1 and Player 2 scores.
    for i in range(len(questions)):
        current_player = i % 2
        print(f"Player {current_player + 1}'s turn.")
        if questions[i].ask_question():
            print("Correct!")
            scores[current_player] += 1
        else:
            print("Wrong!")
        print(f"Current score: Player 1: {scores[0]}, Player 2: {scores[1]}")
        print("\n")

    # Determine the winner
    if scores[0] > scores[1]:
        print("Player 1 wins!")
    elif scores[1] > scores[0]:
        print("Player 2 wins!")
    else:
        print("It's same!")
play_game(questions)
