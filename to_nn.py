qs = ["\n".join(q.split("\n")[0:2]) for q in open("__trivia.txt", "r").read().split("\n\n")]

with open("__triviann.txt", "w+") as f:
    for q in qs:
        f.write(q + "\n\n")
        
