from .crop_zero_planes import crop_external_zero_planes
from .non_zero_normalize import NonZeroNormalizeOnMaskedRegion
from .threshold_and_clip import (
    threshold_transform,
    clip_transform,
)
from .normalize_rgb import (
    normalize_by_val_transform,
    normalize_imagenet_transform,
    normalize_standardize_transform,
    normalize_div_by_255_transform,
)

from torchio.transforms import (
    ZNormalization,
)


def positive_voxel_mask(image):
    return image > 0


def nonzero_voxel_mask(image):
    return image != 0


# defining dict for pre-processing - key is the string and the value is the transform object
global_preprocessing_dict = {
    "threshold": threshold_transform,
    "clip": clip_transform,
    "normalize": ZNormalization(),
    "normalize_positive": ZNormalization(masking_method=positive_voxel_mask),
    "normalize_nonZero": ZNormalization(masking_method=nonzero_voxel_mask),
    "normalize_nonZero_masked": NonZeroNormalizeOnMaskedRegion(),
    "crop_external_zero_planes": crop_external_zero_planes,
    "normalize_by_val": normalize_by_val_transform,
    "normalize_imagenet": normalize_imagenet_transform,
    "normalize_standardize": normalize_standardize_transform,
    "normalize_div_by_255": normalize_div_by_255_transform,
}
