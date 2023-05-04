# pc-crawler
Finds PC members from conference websites. Conferences currently supported are ASE and FSE. Url's provided should be from the `Research Papers` page (e.g. https://2023.esec-fse.org/track/fse-2023-research-papers or https://conf.researchr.org/track/ase-2023/ase-2023-papers) so that the crawler can pick up the right HTML elements. If multiple conferences are submitted, the overlaping PC members between conferences will also be found.
## Install
```bash
conda create -y -n pc-crawler python=3.9 && conda activate pc-crawler
pip install selenium==4.9.0 tqdm==4.65.0 beautifulsoup4==4.12.2 requests
```
## Run
```bash
# specify url with -c (you can chain multiple urls as well) 
# members.txt file will be generated with all pc members as well as overlaps (if more than 1 url)
python crawl.py -c https://2023.esec-fse.org/track/fse-2023-research-papers https://conf.researchr.org/track/ase-2023/ase-2023-papers
```