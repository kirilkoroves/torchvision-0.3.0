__version__ = '0.3.0'
git_version = u'cb5bb1eb7cd95ca8fad25f65a84b26261cda7f8e'
from torchvision import _C
if hasattr(_C, 'CUDA_VERSION'):
    cuda = _C.CUDA_VERSION
