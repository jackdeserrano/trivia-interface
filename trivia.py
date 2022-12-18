# to get Scio r into testing.txt run sed -n '(8000(r-1) + 1),(8000r)p' tex_trivia.txt > testing.txt
# can edit TeX output in ~/manim/manimlib/ ... .yml
# manimgl trivia.py Trivia

# todo: add credits to all photos

from manimlib import *
import random 
import time
import os

questions = open("__trivia.txt", "r").read().split("\n\n")
length = len(questions)

# -> Nat
def get_number():
    random.seed(time.perf_counter())
    index = random.randint(0, length - 1)
    return index

# -> (Str Str Nat)
def get_question():
    index = int(get_number())
    ret = questions[index].split("\n")
    ret[2] = int(ret[2]) #
    return ret

# Nat -> Str
def answer_from(index):
    return questions[index].split("\n")[1]
    
class Trivia(Scene):

    def on_mouse_press(self, point, button, mods):
        if (self.active):
            return
        
        if (self.state == 0):
            self.active = True
            
            try:
                self.image = ImageMobject(f"./images/{self.question[2]}").scale(1.5)
                self.image.fade(0.7)
                self.play(FadeIn(self.image), FadeIn(self.prompt), run_time = 0.5)
                
            except:
                self.play(FadeIn(self.prompt), run_time = 0.5)
                
            self.state += 1
            self.active = False
            
        elif (self.state % 2):
            self.active = True

            self.play(FadeOut(self.prompt), run_time = 0.5)
            self.ans = TexText(self.question[1]).scale(0.8)
            self.length = len(self.question[1])
            
            self.play(FadeIn(self.ans), run_time = 0.5)
            self.length = len(self.question[1])
            self.state += 1
            self.active = False
            
        else: 
            self.active = True
            
            try:
                ImageMobject(f"./images/{self.question[2]}").scale(1.5)
                self.play(FadeOut(self.ans), FadeOut(self.image), run_time = 0.5)
                
            except:
                self.play(FadeOut(self.ans), run_time = 0.5)
                
            self.question = get_question()
            self.length = len(self.question[0])
            self.prompt = TexText(self.question[0]).scale(0.8)

            try:
                self.image = ImageMobject(f"./images/{self.question[2]}").scale(1.5)
                self.image.fade(0.7)
                self.play(FadeIn(self.image), FadeIn(self.prompt), run_time = 0.5)
                
            except:
                self.play(FadeIn(self.prompt), run_time = 0.5)
                
                
            self.state += 1
            self.active = False


    def on_key_release(self, symbol, modifiers):
        if (self.active):
            return
        if (symbol == 113): # q
            os._exit(1)


    def construct(self):

        self.question = get_question()
        #self.question = [questions[2348].split("\n")[0], questions[2348].split("\n")[1], 2348]
        self.length = len(self.question[0]) 
        self.prompt = TexText(self.question[0]).scale(0.8)
        
        self.state = 0
        self.active = False

