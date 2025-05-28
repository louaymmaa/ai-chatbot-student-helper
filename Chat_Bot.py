from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Predefined questions and answers
qa_pairs = [
    ("What programming courses are offered in summer?", "Common summer CS courses include Data Structures, Algorithms, and Web Development."),
    ("Is Data Structures available in summer?", "Yes, Data Structures (CS201) is typically offered as an intensive 8-week summer course."),
    ("Can I take Algorithm Design in summer?", "Yes, Algorithm Design (CS301) is available in summer with a focus on practical implementations."),
    ("Are there any AI courses in summer?", "Introduction to AI (CS401) is offered in summer with hands-on machine learning projects."),
    ("What about Database courses?", "Database Systems (CS302) runs during summer with intensive lab sessions."),
    ("Is Software Engineering offered in summer?", "Yes, Software Engineering (CS304) includes summer team projects with local tech companies."),
    ("Are there any Web Development courses?", "Full-stack Web Development (CS305) is offered as an intensive summer course."),
    ("What programming languages are taught in summer?", "Python, Java, and JavaScript courses are typically available in summer."),
    ("Are Computer Networks courses available?", "Yes, Computer Networks (CS303) runs with practical networking labs in summer."),
    ("Can I take Operating Systems in summer?", "Operating Systems (CS306) is offered with intensive lab components."),
    ("What about Mobile App Development?", "Mobile App Development (CS307) is available with Android/iOS projects."),
    ("Are there any Cybersecurity courses?", "Introduction to Cybersecurity (CS308) runs during summer semester."),
    ("What CS electives are available in summer?", "Cloud Computing, Machine Learning, and Game Development are common summer electives."),
    ("Are programming labs open in summer?", "Yes, CS labs are open with modified hours and teaching assistants available."),
    ("Can I do a CS internship for credit?", "Yes, CS internships (CS399) can be taken for credit during summer."),
    ("What about senior projects in summer?", "Senior projects (CS499) can be completed during summer semester."),
    ("Are there CS research opportunities?", "Faculty often hire CS students for summer research projects."),
    ("What CS prerequisites can I take?", "Core prerequisites like Calculus and Discrete Math are usually offered."),
    ("Is there CS tutoring in summer?", "CS tutoring services continue with modified hours during summer."),
    ("Are CS project rooms available?", "Project rooms can be reserved for team assignments during summer."),
    ("When does the summer semester start?", "The summer semester typically starts in June, but check the academic calendar for exact dates."),
    ("What is the maximum course load in summer?", "CS students can take up to 4 courses or 12 credit hours during summer."),
    ("Are summer CS courses more intensive?", "Yes, summer CS courses cover the same material in 8 weeks with more frequent lab sessions."),
    ("Can I take online CS courses in summer?", "Yes, several CS courses are offered online with virtual lab components."),
    ("What is the attendance policy?", "Due to intensive lab work, strict attendance is required for summer CS courses."),
    ("Can I withdraw from summer courses?", "Yes, but check the withdrawal deadlines in the academic calendar."),
    ("Is summer semester mandatory?", "No, but it's useful for completing CS prerequisites or catching up on requirements."),
    ("Are all CS courses offered in summer?", "No, only selected CS courses run during summer - check the department schedule."),
    ("What if a required CS course isn't offered?", "Consult your CS advisor about course substitutions or waiting until fall."),
    ("How many CS sections are offered?", "Most summer CS courses have 1-2 sections with limited enrollment."),
    ("Is financial aid available?", "Yes, check with financial aid about summer funding options."),
    ("Can international students take CS courses?", "Yes, with proper visa status and department approval."),
    ("Are CS faculty available in summer?", "Yes, but they may have modified office hours for summer courses."),
    ("What about CS academic advising?", "CS advisors are available with modified summer schedules."),
    ("Can I use CS software licenses in summer?", "Yes, all department software licenses remain active during summer."),
    ("Are there CS workshops in summer?", "Special workshops on emerging technologies are often offered."),
    ("What about CS career services?", "Career services helps with tech internship and job placements."),
    ("Can I join CS clubs in summer?", "CS student organizations continue with reduced summer activities."),
    ("Is there technical support?", "IT support for CS software and systems continues through summer."),
    ("Are CS study groups available?", "Yes, but they're typically smaller during summer semester.")
]

# Prepare the vectorizer
questions = [q for q, a in qa_pairs]
vectorizer = TfidfVectorizer().fit(questions)
question_vectors = vectorizer.transform(questions)

def get_summer_response(user_question):
    user_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vector, question_vectors)
    best_match_index = np.argmax(similarities)
    best_score = similarities[0, best_match_index]

    if best_score < 0.5:
        return "Hmm, I’m not sure about that. Could you rephrase or ask something else related to summer semester or training?"
    return qa_pairs[best_match_index][1]

def is_exit_phrase(user_input):
    exit_phrases = ["goodbye", "bye", "thanks", "thank you", "exit", "that's all"]
    return user_input.strip().lower() in exit_phrases

def run_chatbot():
    print("Hi there! I'm your Summer Assistant Bot. Ask me anything about summer training or summer semester.")
    while True:
        user_input = input("You: ")
        if is_exit_phrase(user_input):
            print("Bot: You're welcome! Good luck with your summer plans ")
            break
        response = get_summer_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    run_chatbot()
