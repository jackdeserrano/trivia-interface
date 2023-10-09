# to get scio r into testing.txt run ./getscio r
# can edit TeX output in ~/manim/manimlib/ ... .yml
# manimgl trivia.py Trivia

# todo: add credits to all photos

from manimlib import *
import random 
import time
import os

questions = open("__trivia.txt", "r").read().split("\n\n")
length = len(questions)

ANIMATION_RUN_TIME = 0.5

# -> Nat
def get_number():
    random.seed(time.perf_counter())
    index = random.randint(0, length - 1)
    return index

# -> (Str Str Nat)
def get_question():
    index = int(get_number())
    returned_question = questions[index].split("\n")

    try:
        returned_question[2] = int(returned_question[2]) #
    except IndexError as e:
        print(returned_question,e)

    try:
        TexText(returned_question[1]).scale(0.8)
    except Exception as e:
        print(f"error at {returned_question[2]}",returned_question[0],e)
        return get_question()

    return returned_question

# Nat -> Str
def answer_from(index):
    return questions[index].split("\n")[1]
    
class Trivia(Scene):

    def on_mouse_press(self, point, button, mods):
        if (self.active):
            return
        
        self.active = True
        if self.on_question == None: # opening state
            try:
                self.image = ImageMobject(f"./images/{self.question[2]}").scale(1.5)
                self.image.fade(0.7)
                self.play(FadeIn(self.image), FadeIn(self.prompt), run_time = ANIMATION_RUN_TIME)
                
            except:
                self.play(FadeIn(self.prompt), run_time = ANIMATION_RUN_TIME)
                
            
            
        elif self.on_question:
            self.play(FadeOut(self.prompt), run_time = ANIMATION_RUN_TIME)
            self.ans = TexText(self.question[1]).scale(0.8)
            self.length = len(self.question[1])
            
            self.play(FadeIn(self.ans), run_time = ANIMATION_RUN_TIME)
            self.length = len(self.question[1])
            
            
        elif not self.on_question: 
            try:
                ImageMobject(f"./images/{self.question[2]}").scale(1.5)
                self.play(FadeOut(self.ans), FadeOut(self.image), run_time = ANIMATION_RUN_TIME)
                
            except:
                self.play(FadeOut(self.ans), run_time = ANIMATION_RUN_TIME)
                
            self.question = get_question()
            self.length = len(self.question[0])
            self.prompt = TexText(self.question[0]).scale(0.8)

            try:
                self.image = ImageMobject(f"./images/{self.question[2]}").scale(1.5)
                self.image.fade(0.7)
                self.play(FadeIn(self.image), FadeIn(self.prompt), run_time = ANIMATION_RUN_TIME)
                
            except:
                self.play(FadeIn(self.prompt), run_time = ANIMATION_RUN_TIME)
                
                
        
        self.on_question = not self.on_question
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
        
        self.on_question = None
        self.active = False

