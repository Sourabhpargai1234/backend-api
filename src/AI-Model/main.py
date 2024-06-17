import sys
import json
from transformers import pipeline

# Load the model once at the start
qa = pipeline('question-answering')

def process_request(context, question):
    # Perform question answering
    result = qa(context=context, question=question)
    return result

if __name__ == "__main__":
    while True:
        # Read input from standard input
        input_line = sys.stdin.readline().strip()
        if not input_line:
            continue
        
        # Parse the input JSON
        try:
            data = json.loads(input_line)
            context = data['context']
            question = data['question']
            
            # Process the request
            result = process_request(context, question)
            
            # Print the result as a JSON string
            print(json.dumps(result))
            sys.stdout.flush()
        except Exception as e:
            error_message = {'error': str(e)}
            print(json.dumps(error_message))
            sys.stdout.flush()
