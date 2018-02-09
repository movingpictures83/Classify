# Classify
# Language: Python
# Input: NOA (OTU nodes and classifications)
# Output: NOA (OTU nodes and lowest classification)
# Tested with: PluMA 1.0, Python 2.7

PluMA plugin that takes a set of nodes from a NOde Attribute (NOA)
file and classifies them at their lowest level.  The plugin assumes
that full OTU classifications are in the first column of the NOA
file and that they use notation similar to Mothur, i.e. :

k__....p__...

It will then output an NOA file that contains the same OTU
full classifications from the first file in the first column, 
and their lowest level of classification in the second column.
In addition, the plugin provides IDs to OTUs with the exact
same classification, so that they are correctly detected as
different OTUs by any downstream analysis.  These identifiers
start at .01, and count up.
