import gradio as gr
import ollama

# Define a function to interact with the model using the 'chat' method
def generate_response(prompt):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response.message.content  # Extract content from the message


# Create the Gradio interface
iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(label="Enter your question:", lines=2, placeholder="Ask something..."),
    outputs=gr.Textbox(label="Model's Response:", lines=5),
    title="Ask Anything"
)

# Launch the interface
iface.launch()
