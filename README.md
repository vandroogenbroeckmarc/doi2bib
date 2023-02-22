# doibib : yet another tool to generate a BiBTeX entry based on a DOI

## Features of this package:
- corrects misformed crossref fields given a DOI.
- replaces keys (IDs) by a key nomenclature containing the first author's name, the year of publication, and the first word(s) of the title. 
- substitutes journal/proceedings names by a _STRING_ macro if available, and suggests a short abbreviation otherwise.
- transforms unicode characters (utf-8) into ASCII 7 bits characters.
- handles capitalized letters in the title (whenever possible).
- guesses page numbers automatically when the web page mentions it or when the PDF is publicly available.
- offers the possibility to switch from long names to short names (for journal or proceedings that have a _STRING_ macro).
- works for many publishers, including preprints (arXiv, PsyArXiv, bioRxiv).

## Examples on how to use it 

> doi2bib 10.1109/TIP.2010.2101613  _(simple usage)_ <br>
> doi2bib -v 10.1109/CVPR42600.2020.01314  _(simple usage, moderate verbosity)_ <br>
> doi2bib -vv https://doi.org/10.1145/3552437.3558545 _(with the complete URL, verbose mode)_ <br>

## Instructions for installation

### First clone the repository and install the needed python packages

> git clone https://github.com/vandroogenbroeckmarc/doi2bib.git <br>
> cd doi2bib <br>
> pip3 install -r requirements.txt

### Additional features

This "doi2bib" version was initially *tuned* for the scientific domains of electrical engineering and computer sciences, but should work for many other domains as well --if only NIPS and ICLR were using DOIs as well... 
To help improving the consistency of references, there is a list of abbreviations named [abbreviation.bib](bib/abbreviation.bib) (with his companion's file of short abbreviations [abbreviation-short.bib](bib/abbreviation-short.bib)) that will automatically be substituted if detected. 
For that you need to inform doi2bib of the availability of [abbreviation.bib](bib/abbreviation.bib). 

For linux and MacOSX systems, the steps to follow are:

- edit your ".zshrc" ou ".bashrc" file (adapt this to your favorite shell if you use another one; to find out which SHELL you are using, just run _printenv SHELL_ in a terminal).
- add the following line (after adaptation): 
export BIBLIOGRAPHYDIR='/home/me/utilityPath/doi2bib/' 
- copy the bib directory to /home/me/utilityPath/doi2bib/ if this directory is not where you have cloned doi2bib
- start a new terminal and check if your variable has been set correctly by 
> printenv BIBLIOGRAPHYDIR


### If you want to run doi2bib from anywhere

It might be a good idea to add the location of the script into your PATH envrionment variable to run it from anywhere. 
After adding it, do not forget to make the file "executable" by a typical 

> chmod u+x doi2bib 


### Proposal for abbreviations if not found 

Some journals require you to mention journal/conference names in an abbreviated format (or if you just want to compress your list of references to match the publisher's requirements in terms of page numbers...).
Later to use a short abbreviation instead, you only need to replace "abbreviation" by "abbreviation-short" in the bibliography LaTeX entry. 
For example (please note that abbreviation must be the first name in the list!), 
> \bibliography{bib/abbreviation,bib/myrefs}

becomes

> \bibliography{bib/abbreviation-short,bib/myBiBTeXEntries}

If no abbreviation is found in [abbreviation.bib](bib/abbreviation.bib), the doi2bib script will suggest an abbreviated format in the _shortjournalproceedings_ string, in addition to the complete name in the _journal_ or _proceedings_ string. This suggestion follows the LTWA standards and uses the file [abbrev.txt.gz](bib/_abbreviation_misc_/abbrev.txt.gz). 
It is then up to you to decide on how to use this (either keep the suggestion or add it your own versions of the abbreviation/abbrebviation-short pair of files). 
Note however that I will update the two files from time to time.
 
## Some excellent reasons to prefer doi2bib to what google scholar provides

(1) While Google scholar allows to retrieve an acceptable BiBTeX entry, most of the time further manual editing is required. 

- For example, for journal entries, the month field is missing. See for example:
> @article{barnich2010vibe,
> title={ViBe: A universal background subtraction algorithm for video sequences},
> author={Barnich, Olivier and Van Droogenbroeck, Marc},
> journal={IEEE Transactions on Image processing},
> volume={20},
> number={6},
> pages={1709--1724},
> year={2010},
> publisher={IEEE}
> }

- For a conference entry, the month, address (location), and publisher fields are missing. 
> @inproceedings{cioppa2020context,
> title={A context-aware loss function for action spotting in soccer videos},
> author={Cioppa, Anthony and Deliege, Adrien and Giancola, Silvio and Ghanem, Bernard and Droogenbroeck, Marc Van and Gade, Rikke and Moeslund, Thomas B},
> booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
> pages={13126--13136},
> year={2020}
> }

Also: 
- Titles provided by google do not handle capitalized letters properly. For example, “Gaussian” should always be “{Gausssian}” (or “{G}ausssian”). 
- authors lists are truncated, see 
> @inproceedings{giancola2022soccernet,
> title={SoccerNet 2022 Challenges Results},
> author={Giancola, Silvio and Cioppa, Anthony and Deli{\\`e}ge, Adrien and Magera, Floriane and Somers, Vladimir and Kang, Le and Zhou, Xin and Barnich, Olivier and De Vleeschouwer, Christophe and Alahi, Alexandre and others},
> booktitle={Proceedings of the 5th International ACM Workshop on Multimedia Content Analysis in Sports},
> pages={75--86},
> year={2022}
> }
- For axXiv entries, scholar provides 
> @article{deliege2018hitnet,
> title={Hitnet: a neural network with capsules embedded in a hit-or-miss layer, extended with hybrid data augmentation and ghost capsules},
> author={Deliege, Adrien and Cioppa, Anthony and Van Droogenbroeck, Marc},
> journal={arXiv preprint arXiv:1806.06519},
> year={2018}
> }

to be compared to what is given by doi2bib

> @article{Deliege2018HitNet-arxiv,
>	title = {{HitNet}: a neural network with capsules embedded in a {Hit-or-Miss} layer, extended with hybrid data augmentation and ghost capsules},
>	author = {Deli{\\`e}ge, Adrien and Cioppa, Anthony and Van Droogenbroeck, Marc},
>	journal = arxiv,
>	volume = {abs/1806.06519},
>	year = {2018},
>	publisher = {arXiv},
>	eprint = {1806.06519},
>	keywords = {},
>	eprinttype = {arXiv},
>	doi = {10.48550/arXiv.1806.06519},
>	url = {https://doi.org/10.48550/arXiv.1806.06519}
> }


Finally, so useful doi or url fields are useful but not provided by scholar.  

(2) Handling macro strings is not done by "commercial" BiBTeX generators. However, macros help guaranteeing some consistency between references and also allow to replace “long” versions of strings (like "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)") by their shorter versions ("IEEE/CVF Conf. Comput. Vis. and Pattern Recogn. (CVPR)”). 

### Future plans

Obviously, the main plan is to allow a kind-of _pip3 install this_package_. Unfortunately, the doi2bib is already used by another package. So, I still need to find a workaround. I will, so stay tuned.

## Use at your own risks... 

I did my best to limit the amount of manual corrections but, believe me, crossref fields given a DOI are quite often wrongly encoded (even by well-known publishers...). Therefore, there will be mistakes in some BiBTeX entries, although in my daily practice more than 9 out of 10 references are rightly encoded. 
Suggestions for improvement are obviously welcome !  


## Disclaimer 

I have used some initial code (largely modified though) from a github site that I cannot trace back. If you are the person who wrote that code, please let me know and I will give you the proper credit. Last but not least, I am also very grateful to all the kind developers who make their code available and to this extraordinary community! 

Enjoy! 

	Marc Van Droogenbroeck

