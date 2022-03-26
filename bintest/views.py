from django.shortcuts import render

from bintest.forms import PollingUnitForm
from .models import AnnouncedPuResults, Lga, Party , PollingUnit
from random import randrange


# Create your views here.

def index(request):
    available_poll_units = {}
    for x in AnnouncedPuResults.objects.all():
        uniqueid=  x.polling_unit_uniqueid
        pollunitName = PollingUnit.objects.get(uniqueid = uniqueid)
        if pollunitName.polling_unit_name in available_poll_units.keys():
            print("Already There")
        else:
            available_poll_units[pollunitName.polling_unit_name] = {}
            available_poll_units[pollunitName.polling_unit_name]["data"] = [uniqueid]
    def getTotalVote(uniqueid):
        uid = uniqueid
        obj = AnnouncedPuResults.objects.filter(polling_unit_uniqueid = uid)
        allPartyVotes = []
        for x in obj:
            allPartyVotes.append(int(x.party_score))
        return sum(allPartyVotes)
    TPSV = [] # Total PollUnitS Votes    
    for pollunit in available_poll_units.keys():
        
        result = getTotalVote(uniqueid=available_poll_units[pollunit]["data"][0])
        TPSV.append(result)
        available_poll_units[pollunit]["data"].append(result) 
    STPSV = int(sum(TPSV))
    def getPercent(low: int,high: int) -> int:
        percent = (int(low) * 100)/ high
        return int(percent)
    for pollunit in available_poll_units.keys():
        percent = getPercent(low = available_poll_units[pollunit]["data"][1], high=STPSV)
        available_poll_units[pollunit]["data"].append(percent)
    print(available_poll_units)  
    sort_orders = sorted(available_poll_units.items(), key=lambda x: x[1]["data"][1], reverse=True)  
    print(dict(sort_orders))
    context = {
                "apu": dict(sort_orders),
    }
    return render(request,"index.html",context)

def localGov(request):
    localGovernments = {}
    for lga in Lga.objects.all():
        localGovernments[lga.lga_name] = {}
        localGovernments[lga.lga_name]["id"] = lga.lga_id
    for lg in localGovernments:
        pu = PollingUnit.objects.filter(lga_id = localGovernments[lg]["id"])
        localGovernments[lg]["pu"]=[]
        for x in pu:
            localGovernments[lg]["pu"].append(x.polling_unit_name)
    
    context = {
        "localG": localGovernments
    }
    print(localGovernments)
    return render(request,"page2.html", context= context)

def getResults(request):
    localg = request.GET.__getitem__("LG")
    localGovernments = {}
    for lga in Lga.objects.all():
        localGovernments[lga.lga_name] = {}
        localGovernments[lga.lga_name]["id"] = lga.lga_id
    for lg in localGovernments:
        pu = PollingUnit.objects.filter(lga_id = localGovernments[lg]["id"])

        localGovernments[lg]["pu"]=[]
        for x in pu:
            localGovernments[lg]["pu"].append((x.polling_unit_name,x.uniqueid))
    lgpollunits = localGovernments[localg]
    print(lgpollunits)
    Results = {}
    
    for pu in lgpollunits["pu"]:
        Results[pu[0]] = []
        for x in AnnouncedPuResults.objects.filter(polling_unit_uniqueid =pu[1]):
            Results[pu[0]].append((x.party_abbreviation,x.party_score))
    print(Results)
            
    context = {
        "localG": localGovernments,
        "Select": localg,
        "Result": Results

    }
    return render(request, "page2.html",context,)
        
   
def update(request):
    context ={}
    allParty = []
    for x in Party.objects.all():
        allParty.append(x.partyname)
    context['ap']= allParty
    return render(request, "page3.html", context)

def regORupdate(request):
    party_name = request.GET.__getitem__("pn")
    party_score = request.GET.__getitem__("ps")
    PollUnit = request.GET.__getitem__("pu")
    allParty = []

    for x in Party.objects.all():
        allParty.append(x.partyname)
    
    available_poll_units = {}
    uniqueids = []
    for x in AnnouncedPuResults.objects.all():
        uniqueid=  x.polling_unit_uniqueid
        uniqueids.append(uniqueid)
        pollunitName = PollingUnit.objects.filter(uniqueid = uniqueid)
        for pun in pollunitName:
            if pun.polling_unit_name in available_poll_units.keys():
                print("Already There")
            else:
                available_poll_units[pun.polling_unit_name] = {}
                available_poll_units[pun.polling_unit_name]["id"] = [uniqueid]
    def genuid(uids):
        Val = True
        while Val:
            w = randrange(100)
            if w not in uids:
                Val= False
        return int(w)

        
    if party_name in allParty:
        if PollUnit in available_poll_units.keys():
            AnnouncedPuResults.objects.create(polling_unit_uniqueid = available_poll_units[PollUnit]["id"], party_score = party_score, party_abbreviation = party_name )
        else:
            uid = genuid(uids=uniqueids)
            PollingUnit.objects.create(uniqueid = uid,polling_unit_name = PollUnit )
            AnnouncedPuResults.objects.create( polling_unit_uniqueid = uid ,  party_score = party_score, party_abbreviation = party_name)
        context = {}
        context['ap']= allParty
        context['message'] = "Updated SuccessFully!"
    else:
        
        context = {"err": "Correct Party Not Selected"}

    return render(request, "page3.html", context)