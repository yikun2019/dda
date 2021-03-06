import pytest
import torch

from dda import operations


@pytest.mark.parametrize('op', [operations.ShearX(),
                                operations.ShearY(),
                                operations.TranslateY(),
                                operations.TranslateY(),
                                operations.Rotate(),
                                operations.Invert(),
                                operations.HorizontalFlip(),
                                operations.Invert(),
                                operations.Solarize(),
                                operations.Posterize(),
                                operations.Contrast(),
                                operations.Saturate(),
                                operations.Brightness(),
                                operations.Sharpness(),
                                operations.AutoContrast(),
                                operations.Equalize(),
                                operations.SamplePairing()])
@pytest.mark.parametrize('input', [torch.randint(0, 255, (b, 3, 32, 32), dtype=torch.float32) / 255 for b in [1, 2, 4]])
def test_operations(op, input):
    out = op(input)
    out.mean().backward()
