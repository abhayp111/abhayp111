import streamlit as st
from transformers import pipeline
from huggingface_hub import login
import torch
import os # Import os for environment variables check

st.write("--- Debug Info ---")

# Check if secrets.toml is being loaded at all
if hasattr(st, 'secrets'):
    st.write("st.secrets object found.")
    st.write(f"Type of st.secrets: {type(st.secrets)}")
    try:
        # Attempt to print all keys that Streamlit sees
        st.write("Keys found in st.secrets:")
        for key in st.secrets.keys():
            st.write(f"- '{key}'")
            # Try to access and print the value (masked) if it's the HF token
            if key == "HUGGINGFACE_TOKEN":
                st.write(f"  Value: {st.secrets['HUGGINGFACE_TOKEN'][:5]}...") # Print first 5 chars
    except Exception as e:
        st.error(f"Error inspecting st.secrets keys: {e}")
else:
    st.error("st.secrets object NOT found. This is unexpected.")


# Also check environment variables, in case that's interfering or preferred
st.write("--- Environment Variable Check ---")
if "HF_TOKEN" in os.environ:
    st.write("HF_TOKEN environment variable is set.")
    st.write(f"HF_TOKEN value starts with: {os.environ['HF_TOKEN'][:5]}...")
else:
    st.write("HF_TOKEN environment variable is NOT set.")
st.write("--- End Debug Info ---")


# --- Your original code for Hugging Face Authentication ---
if "HUGGINGFACE_TOKEN" in st.secrets:
    try:
        login(token=st.secrets["HUGGINGFACE_TOKEN"])
        st.success("Successfully logged in to Hugging Face!")
    except Exception as e:
        # THIS IS THE ERROR YOU ARE CURRENTLY GETTING
        st.error(f"Failed to log in to Hugging Face: {e}")
        st.info("Please ensure your token is valid and has access to the model on Hugging Face Hub.")
        st.stop()
else:
    st.warning("Hugging Face token (HUGGINGFACE_TOKEN) not found in Streamlit secrets. "
               "Please add it to run gated models.")
    st.info("Instructions: Create .streamlit/secrets.toml in your project root "
            "and add HUGGINGFACE_TOKEN = 'your_token_here'.")
    st.stop()

# --- Rest of your app code (assuming it's after successful login) ---
@st.cache_resource
def load_llm_pipeline():
    try:
        llm_generator = pipeline(
            "text-generation",
            model="mistralai/Mistral-7B-Instruct-v0.2",
            torch_dtype=torch.float16,
            device_map="auto"
        )
        return llm_generator
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.info("Make sure you have accepted the model's terms on Hugging Face Hub.")
        st.stop()

llm_pipeline = load_llm_pipeline()

# ... (rest of your generate_quiz function and Streamlit UI)