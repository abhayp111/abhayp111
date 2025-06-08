from llm import call_llm
import json

def generate_quiz(subject, num_questions):
    prompt = (
        f"Generate a quiz on the topic '{subject}' with {num_questions} questions. "
        f"For each question, provide a JSON object with keys: 'question', 'options' (a list), and 'answer'. "
        f"Output a JSON array of objects."
    )

    response = call_llm(prompt)

    print(response)

    try:
        quiz_data = json.loads(response)
        print("Raw response from LLM:", response) # Debugging print 
        return quiz_data
    except json.JSONDecodeError:
        # If LLM doesn't return pure JSON, extract JSON from the response
        start = response.find("[")
        end = response.rfind("]") + 1
        try:
            return json.loads(response[start:end])
        except:
            return [{"question": "Failed to parse quiz", "options": [], "answer": "N/A"}]

def my_prompt(prompt):
    prompt = (prompt)

    response = call_llm(prompt)

    print(response)

    return response


