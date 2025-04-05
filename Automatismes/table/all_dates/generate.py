import subprocess
import datetime

def tablepdf(index, date):
    """
    INPUTS : index, non negative integer. Date of pdf is today+index
            date, string date of today+index for filename
    Compiles table4.tex with appended newcommand{\datedelta}{index}.
    Outputs in out/table4_date.pdf.
    """
    
    # COMPILE WITH VARS INPUT  
        
    INPUTS = "\\documentclass[14pt]{extarticle} \\newcommand{\datedelta}{"+str(index)+"}  \\input{table4.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=2nde13_{date}"
    # suppress output
    PARAMETER3 = "-interaction=batchmode"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, PARAMETER3, INPUTS])

    return 0


# isviable returns True is day is viable, False otherwise.
# this is made on a Sunday, and Monday, Tuesday, Friday are viable.
def isviable(index):
    return index%7 in [1, 2, 5]

def datetostring(date):
    return date.strftime('%Y-%m-%d')


if __name__ == "__main__":
    N = 100 # 3/7*100 : 43 viable days
    date = datetime.date.today()
    for index in range(1,N):
        date += datetime.timedelta(days=1)
        
        if not isviable(index):
            continue
        
        datestring = datetostring(date)
        print("Compiling pdf "+datestring)
        tablepdf(index, datestring)













