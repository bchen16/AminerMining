Researchers’ Relocation To and From China

China’s thrive has been a heated topic in recent years. While it attracts people’s attention with it’s economical prosperity, the academic strength of China is also thriving. According to the World Economic Forum, China is ranked No.1 in STEM graduates, No.2 in academic paper produced and No.2 in expenditure in research and development. However, besides its promising statistics, academic dishonesty, government instability and bureaucracy have always worried researchers who are seeking a career in a Chinese research institution.
In this project, we would like to find out the pattern of researchers moving to and from China, what research interest the researchers hold, and when they chose to relocate. Further, we would like to find out what correlate with their decision: are there major historical events? Are there any chronic effects? Are the decisions personal or due to economical considerations?
	For our project, we’ll be looking at different approaches multiple researchers employed to utilize the same dataset we use. A demonstration created by Aminer team used the data sets to analyze all the researchers relocating from all over the world; also, it unified researchers in various fields.  We, on the other hand, will examine how the researcher are moving from and to china, and their field distribution.


Problem statement: 
How and why researchers relocated to and from China?

Data Acquisition: 
From dataset provided by AMiner.org, we can select data[1] we need, such as authors, publication year, affiliation at that year from the paper information file: AMiner-Paper( http://arnetminer.org/lab-datasets/aminerdataset/AMiner-Paper.zip), and according research interests filed from author information file: AMiner-Author(http://arnetminer.org/lab-datasets/aminerdataset/AMiner-Author.zip).

Algorithm choices/ideas:
Data Cleaning:
Based on the data from AMiner-Paper, we found out that some of the important attribute values,like affiliation, are missing. After doing the statistical analysis, if the datasets with missing attributes take a large part of whole data, we would use predict the probable affiliation value by using the ‘mean’ value by nearly years’ affiliation the author is at;
if not taking a large part, we just ignore the datasets.

Data Intergration:
We delete the redundant data occur more than once. Then we combine dataset with the same author and affiliation, and predict the time range for the author in an affiliation based on the discrete year value. Finally, we select the authors who have ever belonged to more than one affiliation and the time range in each affiliation. 

Data Processing: 

1.classification(decision tree) 
In this case, for we only have 4 attributes: authors, year, affiliation, and interests, we don’t need to use algorithms such as random forests, decision tree can work well in this case.
We would do classification of the author's research interests filed, generate a larger domain of small fields.

2.hierarchical clustering 
Cluster the differenct-scales domain of their affiliation, like affiliation, province(state), country. Find out the most popular area involved in the immigraiton.   

3.Frequent pattern analysis (FP-Growth)
Find out what characters combine together will cause the remote of researchers，like their interest fileds or working area

4. Linear Regression (Single and Multiple)
Find out correlation between a class of relocation behavior and a potential cause.





Reference:
[1]Jie Tang, Jing Zhang, Limin Yao, Juanzi Li, Li Zhang, and Zhong Su. ArnetMiner: Extraction and Mining of Academic Social Networks. In Proceedings of the Fourteenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (SIGKDD'2008). pp.990-998. [PDF] [Slides] [System] [API]


