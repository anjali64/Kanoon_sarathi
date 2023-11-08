from django.shortcuts import render, HttpResponse
from Sparql_queries.queries import get_data
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is homepage")
def partyname(request):
    sparqlQueries = get_data()
    
    data = {}
    all_res = sparqlQueries.all_respondent()

    if((request.method=='POST' and request.POST['step'] and request.POST['step'] == '1')):
        partyType=request.POST['partyType']
        if(partyType=='Respondent'):
            all_res = sparqlQueries.all_respondent()
        if(partyType=='Petitioner'):
            all_res = sparqlQueries.all_petitioner()
        return render(request, 'partyname.html', { "all_res": all_res, 'partyType': partyType })

    if(request.method=='POST' and request.POST['step'] and request.POST['step'] == '2'):
        partyName = request.POST['partyName']
        partyType = request.POST['partyType']
        casename = ""
        if(partyType=='Respondent'):
            casename = sparqlQueries.case_respondent_name(partyName)
        if(partyType=='Petitioner'):
            casename = sparqlQueries.case_petitioner_name(partyName)
        data = {
            "name":casename,
            'flag':True,
            'suffix':'Case name',
            'title':'Case Name',
            "all_res": all_res,
            'partyType': partyType
        }

        return render(request,'partyname.html', context = data)
    
    return render(request, 'partyname.html', { 'all_res': all_res })
    
def judge(request):
    sparqlQueries = get_data()
    
    data = {}

    # judges = sparqlQueries.case2_judge_name()
    # print(judges)
    # data = {
    #         "name":judges,
    #         'flag':True,
    #         'suffix':'judges',
    #         'title':'Judge of Case2'
            
    #        }
    
    print("HERE")
    all_jud = sparqlQueries.all_judges()
    
    print("after query HERE")
    
    
    if(request.method=='POST'):
        
        judgename = request.POST['taskOption']
        
        

        
            
        casename = sparqlQueries.case_judge_name(judgename)
        
        data = {
            "name":casename,
            'flag':True,
            'suffix':'Case name',
            'title':'Case Name',
            "all_jud": all_jud
        }

        return render(request,'judge.html', context = data)
     
    return render(request,'judge.html', {"all_jud": all_jud})
    


