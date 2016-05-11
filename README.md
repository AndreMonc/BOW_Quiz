# PopART_Xtreme.py



##Introduction
This is a python program written by Glaucia Del-Rio, Marco Rego, and Andre Moncrieff 
that aims to increase the general utility of haplotype networks to researchers. 
Haplotype networks are commonly used to represent population level genetic relatedness 
between individuals, and they are easy to generate to using the freely available program 
PopART. The networks produced, however, are often cumbersome to interpret. For instance, 
labels for individuals in the haplotype network are strictly based on the sequence label 
in the Nexus file passed to PopART. Thus, full locality information, morphological traits, 
or other descriptive information must often be consulted in conjunction with the 
haplotype network in order to make a meaningful interpretation. 

Our efforts to improve the utility of haplotype networks to researchers have resulted in
the following three specific contributions via PopART_Xtreme.py:

1. User can provide additional text that will appear in the labels for individuals in the 
haplotype network.
2. User can provide coordinates for localities such that a color-coded map is 
generated alongside the haplotype network.
3. Clutter is kept to a minimum by introducing a mouseover effect such that labels only 
appear when the user hovers over a given haplotype circle. (*Note: such a mouseover effect 
is already available within PopART, but this functionality is not preserved in saved 
haplotype network files. We were required to construct our own mouseover effect 
function to work with the user-customized labels.*)



##Software Requirements
- Python 3. We recommend the Anaconda package of Python 3.5 downloadable for free [here](https://www.continuum.io/downloads).
- PopART. Downloadable for free [here](http://popart.otago.ac.nz/downloads.shtml).
- Latest version of Bokeh. More information on how to download for free [here](http://bokeh.pydata.org/en/latest/docs/installation.html).



##Instructions Step-by-Step
#####Before running PopART_Xtreme.py
- Select a Nexus alignment file for which you would like to produce a haplotype network.
- Open PopART.
- Import your Nexus files into PopART (*Click on "nex" icon at top left of pane*).
- Create network of choice (Network --> *your network of choice*). (*Note: Ancestral parsimony
networks require a trees block in your Nexus file*).
- Optional: for cleaner final product manually move all labels over center of haplotypes.
- Export the network as a Scalable Vector Graphic file (File --> Export graphics --> *Save as .svg*).
- Save log file (Statistics --> Identical sequences --> Yes).


#####User input file
- Open a new .txt file.
- Use tab-delimited format.
- Insert the following four column headers: "Lat", "Long", "Sequence", "Locality".
- Use decimal format for Lat and Long when adding rows.
- User may add columns (no more than 3 recommended) with additional information to be 
displayed as haplotype network labels. 
- Insert any string for sequence and locality.
- Save file.


#####Running program on command line
- Place PopART_Xtreme.py, and the .txt, .svg, and .log files into the same directory.
- Command line setup:
`python PopART_Xtreme.py --SVG some_name.svg --LOG some_name.log --TEXT some_name.txt
--OUT some_name.html
- Press enter and wait for two html files to appear in the working directory: 1) the 
map_plot.html file and 2) the some_name.html that contains the haplotype network
and associated map.


#####Viewing
- Open the new some_name.html file in your web browser of choice.
- Hover over circles in the haplotype network and map to see your input information.



##Acknowledgements
- Thanks to Peter Collingridge for some carefully crafted tutorials on the [tooltip 
function](http://www.petercollingridge.co.uk/interactive-svg-components/tooltip).
- Thanks to Brant Faircloth for answering various questions regarding this project.









 








