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
