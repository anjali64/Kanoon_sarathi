from SPARQLWrapper import SPARQLWrapper, JSON , CSV
import pandas as pd
import numpy as np

class get_data:

    def __init__(self):
        # self.sparql = SPARQLWrapper('https://casecrawler.herokuapp.com/kg/sparql')
        self.sparql = SPARQLWrapper('http://localhost:3030/kanoon-sarathi/sparql')
        print("hello")

    def case_judge_name(self,name):
        
        query="""
        PREFIX nyon: <https://w3id.org/def/NyOn#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select ?CaseName where
{
  
  ?participants rdfs:label '""" + name+"""'@en.
  ?case nyon:hasCourtOfficial ?participants;                                                
        nyon:hasCaseName ?CaseName.
} 
        """ 
        print(query)
        self.sparql.setQuery(query)
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        
        judge = []
        for result in results["results"]["bindings"]:
              judge.append( result["CaseName"]["value"])
             
    
        return judge
    
    def all_judges(self):
        
        query="""
        prefix nyon: <https://w3id.org/def/NyOn#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select distinct ?Judges where
{
?case nyon:hasCourtOfficial ?participants.
?participants rdfs:label ?Judges.
}
            """ 
        self.sparql.setQuery(query)
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
       
        all_judgename = []
        for result in results["results"]["bindings"]:
              all_judgename.append( result["Judges"]["value"])
             
    
        return all_judgename

    def all_petitioner(self):
        
        query="""PREFIX nyon: <https://w3id.org/def/NyOn#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select ?petitioner where
{
  ?case nyon:hasParty ?party.
  ?party rdfs:type nyon:Petitioner;
         rdfs:label ?petitioner.
}
            """ 
        self.sparql.setQuery(query)
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
       
        all_petitioner = []
        for result in results["results"]["bindings"]:
              all_petitioner.append( result["petitioner"]["value"])
             
    
        return all_petitioner

    def all_respondent(self):
        
        query="""
        PREFIX nyon: <https://w3id.org/def/NyOn#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select ?petitioner where
{
  ?case nyon:hasParty ?party.
  ?party rdfs:type nyon:Respondent;
         rdfs:label ?petitioner.
}
            """ 
        self.sparql.setQuery(query)
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
       
        all_respondent = []
        for result in results["results"]["bindings"]:
              all_respondent.append( result["petitioner"]["value"])
             
    
        return all_respondent

    def case_petitioner_name(self,name):
        
        query="""
         PREFIX nyon: <https://w3id.org/def/NyOn#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select distinct ?CaseName where
{
  ?party rdfs:type nyon:Petitioner;
         rdfs:label  '""" + name+"""'@en .
  ?case nyon:hasParty ?party;                                            
        nyon:hasCaseName ?CaseName.
}
        """ 
        print(query)
        self.sparql.setQuery(query)
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        
        petitioner_case = []
        for result in results["results"]["bindings"]:
              petitioner_case.append( result["CaseName"]["value"])
             
    
        return petitioner_case

    def case_respondent_name(self,name):
        
        query="""
         PREFIX nyon: <https://w3id.org/def/NyOn#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select distinct ?CaseName where
{
  ?party rdfs:type nyon:Respondent;
         rdfs:label '""" + name+"""'@en .
  ?case nyon:hasParty ?party;                                            
        nyon:hasCaseName ?CaseName.
}
        """ 
        print(query)
        self.sparql.setQuery(query)
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        
        respondent_case = []
        for result in results["results"]["bindings"]:
              respondent_case.append( result["CaseName"]["value"])
             
    
        return respondent_case