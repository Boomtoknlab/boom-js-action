# run_pipeline.py

from transformers import pipeline

# Use a pipeline as a high-level helper
pipe = pipeline("text-generation", model="Boomtoknlab/BoomAI")

# Example usage
prompt = "BoomAI is designed to revolutionize"
output = pipe(prompt, max_length=50)
print(output)
