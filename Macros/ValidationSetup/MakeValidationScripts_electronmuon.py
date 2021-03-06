import os,sys
from functions import *

### dimuon
datasets = ["MuonEG"]
cuts = ["EMuon", "EMuon_BB", "EMuon_dijet","EMuon_IDW","EMuon_noW","EMuon_puW","EMuon_Trigger", "EMuon_SSPreselection"]
IDs = ["POGTightroch_corrected"]

for x in IDs:
    samples_os = ["top","wjets","dylow","dyhigh"]
    if "truthmatch" in x:
        samples_os = ["top","wjets","dylow","dyhigh","nonprompt_DoubleEG"]
                
    for d in datasets:
        
        runfile= open("/home/jalmond/HeavyNeutrino/13TeV/LQAnalyzer_cat/LQanalyzer/Macros/Plotting/Plotting_PhaseSpaces_CtoD/SKTreeValidationDir/run_" + x + "_"+d +".sh","w")
        runfile.write(MakeRunFile(d, cuts,x))
        
        for i in cuts:
            cutfile  = open("/home/jalmond/HeavyNeutrino/13TeV/LQAnalyzer_cat/LQanalyzer/Macros/Plotting/Plotting_PhaseSpaces_CtoD/SKTreeValidationDir/SKTreeValidation"+d+"/dat/hn_cut_"+ x+"_"+ i + ".txt","w")
            cutfile.write(i + x + '\n')
            cutfile.write("END")       
            histfile  = open("/home/jalmond/HeavyNeutrino/13TeV/LQAnalyzer_cat/LQanalyzer/Macros/Plotting/Plotting_PhaseSpaces_CtoD/SKTreeValidationDir/SKTreeValidation"+d+"/dat/hn_histfile.txt","w")
            histfile.write(MakeHistFile())
            configfile = open("/home/jalmond/HeavyNeutrino/13TeV/LQAnalyzer_cat/LQanalyzer/Macros/Plotting/Plotting_PhaseSpaces_CtoD/SKTreeValidationDir/SKTreeValidation"+d+"/Config/hnplots_periodCtoD_"+x + "_"+i+".txt", "w")
            configfile.write(makeConfigFile("/data2/CAT_SKTreeOutput/JobOutPut/jalmond/LQanalyzer//data/output/CAT/SKTreeValidation/periodCtoD/", d ,"hn_histfile.txt","hn_cut_" + x + "_" +i + ".txt", "v7-6-6", samples_os, i+"_"+x))
            
    
