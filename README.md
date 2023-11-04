# Books and authors' datasets analysis 
**ADM HW2 Group #2\
The aim of this work is to clean and to analyze datasets regarding books and their authors.
## Scritps description
* `mainGroup2.ipynb`: The notebook contains the whole project, from the RQ to the AQ.
  - **RQ**: Data cleaning and exploratory analysis has been performed through pandas and re libraries. We first imported the datasets and transformed into pandas dataframes; We adjusted some dirty data and then started with the questions. \
    All the questions are organized under their name and all the outputs are shown. A brief comment is reported when needed.\
    The functions we defined are stored in a separate file, called *defs.py*, from which the functions are sourced whenever are needed.
  - **CLQ**:
  - **AWS**:Using AWS to run the code, we wrote a code in python that traces the five most common tags in the file list.json. The code prints the table containing those tags and the number of times that each of them occur in the list.json file. After the table, our code shows the time of its execution. When our code was finished, we launched an EC2 instance on AWS and used it to run our code again. All the commands we used to acomplish running the code with EC2 instance are provided in our report that we finished by comparing the running time of our code with and without EC2.
  - **AQ**: 
* `defs.py`: Here are present the functions we defined and used in our analysis, for the sake of clearnes.
* `CommandLine.sh`:

