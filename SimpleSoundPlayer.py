import pygame
import sys
from pygame import mixer
from tkinter import filedialog
import tkinter
import time
pygame.font.init()
fs = pygame.font.SysFont('Calibri',20)
def fsrender(text):
    text = str(text)
    a = f.render(text,1,(255,255,255))
    return a
def main():
    ds = pygame.display.set_mode((311,390))
    mixer.init()
    playing = False
    pygame.display.set_caption("Simple Sound Player")
    bk = pygame.image.load("Background.png")
    ds.blit(bk,(0,0))
    while True:
        for event in pygame.event.get():
        	if(event.type == pygame.QUIT):
        		sys.exit(0)
        	if(event.type == pygame.KEYDOWN):
        		if(event.key == pygame.k_s):
        			mixer.music.stop()
        			playing = False
        		if(event.key == pygame.K_p):
        			if(playing == True):
        				mixer.music.pause()
        				playing = False
        			elif(playing == False):
        				mixer.music.play()
        				playing = True
        		if(event.key == pygame.K_o):
        			root = tkinter.Tk()
        			fn = filedialog.askopenfilename()
        			root.withdraw()
        			try:
        				mixer.music.load(fn)
        			except Exception:
        				print("Failed to open", fn)
        pygame.display.update()

if __name__ == '__main__':
    main()
    
