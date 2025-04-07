#! /usr/bin/python3
# -*- coding:Utf-8 -*-

import os
import subprocess
import traceback


def compile_CV():
    
    try:
        md5_new = subprocess.check_output(["md5sum", "conferences.bib", 
                                           "publications.bib", 
                                           "assets/CV_Juliette_Monsel.tex", 
                                           "assets/CV_Juliette_Monsel.pdf"]).decode()
        with open("assets/build/.texhash") as f:
            md5_old = f.read()
            
        recompile = md5_new.strip() != md5_old.strip()
        
    except Exception:
        recompile = True
        print(traceback.format_exc())
        
    if recompile:
        print("Compiling CV from CV_Juliette_Monsel.tex")
        os.chdir("assets")
        p = subprocess.Popen(["pdflatex", "-output-directory=build", "CV_Juliette_Monsel.tex"], stdout=subprocess.PIPE)
        try:
            print(p.stdout.read().decode())
        except Exception as err:
            print(err)
        p = subprocess.Popen(["biber", "build/CV_Juliette_Monsel"], stdout=subprocess.PIPE)
        try:
            print(p.stdout.read().decode())
        except Exception as err:
            print(err)
        p = subprocess.Popen(["pdflatex", "-output-directory=build", "CV_Juliette_Monsel.tex"], stdout=subprocess.PIPE)
        try:
            print(p.stdout.read().decode())
        except Exception as err:
            print(err)
        os.rename("build/CV_Juliette_Monsel.pdf", "CV_Juliette_Monsel.pdf")
        os.chdir("..")
        
        md5_new = subprocess.check_output(["md5sum", "conferences.bib", 
                                           "publications.bib", 
                                           "assets/CV_Juliette_Monsel.tex", 
                                           "assets/CV_Juliette_Monsel.pdf"]).decode()
        with open("assets/build/.texhash", "w") as f:
            f.write(md5_new)
            
    else:
        print("CV unchanged, skipping compilation.")


if __name__ == '__main__':
    compile_CV()
