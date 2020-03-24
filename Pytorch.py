import torch

# ------------------------
# Basic tensor operations
# ------------------------

# 1D Tensors
# ----------

# Construct LongTensor
a = torch.tensor([1, 2, 3, 4])
print(a.type())  # type of Tensor
print(a.dtype)  # type of data within Tensor

# Methods to construct float Tensor
a = torch.tensor([1, 2, 3], dtype=float)  # float64
a = torch.FloatTensor([1, 2, 3])  # float32
a = a.type(torch.FloatTensor)  # transform tensor into float32

# Informative methods
a.size()  # == a.shape
a.ndimension()  # rank

# Transformative methods
a_col = a.view()