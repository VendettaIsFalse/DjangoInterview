from django.shortcuts import render

# Dictionary to store predefined interview questions and answers
QA_DICT = {
    "tell me about yourself": "I am a student passionate about technology and solving problems.",
    "strengths": "I am hardworking, dedicated, and a quick learner.",
    "weakness": "I tend to overthink things sometimes, but I am working on it.",
}

def home(request):
    answer = None
    question = None
    
    if request.method == "POST":
        question = request.POST.get("question", "").strip().lower()
        # Basic string matching with dictionary keys
        answer = QA_DICT.get(question, "Answer not available")
        
    return render(request, "index.html", {"answer": answer, "question": question})
