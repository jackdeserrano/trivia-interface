Requires 3b1b [manim](https://github.com/3b1b/manim/tree/master) (say ManimGL 1.6.1).

[scio](https://quizlet.com/jack_deserrano/folders/scio/sets)

```
manimgl trivia.py Trivia
```

Requires you to update `tex_templates.yml` or the appropriate file in the manim directory as follows:
```
default:
  description: ""
  compiler: xelatex
  preamble: |-
    \usepackage [no-math] {fontspec}
    \setmainfont [Script=Greek] {Gentium Plus} 
    \usepackage {mhchem}
    \usepackage {MnSymbol}  
    \usepackage {mathrsfs} 
    \usepackage {tipa} 
    \usepackage {CJKutf8}
    \linespread {1}
```
That is, the latex should be compiled with this preamble in xelatex (lualatex should work too). 
If this doesn't make sense in the modern version of manim then the version of 3b1b's [manim](https://github.com/3b1b/manim/tree/master) live on 9 October 2023 should work (ManimGL 1.6.1).

You may also need to install some of these latex packages.