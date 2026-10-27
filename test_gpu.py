import torch

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version (runtime): {torch.version.cuda}")
print(f"GPU count: {torch.cuda.device_count()}")
if torch.cuda.device_count() > 0:
    print(f"GPU name: {torch.cuda.get_device_name(0)}")
    print(f"GPU memory (GB): {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f}")