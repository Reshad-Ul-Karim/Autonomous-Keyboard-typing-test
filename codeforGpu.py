import torch

# Check if MPS is available
if torch.backends.mps.is_available():
    print("MPS is available on this system!")
else:
    print("MPS is not available on this system.")
print(torch.__version__)