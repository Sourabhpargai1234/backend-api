import os
import sys
from gradientai import Gradient
from gradientai.openapi.client.exceptions import UnauthorizedException
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GRADIENT_ACCESS_TOKEN = os.getenv('GRADIENT_ACCESS_TOKEN')
GRADIENT_WORKSPACE_ID = os.getenv('GRADIENT_WORKSPACE_ID')

#print(f"Access Token: {GRADIENT_ACCESS_TOKEN}")
#print(f"Workspace ID: {GRADIENT_WORKSPACE_ID}")

def main():
    if len(sys.argv) < 2:
        print("No question provided.")
        return

    question = sys.argv[1]

    try:
        with Gradient(access_token=GRADIENT_ACCESS_TOKEN) as gradient:
            base_model = gradient.get_base_model(base_model_slug="nous-hermes2")

            new_model_adapter = base_model.create_model_adapter(
                name="test model 3"
            )
            #print(f"Created model adapter with id {new_model_adapter.id}")
            sample_query = f"### Instruction: {question} \n\n### Response:"
            print(f"Asking: {sample_query}")

            # before fine-tuning
            #completion = new_model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
            #print(f"Generated (before fine-tune): {completion}")

            samples = [
                { "inputs": "### Instruction: What is your branch \n\n### Response: Btech" },
                { "inputs": "### Instruction: Skills ? \n\n### Response: Coding, Development" },
                { "inputs": "### Instruction: Job? \n\n### Response: SDE at google" },
                { "inputs": "### Instruction: What is your branch \n\n### Response: Mechanical Engineering" },
            ]

            # Uncomment for multiple epochs
            # num_epochs = 3
            # for epoch in range(num_epochs):
            #     print(f"Fine-tuning the model, iteration {epoch + 1}")
            #     new_model_adapter.fine_tune(samples=samples)

            new_model_adapter.fine_tune(samples=samples)

            completion = new_model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
            print(f"Generated (after fine-tune): {completion}")

            new_model_adapter.delete()

    except UnauthorizedException as e:
        print("Unauthorized: Check your API key and permissions.")
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
