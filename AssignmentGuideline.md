# Assignment guidelines

Last modified: 05.09.2019
>Note: this guideline can be stayed in your submission.

The assignment delivery will be everything within the top directory **assignment_nr_studentid**. We suggest you to use git to work on your assignment delivery by cloning this assignment delivery template.

## Important identifier

* Your student id should be in the **submitter.csv**.
* The assignment id and your student id should be in the name of the top directory of the assignment delivery
* Self-evaluation: do the self-evaluation of your assignment and put the points of your self-evaluation into **selfgrading.csv**

## Directory structure

* You must make sure that the top directory is named as "assignment_nr_studentid" by replacing "nr" with the assignment number and "studentid" with your student id.
* We have subdirectory:
   - *data*: for describing data. Do not put large dataset into this directory. You can put a small sample of data and/or indicate a public place where the data can be downloaded.
   - *code*: where you can put source code written by you (or source code modified by you)
   - *logs*: where you put logs generated from test programs or service logs that can be used to back up your report
   - *report*: where you put for reports about design, performance, etc.

## Content in the assignment

* No sensitive information should be stored in the assignment delivery (data, source, logs, reports)
* You must guarantee the data regulation w.r.t. all contents in the assignment delivery
* Only your student id should be stored in the delivery: the **submitter.csv** should have only a single line which is your student id.
* Reports have to be written in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* No **BINARY format** for any content (code, data, logs, reports), except figures of your design or performance charts. It means, for example, external libraries for your programs should be automatically downloaded when we compile the code (following your README guide), no report is written in Microsoft/open office or PDF.

## Programming Languages
You must use only **Java, Scala, Javascript/NodeJS, Python or bash scripts**

## Assignment submission

* Make sure your clean your directory before creating a zip file for submission.
* The zip file should **assignment-nr-studentid.zip** which, when unzipped, will be **assignment-nr-studentid** directory.
* The zip file will be submitted into [Mycourses](http://mycourses.aalto.fi)
* All deadlines are hard so make sure you test the submission in advance.
