# doibib : yet another tool to generate a BiBTeX entry based on a DOI

Features of this package:
- corrects misformed crossref fields given a DOI.
- replaces keys (IDs) by a key nomenclature containind the first author'name, the year of publication and the first word(s) of the title. 
- substitutes journal or proceedings names by a _STRING_ macro if available, and suggests a short abbreviation otherwise.
- transform unicode characters into ASCII 7 bits characters.
- handles capitalized letters in the title whenever possible.
- guesses page numbers automatically when the web page mentions it or the PDF is available.
- offers the possibility to switch from long names to short names (for journal or proceedings that have a _STRING_ macro).
- works for many publishers and including preprints (arXiv, PsyArXiv, bioRxiv).

## Examples on how to use it 

> doi2bib 10.1109/TIP.2010.2101613  _(simple usage)_ <br>
> doi2bib -v 10.1109/CVPR42600.2020.01314  _(simple usage, moderate verbosity)_ <br>
> doi2bib -vv https://doi.org/10.48550/arXiv.2210.02365  _(with the complete URL, verbose mode)_ <br>

## Instructions for installation

### First clone the repository and install the needed python packages

> git clone https://github.com/vandroogenbroeckmarc/doi2bib.git <br>
> cd doi2bib <br>
> pip3 install -r requirements.txt

### Additional features

This "doi2bib" version is *tuned* for the scientific domains of electrical engineering and computer sciences, but should work for many other domains as well --if only NIPS and ICLR were using DOIs as well... 
To help improving the consistency of references, there is a list of abbreviations named [abbreviation.bib](bib/abbreviation.bib) (with his companion's file of short abbreviations [abbreviation-short.bib](bib/abbreviation-short.bib)) that will automatically be substituted if detected. 
For that you need to inform doi2bib of the availability of [abbreviation.bib](bib/abbreviation.bib). 

For linux and MacOSX systems, the steps to follow are:

- edit your ".zshrc" file (adapt this to your favorite shell if you use another one; to find out which SHELL you are using, just run _printenv SHELL_ in a terminal).
- add the following line (after adaptation): 
export BIBLIOGRAPHYDIR='/home/me/utilityPath/doi2bib' 
- copy the bib directory to /home/me/utilityPath/doi2bib
- start a new terminal and check if your variable has been set correctly by 
> printenv BIBLIOGRAPHYDIR


### If you want to run doi2bib from anywhere

It might be a good idea to add the location of the script into your PATH envrionment variable to run it from anywhere. 
After adding it, do not forget to make the file "executable" by a typical 

> chmod u+x doi2bib 


### Proposal for abbreviations if not found. 

Some journals require you to mention journal or conference or names in an abbreviated format (or if you just want to compress your list of references to match the publisher's requirements...).
Later to use a short abbreviation instead, it is sufficient to replace "abbreviation" by "abbreviation-short" in the bibliography LaTeX entry. 
For example (please note that abbreviation must be the first name in the list!), 
> \bibliography{bib/abbreviation,bib/myrefs}

becomes

> \bibliography{bib/abbreviationshort,bib/myBiBTeXEntries}

If no abbreviation is found in [abbreviation.bib](bib/abbreviation.bib), the doi2bib script will suggest an abbreviated format in the 'shortjournalproceedings' string, in addition to the complete name in the journal or proceedings string. This suggestion follows the LTWA standards and uses the file [abbrev.txt.gz](bib/_abbreviation_misc_/abbrev.txt.gz). 
It is then up to you to decide on how to use this (either keep the suggestion or add it your own versions of the abbreviation/abbrebviation-short pair of files). 
Note however that I will update the two files from time to time.
 

## Use at your own risks... 

I did my best to limit the amount of manual corrections but, believe me, crossref fields given a DOI are quite often wrongly encoded (even by well-known publishers...). Therefore, they will be mistakes in some BiBTeX entries, although in my daily practice more than 9 out of 10 references are rightly encoded. 
Suggestions for improvements are obviously welcome.  


## Disclaimer 

I have used some initial code (largely modified though) from a github site that I cannot trace back. If you are the person who wrote that code, please let me know and I will give you the proper credit. I am also grateful to all the kind developers who makes their code available and to this extraordinary community! 

Enjoy! 

	Marc Van Droogenbroeck

