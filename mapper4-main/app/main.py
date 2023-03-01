# importing module
from pandas import *
import re

#reading CSV file
#creating the proposal links and titles dictionaries using the output
proposal_data = read_csv("data/V0_proposal_links_title_synopsis.csv")
proposal_links = proposal_data['nsf_proposal_links_v0'].tolist()
proposal_titles = proposal_data['title'].tolist()
proposal_link_title_dict =  dict(zip(proposal_links, proposal_titles))


path = "data/Recommendation_output.csv"
data = read_csv(path)
# converting column data to list
names = data['names'].tolist()
links = data['links'].tolist()
nsf_id = data['nsf_id'].tolist()
# Creating name and nsfid pairs
name_id_dictionary = dict(zip(names, nsf_id))
# Creating name and nsf link pairs
name_link_dictionary = dict(zip(names, links))
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return(render_template("matching.html",names = names))
@app.route('/',methods=["POST"])
def getValue():
    it=request.form["inputtext"]
    if it in names:
        # converting the string of nsf ids into list for the given name in the input text
        idslist_for_it = name_id_dictionary[it].split("'")[1::2]
        # length = len.name_id_dictionary[it]
        # converting the string of nsf links into list for the given name in the input text
        linkslist_for_it = name_link_dictionary[it].split("'")[1::2]
        #Extract year from nsf links
        years = []
        for i in range(len(linkslist_for_it)):
            test_string = linkslist_for_it[i]
            spl_word = 'pubs/'
            res=test_string[test_string.find(spl_word)+len(spl_word):test_string.find(spl_word)+len(spl_word)+4]
            years.append(res)
        #Extract titles for the given input text
        proposal_titles_for_it = []
        for i in range(len(linkslist_for_it)):
            proposal_titles_for_it.append(proposal_link_title_dict[linkslist_for_it[i]])
        print(proposal_titles_for_it)
        
        return(render_template("matching.html",name = it,length = len(idslist_for_it),range = range(len(idslist_for_it)),names = names, nsfids = idslist_for_it, nsflinks = linkslist_for_it, nsftitles = proposal_titles_for_it,years = years, itext = it))
   
  