#!/usr/bin/env python


from tkinter import *

root = Tk()
root.title("CTOOL_BYerror1096")
rDONt = Frame(root)
rDONt.pack(side=BOTTOM)
Ev1 = StringVar()
entry = Entry(root,width=34,textvariable=Ev1).pack()
Ev2 = StringVar()
entry = Entry(root,width=34,textvariable=Ev2).pack()
comb0 = Text(root,height=10,width=39)
comb0.pack(side=RIGHT)

def GO_ON_ERROR1096():
    cGET = Ev1.get()
    cG4T = Ev2.get()

    fileUSER = open(cGET,'r')
    filePASS = open(cG4T,'r')
    fileUSER_PASS = open("error1096_cTOOL.txt",'w')

    USER = fileUSER.read().split("\n")
    PASS = filePASS.read().split("\n")

    for line in USER :

        for l1ne in PASS :

            com = str(line)+":"+str(l1ne)+"\n"
            comb0.insert(END,com)
            fileUSER_PASS.write(com)

                        #comb0.insert(END, ":")
                        #comb0.insert(END, passw)
                        #comb0.insert(END, "\n")
    fileUSER.close()
    filePASS.close()



BUTTON = Button(rDONt,text="start",command=GO_ON_ERROR1096).pack(side=LEFT)
BUTT0N = Button(rDONt,text="Stop").pack(side=LEFT)

root.mainloop()

"""

               z
             z"F"$$.
       -%- . Led$$$$P-
              3$3 F3$%
              " ^  .3""
                 d***$$e.
              r .%     ^"%
              '$$r
               3$$  *$*$$$$$
                '$$. *b'b"$*$.
                  *$. "L^L"b"$-
                   "$b '. L^b^$
                    ^$$bJ  \ b^$ .
                    b *$$$b.\ \ b \
                    *$."$$$$$b.. % %
                    4$$r'$$b *$.%.\ ".
                    ^$$  $$P  "$.'c^c"e
                    4P"  $F%   '$.'c^r*$c
                    $    $      '$.'c^c "$-
                   $%   .$       '$.'L^b
           J$$$$$$$$$$$$$$$$$$     *.JL.b    byERROR109      
"""
