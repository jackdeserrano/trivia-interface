# expects new_batch.txt to contain something of the form

"""
[index i at which to start, so the last one is i - 1]

q_i
a_i

q_{i+1}
a_{i+1}

etc.
"""

# otherwise do not expect something sensible or for this to run at all

# the workflow is then:
# create trivia questions
# note the index at which the last batch ended and create new_batch.txt
# run add_batch.py
# to make any edits, do so in __trivia.txt then run to_nn.py

qa_pairs_temp = open("new_batch.txt", "r").read().split("\n\n")

index = int(qa_pairs_temp.pop(0))

with open("__trivia.txt", "a") as __trivia:

    for qa_pair in qa_pairs_temp:
    
        qa_pair_list = qa_pair.split("\n")
        q = qa_pair_list[0]
        try:
            a = qa_pair_list[1]
        except IndexError as e:
            print(e, q)

        __trivia.write(q + "\n")
        __trivia.write(a + "\n")
        __trivia.write(str(index) + "\n\n")

        index += 1

        
