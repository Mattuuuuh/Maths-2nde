import subprocess
import numpy as  np

def newcommand(current_str, command, value):
    if command in ["\d", "\k"]:
        prefix = "\\renewcommand"
    else:
        prefix = "\\newcommand"
    return current_str+prefix+"{"+command+"}{"+str(value)+"}\n"

def randomize():
    [n, d_over_n, p_over_d, q_over_d] =np.rint(np.random.rand(4)*[10, 15, 10, 10])+[15,10,3,4]

    n=int(n)
    d_over_n=int(d_over_n)
    p_over_d=int(p_over_d)
    q_over_d=int(q_over_d)

    # turn coprime
    gcd = np.gcd(p_over_d, q_over_d)
    p_over_d = int(p_over_d/gcd)
    q_over_d = int(q_over_d/gcd)

    d = d_over_n*n

    # p,q
    p=p_over_d*d
    q=q_over_d*d

    # average k >p, d/n
    k=int(100*(np.random.rand()-.5))

    print(p,q,d_over_n, k)

    return [p,q,d,k,n,d_over_n,p_over_d,q_over_d]


def generate(seed):
    FILE_NAME = f"adr/vars_{seed}.adr"

    CONTENT = newcommand("", "\seed", seed)

    ####### EXERCISE 1

    [p,q,d,k,n,d_over_n,p_over_d,q_over_d] = randomize()

    CONTENT = newcommand(CONTENT,"\p", p)
    CONTENT = newcommand(CONTENT,"\q", q)
    CONTENT = newcommand(CONTENT,"\d", d)
    CONTENT = newcommand(CONTENT,"\k", k)
    CONTENT = newcommand(CONTENT,"\\n", n)
    CONTENT = newcommand(CONTENT,"\\nval", k-d_over_n)
    CONTENT = newcommand(CONTENT,"\kmp", k-p)
    CONTENT = newcommand(CONTENT,"\kpq", k+q)
    CONTENT = newcommand(CONTENT,"\psd", p_over_d)
    CONTENT = newcommand(CONTENT,"\qsd", q_over_d)

    # sols

    b0 = 0
    while((q_over_d*b0 -1) % p_over_d != 0):
        b0+=1

    a0 = int((q_over_d*b0 - 1)/p_over_d)

    CONTENT = newcommand(CONTENT,"\solb", b0+p_over_d)
    CONTENT = newcommand(CONTENT,"\sola", a0+q_over_d)

    CONTENT = newcommand(CONTENT,"\solbZ", b0)
    CONTENT = newcommand(CONTENT,"\solaZ", a0)

    ######### EXERCISE 2

    [p,q,d,k,n,d_over_n,p_over_d,q_over_d] = randomize()

    CONTENT = newcommand(CONTENT,"\pB", p)
    CONTENT = newcommand(CONTENT,"\qB", q)
    CONTENT = newcommand(CONTENT,"\dB", d)
    CONTENT = newcommand(CONTENT,"\kB", k)
    CONTENT = newcommand(CONTENT,"\\nB", n)
    CONTENT = newcommand(CONTENT,"\kmpB", k-p)
    CONTENT = newcommand(CONTENT,"\kpqB", k+q)
    CONTENT = newcommand(CONTENT,"\psdB", p_over_d)
    CONTENT = newcommand(CONTENT,"\qsdB", q_over_d)

    CONTENT = newcommand(CONTENT,"\\nvalB", k-d_over_n + 1)
    CONTENT = newcommand(CONTENT,"\dmnB", d-n)

    ### HISTOGRAM

    Conca = int(np.random.rand()*12)+2
    [EffConca, EffConcb, EffConcc, EffConcd] = np.random.rand(4)*20+3
    EffConca, EffConcb, EffConcc, EffConcd = int(EffConca), int(EffConcb), int(EffConcc), int(EffConcd)

    CONTENT = newcommand(CONTENT, "\CONCa", Conca)
    CONTENT = newcommand(CONTENT, "\CONCb", Conca+1)
    CONTENT = newcommand(CONTENT, "\CONCc", Conca+2)
    CONTENT = newcommand(CONTENT, "\CONCd", Conca+3)
    CONTENT = newcommand(CONTENT, "\EFFCONCa", EffConca)
    CONTENT = newcommand(CONTENT, "\EFFCONCb", EffConcb)
    CONTENT = newcommand(CONTENT, "\EFFCONCc", EffConcc)
    CONTENT = newcommand(CONTENT, "\EFFCONCd", EffConcd)


    [Dispa, Dispd] = np.random.rand(2)*8
    Dispa = int(Dispa)
    Dispd = int(Dispd)+Dispa+6

    [EffDispa, EffDispb, EffDispc, EffDispd, EffDispe] = np.random.rand(5)*20+3
    EffDispa, EffDispb, EffDispc, EffDispd, EffDispe = int(EffDispa), int(EffDispb), int(EffDispc), int(EffDispd), int(EffDispe)

    CONTENT = newcommand(CONTENT, "\DISPa", Dispa)
    CONTENT = newcommand(CONTENT, "\DISPb", Dispa+1)
    CONTENT = newcommand(CONTENT, "\DISPc", Dispa+2)
    CONTENT = newcommand(CONTENT, "\DISPd", Dispd)
    CONTENT = newcommand(CONTENT, "\DISPe", Dispd+1)
    CONTENT = newcommand(CONTENT, "\EFFDISPa", EffDispa)
    CONTENT = newcommand(CONTENT, "\EFFDISPb", EffDispb)
    CONTENT = newcommand(CONTENT, "\EFFDISPc", EffDispc)
    CONTENT = newcommand(CONTENT, "\EFFDISPd", EffDispd)
    CONTENT = newcommand(CONTENT, "\EFFDISPe", EffDispe)


    with open(FILE_NAME, 'w') as file:
        file.write(CONTENT)

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm2.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice for references 
    
    return 0

if __name__=="__main__":

    np.random.seed(42)
    # always the same 15 :)

    for _ in range(15):
        ## SEED ##

        seed = int(np.random.rand() * (2**16 - 1))
        # uncomment to fix seed
        #seed=59583
        np.random.seed(seed)

        generate(seed)

