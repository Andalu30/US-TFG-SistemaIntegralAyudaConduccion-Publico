import numpy as np
import cv2
import matplotlib.pyplot as plt

class VistaTopDown:

    def __init__(self):
        self.vistaTopDown = None
        self.vistaTopDownEditada = None
        self.frontMaskedLines = None
        self.inmediatamenteDelante = None


    def computaVistaTopDown(self, camaraCentral, camaraLatIzq, camaraLatDrch):
        
        #main - 640x480
        #lats - 320x240

        topDownCompleto = np.zeros((1200, 1500, 3), np.uint8)

        #-----Central
        # Transformacion
        src = np.float32([[300, 250], [350, 250], [0, 480],   [640, 480]])
        dst = np.float32([[280, 0],   [370, 0],   [300, 480], [350, 480]])

        M = cv2.getPerspectiveTransform(src, dst)

        topDown = cv2.warpPerspective(camaraCentral, M, (640, 480))

        #cv2.imshow('warpcenter', topDown)
        
        # topDown = cv2.line(topDown, (300, 200), (300,500), (255, 255, 255), 1)
        # topDown = cv2.line(topDown, (325, 450), (325,500), (255, 255, 255), 3)
        # topDown = cv2.line(topDown, (350, 200), (350,500), (255, 255, 255), 1)
        #topDown = cv2.cvtColor(topDown, cv2.COLOR_BGR2GRAY)
        
        #ret, topDown = cv2.threshold(topDown, 155, 255, cv2.THRESH_BINARY)
        topDownCompleto[0:480, 315+50:955+50, :] = topDown



        #Laterales
        camaraLatDrch = cv2.resize(camaraLatDrch, (640, 480))
        camaraLatIzq = cv2.resize(camaraLatIzq, (640, 480))
        camaraLatIzq = cv2.flip(camaraLatIzq, 1)


        ##cv2.imshow('camaraResized', camaraLatDrch)

        src = np.float32([[0, 250], [630, 250],  [0, 480],   [360, 480]])
        dst1 = np.float32([[0, 0],  [600, 0],    [580, 480],   [615, 460]])

        M1 = cv2.getPerspectiveTransform(src, dst1)
        
        WarplatDrch = cv2.warpPerspective(camaraLatDrch, M1, (640, 480))
        Warplatizq = cv2.warpPerspective(camaraLatIzq, M1, (640, 480))

        # Otro mas para que el carril se ajuste
        src2 = np.float32([[0, 0], [0, 480],  [640, 0],   [640, 480]])
        dst2 = np.float32([[0, 0], [320, 480],  [640, 0],   [640, 480]])
        M2 = cv2.getPerspectiveTransform(src2, dst2)

        WarplatDrch = cv2.warpPerspective(WarplatDrch, M2, (640, 480))
        Warplatizq = cv2.warpPerspective(Warplatizq, M2, (640, 480))





        #ret, WarplatDrch = cv2.threshold(WarplatDrch, 155, 255, cv2.THRESH_BINARY)
        #ret, Warplatizq = cv2.threshold(Warplatizq, 155, 255, cv2.THRESH_BINARY)

        WarplatDrch = cv2.rotate(WarplatDrch, cv2.ROTATE_180)

        Warplatizq = cv2.flip(Warplatizq, 1)
        Warplatizq = cv2.rotate(Warplatizq, cv2.ROTATE_180)


        #cv2.imshow('warp2', WarplatDrch)
        #cv2.imshow('warp3', Warplatizq)

        topDownCompleto[580-30:1060-30, 640+25+50:1280+25+50] = WarplatDrch
        topDownCompleto[580-30:1060-30, 0+30:640+30] =  Warplatizq

        #Coche blanco
        #topDownCompleto[480:580, 620+50:660+50] = (255, 255, 255)

        self.vistaTopDown = topDownCompleto[0:875,  370:1000]



        # TopDownEditada
        topdownMasked = self.vistaTopDown.copy()
        topdownMasked = cv2.GaussianBlur(topdownMasked, (3, 3), 0)
        hls = cv2.cvtColor(topdownMasked, cv2.COLOR_RGB2HLS)
        L = hls[:, :, 1]
        mask_blanco = cv2.inRange(L, 130, 255)
        topdownMasked = cv2.bitwise_and(topdownMasked, topdownMasked, mask=mask_blanco)

        front = topdownMasked[200:480, :]

        #gray = cv2.cvtColor(front, cv2.COLOR_BGR2GRAY)
        #gray = cv2.GaussianBlur(gray, (9, 9), 0)

        #lines = cv2.HoughLinesP(gray, 1, np.pi/180,   10,      20, 300)
        # print(type(lines))

        # if lines is not []:
        #     for x1, y1, x2, y2 in lines:
        #         print((x1, y1), (x2, y2))
        #         cv2.line(front, (x1, y1), (x2, y2), (255, 0, 0), 5)
        #         print(".", end="")

        ##cv2.imshow('frontMasked', front)


        inmediatamenteDelante = front[200:, 225:410]
        ##cv2.imshow('inmediatameneteDelante', inmediatamenteDelante)
        self.inmediatamenteDelante = inmediatamenteDelante
        
        self.vistaTopDownEditada = topdownMasked
        self.frontMaskedLines = front


    def getInmediatamentedelante(self):
        return self.inmediatamenteDelante

    def getVistaTopDown(self):
        return self.vistaTopDown

    def getVistaTopDownEditada(self):
        return self.vistaTopDownEditada

    def getFrontMasked(self):
        return self.frontMaskedLines

class marcasCalzada:

    def __init__(self, threshold=0.60):

        self.threshold = threshold

        self.templateDelanteDerecha = cv2.imread('resources/templatesCalzada/DelanteDerecha.png', cv2.IMREAD_GRAYSCALE)
        self.templateDelanteIzq = cv2.imread('resources/templatesCalzada/DelanteIzq.png', cv2.IMREAD_GRAYSCALE)

        self.templateDerecha = cv2.imread('resources/templatesCalzada/Derecha.png', cv2.IMREAD_GRAYSCALE)
        self.templateIzq = cv2.imread('resources/templatesCalzada/Izquierda.png', cv2.IMREAD_GRAYSCALE)

        self.templateCebra = cv2.imread('resources/templatesCalzada/cebra.png', cv2.IMREAD_GRAYSCALE)
        self.templateSTOP = cv2.imread('resources/templatesCalzada/STOP.png', cv2.IMREAD_GRAYSCALE)

        self.marcasCalzada = {}

        self.res = {}


    def analisisMarcasCalzada(self, img):

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        matchsSTOP = cv2.matchTemplate(img, self.templateSTOP, cv2.TM_CCOEFF_NORMED)
        matchsCebra = cv2.matchTemplate(img, self.templateCebra, cv2.TM_CCOEFF_NORMED)

        matchsDelanteDerecha = cv2.matchTemplate(img, self.templateDelanteDerecha, cv2.TM_CCOEFF_NORMED)
        matchsDelanteIzq= cv2.matchTemplate(img, self.templateDelanteIzq, cv2.TM_CCOEFF_NORMED)
        
        matchsIzq = cv2.matchTemplate(img, self.templateIzq, cv2.TM_CCOEFF_NORMED)
        matchsDerecha = cv2.matchTemplate(img, self.templateDerecha, cv2.TM_CCOEFF_NORMED)

        #print(matchsSTOP, matchsCebra, matchsDelanteDerecha, matchsDelanteIzq, matchsIzq, matchsDerecha)


        w, h = 10, 10

        loc = np.where(matchsSTOP >= self.threshold)
        self.marcasCalzada['stop']=loc
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)

        loc = np.where(matchsCebra >= self.threshold)
        self.marcasCalzada['cebra'] = loc
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)

        loc = np.where(matchsDelanteDerecha >= self.threshold)
        self.marcasCalzada['delanteDerecha'] = loc
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)
        
        loc = np.where(matchsDelanteIzq >= self.threshold)
        self.marcasCalzada['delanteIzq'] = loc
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)
        
        loc = np.where(matchsIzq >= self.threshold)
        self.marcasCalzada['izquierda'] = loc
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)
        
        loc = np.where(matchsDerecha >= self.threshold)
        self.marcasCalzada['derecha'] = loc
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)


        #cv2.imshow('Matches', img)


        #---^^Datos raw^^------
        #--..Datos Limpios..----
        
        xStop, _ = self.marcasCalzada['stop']
        if not len(xStop) == 0:
            senyalstop = True
        else:
            senyalstop = False
        self.res['stop'] = senyalstop

        xCebra, _ = self.marcasCalzada['cebra']
        if len(xCebra) > 1:
            pasoCebra = True
        else:
            pasoCebra = False
        self.res['cebra'] = pasoCebra

        izquierda, _ = self.marcasCalzada['izquierda']
        if len(izquierda) > 1:
            senyalizquierda = True
        else:
            senyalizquierda = False
        self.res['senyalizquierda'] = senyalizquierda

        derecha, _ = self.marcasCalzada['derecha']
        if len(derecha) > 1:
            senyalderecha = True
        else:
            senyalderecha = False
        self.res['senyalderecha'] = senyalderecha

        delanteDerecha, _ = self.marcasCalzada['delanteDerecha']
        if len(delanteDerecha) > 1:
            sedelanteDerecha = True
        else:
            sedelanteDerecha = False
        self.res['delanteDerecha'] = sedelanteDerecha

        delanteIzq, _ = self.marcasCalzada['delanteIzq']
        if len(delanteIzq) > 1:
            sedelanteIzq = True
        else:
            sedelanteIzq = False
        self.res['delanteIzq'] = sedelanteIzq

    def getMarcasCalzada(self):
        return self.res

