# to get Scio r into testing.txt run sed -n '(6000(r-1) + 1),(6000r)p' tex_trivia.txt > testing.txt
# can edit TeX output in ~/manim/manimlib/ ....yml
# manimgl trivia.py Trivia
# multiple choice functionality incomplete

from manimlib import *
import random 
import time
import os
import gc

multiple_choice = False

questions = open("__trivia.txt", "r").read().split("\n\n")
length = len(questions)

'''
with open('__trivia.txt', 'w+') as f:
    for i in range(length):
        f.write(questions[i].split('\n')[0] + "\n" +
                questions[i].split('\n')[1] + "\n" +
                str(i) + "\n\n")
'''

def get_number():
    random.seed(time.perf_counter())
    index = random.randint(0, length - 1)
    if "Greek root" in questions[index]: # or (not "$" in questions[index]):
        return get_number()
    print("\n\n" + questions[index].split('\n')[0] + "\n" + questions[index].split('\n')[1] + "\n" + str(index) + "\n\n")
    return index

def get_question():
    index = int(get_number())
    ret = questions[index].split("\n")
    ret[2] = int(ret[2])
    return ret

def get_other_choices(index):
    random.seed(time.perf_counter())
    place_correct = random.randint(0, 3)
    choices = [length] * 4
    for i in range(0,4):
        if i == place_correct:
            choices[i] = index
        else:
            random.seed(time.perf_counter())
            new = random.randint(0, length - 1)
            while new == index or new in choices:
                random.seed(time.perf_counter())
                new = random.randint(0, length - 1)
            choices[i] = new
    return choices

def answer_from(index):
    return questions[index].split("\n")[1]
    
class Trivia(Scene):

    def on_mouse_press(self, point, button, mods):
        if (self.active):
            return
        if (self.i == 0):
            self.active = True
            
            try:
                self.image = ImageMobject(f"./images/{self.question[2]}").scale(1.5)
                self.image.fade(0.7)
                if multiple_choice:
                    self.play(FadeIn(self.image), FadeIn(self.prompt), FadeIn(self.vchoices), run_time = 0.5)
                else:
                    self.play(FadeIn(self.image), FadeIn(self.prompt), run_time = 0.5)
            except:
                if multiple_choice:
                    self.play(FadeIn(self.prompt), FadeIn(self.vchoices), run_time = 0.5)
                else:
                    self.play(FadeIn(self.prompt), run_time = 0.5)
                
            self.i += 1
            self.active = False
        elif (self.i % 2):
            self.active = True
            if multiple_choice:
                self.play(FadeOut(self.prompt), FadeOut(self.vchoices), run_time = 0.5)
            else:
                self.play(FadeOut(self.prompt), run_time = 0.5)
            #self.ans = TexText(r"\textbf{" + self.question[1] + r"}").scale(0.8) # no color = BLUE
            self.ans = TexText(self.question[1]).scale(0.8)
            self.length = len(self.question[1])
            
            self.play(FadeIn(self.ans), run_time = 0.5)
            self.length = len(self.question[1])
            #self.question[2] += 1
            #self.question[0] = questions[self.question[2]].split("\n")[0]
            #self.question[1] = questions[self.question[2]].split("\n")[1]
            #self.question = get_question() too early for image fadeout detection. above worked because try: ImageMobject( . . . had index -1
            self.i += 1
            self.active = False
        else: 
            self.active = True
            try:
                ImageMobject(f"./images/{self.question[2]}").scale(1.5)
                self.play(FadeOut(self.ans), FadeOut(self.guess_obj), FadeOut(self.image), run_time = 0.5)
            except:
                self.play(FadeOut(self.ans), FadeOut(self.guess_obj), run_time = 0.5)
            self.question = get_question()
            self.guess_obj = Text("", color = RED).scale(0.8)
            self.length = len(self.question[0])
            self.prompt = TexText(self.question[0]).scale(0.8)
            
            if multiple_choice:
                self.choices = get_other_choices(self.question[2])
                '''
                self.choice_a = TexText(answer_from(self.choices[0])).scale(0.5)
                self.choice_b = TexText(answer_from(self.choices[1])).scale(0.5)
                self.choice_c = TexText(answer_from(self.choices[2])).scale(0.5)
                self.choice_d = TexText(answer_from(self.choices[3])).scale(0.5)
                self.vchoices = VGroup() + self.choice_a + self.choice_b + self.choice_c + self.choice_d
                self.vchoices.arrange(DOWN, center = False, aligned_edge = LEFT)  
                '''
                self.vchoices = TexText(r"\begin{align*} &\textrm{" + answer_from(self.choices[0]) + r"}\\ &\textrm{" +
                                    answer_from(self.choices[1]) + r"}\\ &\textrm{" +
                                    answer_from(self.choices[2]) + r"}\\ &\textrm{" +
                                    answer_from(self.choices[3]) + r"}\end{align*}").scale(0.5)
                self.vchoices.next_to(self.prompt, DOWN)
                self.vchoices.shift(LEFT)

            try:
                self.image = ImageMobject(f"./images/{self.question[2]}").scale(1.5)
                self.image.fade(0.7)
                if multiple_choice:
                    self.play(FadeIn(self.image), FadeIn(self.prompt), FadeIn(self.vchoices), run_time = 0.5)
                else:
                    self.play(FadeIn(self.image), FadeIn(self.prompt), run_time = 0.5)
            except:
                if multiple_choice:
                    self.play(FadeIn(self.prompt), FadeIn(self.vchoices), run_time = 0.5)
                else:
                    self.play(FadeIn(self.prompt), run_time = 0.5)
                
                
            self.i += 1
            self.active = False

    def on_key_press(self, symbol, modifiers):
        if (symbol == 65505): # shift
            self.shift = True

    def on_key_release(self, symbol, modifiers):
        if (self.active):
            return
        '''
        if (self.guess_on):
            if (symbol == 65293): # enter
                self.guess_on = False
                self.guess = ""
                self.active = True
                self.play(FadeOut(self.prompt), run_time = 0.5)
                self.ans = TexText(self.question[1], color = BLUE).scale(0.8)
                self.length = len(self.question[1])
                self.play(self.guess_obj.animate.next_to(self.ans, DOWN))
                self.play(FadeIn(self.ans))
                self.length = len(self.question[1])
                self.question = get_question()
                self.i += 1
                self.active = False
                return

            if (symbol == 65288): # backspace
                self.guess = self.guess[:-1]
                self.guess_obj.become(Text(self.guess, color = RED).scale(0.8).next_to(self.prompt, DOWN))
                return

            if (symbol == 65505): # shift
                self.shift = False
                return

            if (self.shift and symbol >= ord('a') and symbol <= ord('z')):
                self.guess += chr(symbol - ord('a') + ord('A'))
            else:
                self.guess += chr(symbol)

            self.guess_obj.become(Text(self.guess, color = RED).scale(0.8).next_to(self.prompt, DOWN))
            return
        '''
        if (symbol == 113): # 'q'
            global questions
            del questions
            gc.collect()
            os._exit(1)
        '''
        if (symbol == 103): # 'g'
            if (self.i % 2 and not self.active):
                self.guess_on = True
                self.guess_obj = Text("", color = RED).scale(0.8)
                self.guess_obj.next_to(self.prompt, DOWN)
                self.add(self.guess_obj)
        '''

        # if (symbol == 110): # 'n'
        # if (symbol == 121): # 'y'

        

    def construct(self):

        self.shift = False

        self.question = get_question()
        #self.question = [questions[2348].split("\n")[0], questions[2348].split("\n")[1], 2348]
        self.length = len(self.question[0])
        self.guess_on = False

        self.guess = ""
        self.guess_obj = Text("")
        self.prompt = TexText(self.question[0]).scale(0.8)
        
        if multiple_choice:
                self.choices = get_other_choices(self.question[2])
                '''
                self.choice_a = TexText(answer_from(self.choices[0])).scale(0.5)
                self.choice_b = TexText(answer_from(self.choices[1])).scale(0.5)
                self.choice_c = TexText(answer_from(self.choices[2])).scale(0.5)
                self.choice_d = TexText(answer_from(self.choices[3])).scale(0.5)
                self.vchoices = VGroup() + self.choice_a + self.choice_b + self.choice_c + self.choice_d
                self.vchoices.arrange(DOWN, center = False, aligned_edge=LEFT)
                '''
                self.vchoices = TexText(r"\begin{align*} &" + answer_from(self.choices[0]) + r"\\ &" +
                                    answer_from(self.choices[1]) + r"\\ &" +
                                    answer_from(self.choices[2]) + r"\\ &" +
                                    answer_from(self.choices[3]) + r"\end{align*}").scale(0.5)
                self.vchoices.next_to(self.prompt, DOWN)
                self.vchoices.shift(LEFT)
            
        self.ans = TexText("")
        
        self.i = 0
        self.active = False
