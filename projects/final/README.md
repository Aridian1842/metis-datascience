##Final Project  
####*Prescription Drug Abuse in America*  

**Files in this repo:**  
*NSDUH_modeling_and_analysis.ipynb:*  IPython notebook with supervised classification models applied to the NSDUH data.
*visualization/:*  directory containing all files associated with the D3 visualization.
*Metis Final Project - Master.pdf:*  presentation slides given during Metis Career Day, 31 March 2016.  

**Project Description:**  

For my final project I chose to examine prescription drug abuse.  This is a growing epidemic in the U.S. and I wanted to do some exploratory analysis and see what the profile of addiction looks like so we can target prevention and treatment services accordingly.  

I was able to gather data from several sources, with my primary data set consisting of the Centers for Disease Control and Prevention National Vital Statistics System (NVSS), and survey data from the National Survey on Drug Use and Health (NSDUH), the largest annual national and state-wide survey on substance abuse and mental health.  

I used the NVSS data to examine the number of deaths from drug overdoses from 2002-2014, using the applicable International Classification of Disease, Tenth Revision (ICD-10) codes.  To get a better perspective on how this epidemic is spreading throughout the country, I created a D3 visualization showing the drug overdose death by county from 2002-2014.  The colors indicate the age-adjusted death rate per 100,000 people.  Here is a [link to the D3 visualization](http://rawgit.com/jasonsyp/metis-datascience/master/projects/final/visualization/index.html).

Next I wanted to look at the risk factors associated with prescription drug abuse.  For this, I used the NSDUH data.  I had access to two years of data, 2013 and 2014.  The survey data includes over 55,000 rows (respondents) and 3,100 columns (answers) per year.  There is a 930 page codebook describing each of the variables in the data.  While it is a pretty rich data set, it is survey data and subject to the openness of the respondents to answer questions.  There are many blanks and missing values that need to be accounted for, and many of the values are imputed values based on answers to previous questions, so if a respondent didn't answer one question many others as a result are also left blank.  

I centered my analysis of the NSDUH around the survey question: "Have you ever used prescription drugs non-medically?"  In the end I was left with 20 features to examine the answer to that question.  Modeling substance abuse and addiction is  difficult, and the answer the question here is more general in nature, but given the strong addictive properties of prescription drugs, opioids especially, it was a place to start.  I applied various supervised classification algorithms, and based on the results (accuracy, precision and recall) settled on tree-based ensemble methods, particularly gradient boosted trees.  I took the results of the predicted model and extracted feature importance to build a profile of addiction using the expected values from the data set.  

**References:**  
[Centers for Disease Control and Prevention National Vital Statistics System](http://www.cdc.gov/nchs/data_access/vitalstatsonline.htm#Mortality_Multiple)  
[National Survey on Drug Use and Health](https://nsduhweb.rti.org/respweb/homepage.cfm)  
