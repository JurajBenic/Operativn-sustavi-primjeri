import pygame
from scipy.ndimage import gaussian_filter


class GaussianBlur:
    def __init__(self, kernelsize=7):
        self.kernel_size = kernelsize

    def filter(self, srfc, xpos, ypos, width, height):
        src_w, src_h = srfc.get_size()
        xpos = max(0, int(xpos))
        ypos = max(0, int(ypos))
        width = max(1, min(int(width), src_w - xpos))
        height = max(1, min(int(height), src_h - ypos))

        region = pygame.Rect(xpos, ypos, width, height)
        nSrfc = pygame.Surface((width, height))
        pxa = pygame.surfarray.array3d(srfc.subsurface(region))
        blurred = gaussian_filter(pxa, sigma=(self.kernel_size, self.kernel_size, 0))
        pygame.surfarray.blit_array(nSrfc, blurred)
        del pxa
        return nSrfc
