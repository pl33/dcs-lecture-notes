[![DOI](https://zenodo.org/badge/266426406.svg)](https://zenodo.org/doi/10.5281/zenodo.10419285)

# Digital Communication Systems

Lecture notes of the course Digital Communication Systems at the
Otto-von-Guericke-University Magdeburg.

## Content of the Lecture Notes

This repository contains the LaTeX sources of:

- the lecture notes
- exercises

Furthermore, programming exercises and their model solutions are stored along
with the exercises. The tasks for the programming exercises is part of the
exercise sheet. In the `exercise*/programming/` folder, there is the template
which can be used by the students and the model solution. Furthermore, there
can be a data generation script to produce the required input vectors.

## Building

### Prerequisites

You need th wfollowing software:

- TeX Live distribution (pdfLaTeX + CTAN packages)
- latexmk
- Inkscape
- Git
- Python 3.10+
- GNU Make

It is recommended to use Linux. Windows has not been tested, but should work.
On Windows, please ensure that all required software is accessible via the
PATH variable.

### Building the Book

To build the book, open a terminal and change to the root directory of this
repository. The execute:

```shell
make complete
```

The folder `build/` will be created. The result will be in `build/DCS.pdf`.

### Building Exercise Sheets

To build the exercise sheets, open a terminal and change to the root directory
of this repository. The execute:

```shell
make exercises
```

The folder `build/` will be created. The result will be in
`build/exercise*.pdf`. There will be one `build/exercise*.pdf` file per
`main/exercise*.tex` file.

**Programming Tasks:**

To generate the programming tasks templates and solutions, open a terminal
and change to the root directory of this repository. The execute:

```shell
python package_programming_ex.py
```

The output will be created in:

- `build/programming/Templates*.zip`: Template and input data
- `build/programming/Solutions*.zip`: Model solutions

### Building Single Chapters

In the rara case bulilding single chapters, open a terminal and change to the
root directory of this repository. The execute:

```shell
make chapters
```

The folder `build/` will be created. The result will be in
`build/chapter*.pdf`. There will be one `build/chapter*.pdf` file per
`main/chapter*.tex` file.

## Folder Structure

This repository is structures as follows:

```
ROOT
|-- chapter*/                    One folder per chapter
    |-- content_ch*.tex          LaTeX source of the lecture note chapter
|-- common/                      Title page, imprint, LaTeX header (settings)
|-- exercise*/                   One exercise per chapter
    |-- helpers                  If present, helper software to generate the solutions
    |-- programming              If present, programming exercises templates and model solutions
        |-- datagen*.py          Script to generate the data used in the exercise
        |-- solution*.py         Model solution
        |-- template*.py         Template for the exercise
    |-- exercise*.tex            LaTeX source of the chapter's exercise
|-- main/                        Per each generated PDF output, document settings and content inclusion
    |-- chapter*.tex             Chapter's main file
    |-- DCS.tex                  Main file of the book (all lecture notes chapters and exercises)
    |-- exercise*.tex            Exercise's main file
|-- COPYING                      CreativeCommons BY-SA 4.0 License text
|-- DCS.bib                      BibTex database
|-- gen_vcs_info.sh              Helper script to retrieve the Git commit hash
|-- Makefile                     Makefile with scripted build instructions
|-- NOTICE                       Additional legal notices
|-- package_programming_ex.py    Helper script to package programming exercises
|-- README.md                    This file
```
