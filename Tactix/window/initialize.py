import pygame

flagMap = { "Fullscreen":pygame.FULLSCREEN
          , "DoubleBuffer":pygame.DOUBLEBUF
          , "HWAcceleration":pygame.HWSURFACE
          , "EnableOpenGL":pygame.OPENGL
          , "Resizable":pygame.RESIZABLE
          , "Borderless":pygame.NOFRAME }

def initWindow(title,size,flagsLst=[]):
    """This function intitializes pygame and returns a window with the given title and size."""
    pygame.init()
    flags = 0
    for flg in flagsLst:
        if not flags:
            flags = flagMap[flg]
        else:
            flags = flags | flagMap[flg]
    windowSurf = pygame.display.set_mode(size,flags)
    pygame.display.set_caption(title)
    return windowSurf
