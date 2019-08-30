
There are 7 python files and 5 gmt files in this directory. 
----------------------------------------------------------------------------------------

Python

All the code written here are purposed to perform some calculation/analysis or to assist with that purpose. 

Some code only show one use case example to avoid repetition, such as plate velocity instead of showing all three result variables.

The codes used to parse and write text files have not been included except for two functions:
- main.py: a parser function used in almost every calculation involving subregion-by-subregion analysis. Utilises GMT format of psmeca denoting areas for easy c&p. 
- automate.py: a parser function for calculation of all subregions in a file

The main.py is a much more integral code compared to the automate.py as it allowed more freedom. As some data collected cannot be easily extracted such as those from the MTTK programme, this leads to difficulty in parsing and writing a whole text file with conjunction to other variables. To achieve both automated parsing and manual parsing would welcome opportunities for human error. Another reason is that some calculations require manual inspection and manipulation, and therefore cannot be automated. Therefore, main.py has a more methodologically consistent approach that minimises human error while efficiently reducing time. 

A step-by-step calculation of all subregions goes like this:
1) The moment tensor summation is first calculated through the moment_summation.py file 
by inputting the bounded subregion coordinates and written into a text file.
2) Each variable is then calculated by inputting the same coordinates through all the functions in the variable_calculation.py and then written into a text file.
3) Repeat (1) and (2) for all subregions. The resulting two text files must have a concise structure with a simple delimiter. I use whitespaces. 
4) The calculated values from (1) and (2) are extracted from their text files and turn into several lists which are then passed into functions in results_calculation.py. The output is then written into a text file. 

Every other file has functionality not innately interwoven with other codes. These are their purpose:
1) geodetic_calculation.py - uses UNAVCO data in text file to calculate for geodetic velocity and strain rates
2) b-value.py - calculates the b-value of a region and the overall study region
3) result_analysis.py - analysis of calculated vs geodetic values and uncertainties 
-----------------------------------------------------------------------------------------

GMT 

The GMT files all show similar code with little changes as it is essentially one main code amended and trimmed down to its specific needs for the plot it makes.

The files shown are all examples of only the California region as to avoid repetition of the same code with subtle changes tailored for other regions. 

Explaining each file:
1) main_map.gmt - draws entire study region, all seismicity and the borders of all subregions
2) Cal_region.gmt - zooms into only the California region with essentially all the features of (1)
3) vel_SA.gmt - plots average calculated and geodetic velocity on each other for comparison
4) vel_big_SA.gmt - plots all geodetic velocity to show overall relative plate movement
5) strain_SA.gmt - plots average calculated principal axes strain rates and geodetic strain rates on each other for comparison







