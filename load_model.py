# load_model.py

from transformers import AutoModel

# Load the model directly from the Hugging Face Hub
model = AutoModel.from_pretrained("Boomtoknlab/BoomAI")

print("Model loaded successfully!")
