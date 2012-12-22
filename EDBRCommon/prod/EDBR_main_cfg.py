import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.helpers import *

### read steering options from cmd file:
from ExoDiBosonResonances.EDBRCommon.cmdLine import options
options.parseArguments()


process = cms.Process("CMG")
###########
# Options #
###########
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents))
###process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.PyReleaseValidation.autoCond import autoCond
#process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )
process.GlobalTag.globaltag = cms.string("START53_V7A::All")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff")


###########
# Input   #
###########


fullname  = "ExoDiBosonResonances.EDBRCommon.datasets." + options.infile
###fullname  = "ExoDiBosonResonances.EDBRCommon.datasets.test_RSGZZ600_cff" 
print 'Importing dataset from '
print fullname
process.load(fullname)
####for synch studies
#process.source.eventsToProcess = cms.untracked.VEventRange(cms.EventRange("166699:715236831"),cms.EventRange("173389:180639524"))
#process.source.eventsToProcess  = cms.untracked.VEventRange(cms.EventRange("1:231104"))



###########
# Output  #
###########
process.load('ExoDiBosonResonances.EDBRCommon.outputModules_cff')
process.outpath = cms.EndPath(process.out)

###################
# JSON Filtering  #
###################
### #only do this for data
if "DATA" in options.mcordata and options.json!="" :
     import PhysicsTools.PythonAnalysis.LumiList as LumiList
     import FWCore.ParameterSet.Types as CfgTypes
     myLumis = LumiList.LumiList(filename = options.json).getCMSSWString().split(',')
     process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
     process.source.lumisToProcess.extend(myLumis)



############
# Event filter    #
############

process.badEventFilter = cms.EDFilter("HLTHighLevel",
                                     TriggerResultsTag =
                                      cms.InputTag("TriggerResults","","PAT"),
                                      HLTPaths =
                                      cms.vstring('primaryVertexFilterPath',
                                                  'noscrapingFilterPath',
                                                  'hcalLaserEventFilterPath',
                                                  'HBHENoiseFilterPath',
    #                                              'totalKinematicsFilterPath' #only for Madgraph MC
                                                  ),
                                      eventSetupPathsKey = cms.string(''),
                                       # how to deal with multiple triggers: True (OR) accept if ANY is true, False
                                      #(AND) accept if ALL are true
                                      andOr = cms.bool(False), 
                                      throw = cms.bool(True)    # throw exception on unknown path names
                                      ) 


###########
# HLT filter
###########

# provide list of HLT paths (or patterns) you want
HLTlistMu  = cms.vstring("HLT_Mu*_Mu*")   # triggers for DoubleMuon PD   
HLTlistEle = cms.vstring("HLT_Ele17_Calo*_Ele8_Calo*") # triggers for DoubleElectron PD

### for SingleElectron and SingleMuon PD, request single lept trigger and
#veto the same triggers used for double ele and DoubleMu PD: in this way
#remove events in both PDs
HLTlistSE = cms.vstring("HLT_Ele80_CaloIdVT_GsfTrkIdT_v1 AND NOT HLT_Ele17_Calo*_Ele8_Calo*") # triggers fro SingleElectron PD
HLTlistSM  = cms.vstring("HLT_Mu40_* AND NOT HLT_Mu*_Mu*")

process.hltHighLevelEle = cms.EDFilter("HLTHighLevel",
                                       TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                       HLTPaths = cms.vstring(HLTlistEle),
                                       eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                                       andOr = cms.bool(True),  # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
                                       throw = cms.bool(True)    # throw exception on unknown path names
                                       )
process.hltHighLevelMu = cms.EDFilter("HLTHighLevel",
                                       TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                       HLTPaths = cms.vstring(HLTlistMu),
                                       eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                                       andOr = cms.bool(True),   # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
                                       throw = cms.bool(True)    # throw exception on unknown path names
   )
process.hltHighLevelSM = cms.EDFilter("HLTHighLevel",
                                       TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                       HLTPaths = cms.vstring(HLTlistSM),
                                       eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                                       andOr = cms.bool(True),   # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
                                       throw = cms.bool(True)    # throw exception on unknown path names
   )

process.hltHighLevelSE = cms.EDFilter("HLTHighLevel",
                                       TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                       HLTPaths = cms.vstring(HLTlistSE),
                                       eventSetupPathsKey = cms.string(''),
                                       andOr = cms.bool(True),
                                       throw = cms.bool(True) 
                                      )

### add them to event filter
process.eventFilterSequence = cms.Sequence(process.badEventFilter)
if options.mcordata == "DATAELE" :
     process.eventFilterSequence +=process.hltHighLevelEle
if options.mcordata == "DATASE" :
     process.eventFilterSequence +=process.hltHighLevelSE
if options.mcordata == "DATAMU" :
     process.eventFilterSequence +=process.hltHighLevelMu
if options.mcordata == "DATASM" :
     process.eventFilterSequence +=process.hltHighLevelSM

###################################################################
# Ele Sequence: select electrons and build di-electrons from them #
###################################################################
              
process.load('ExoDiBosonResonances.EDBRElectron.electron_cff')
process.load('ExoDiBosonResonances.EDBRElectron.diElectron_cff')
process.load('ExoDiBosonResonances.EDBRElectron.skims.selEventsElectron_cfi')
process.load('ExoDiBosonResonances.EDBRElectron.skims.selEventsZ_cff')


process.analysisSequenceElectrons = cms.Sequence(
    process.eleSequence +
    process.selectedElectronSequence +
    process.diElectronSequence +
    process.selectedZSequence
    )

##############
# PU weights #
##############
process.load('ExoDiBosonResonances.EDBRCommon.PUweights_cff')
## process.PUWeights.filenameData=cms.FileInPath("ExoDiBosonResonances/EDBRCommon/data/Pileup_2011_to_173692_LPLumiScale_NEW.root")
## process.PUWeights.filenameMC=cms.FileInPath("ExoDiBosonResonances/EDBRCommon/data/Pileup_2011_MC_Oct2011_35bins.root")

process.eleSequence.insert(0,process.PUseq)


############################################################
# Muon Sequence: select muons and build di-muons from them #
############################################################
              
process.load('ExoDiBosonResonances.EDBRMuon.muon_cff')
process.load('ExoDiBosonResonances.EDBRMuon.diMuon_cff')
process.load('ExoDiBosonResonances.EDBRMuon.skims.selEventsMuon_cfi')
process.load('ExoDiBosonResonances.EDBRMuon.skims.selEventsZ_cff')


process.analysisSequenceMuons = cms.Sequence(
    process.muonSequence +
    process.selectedMuonSequence +
    process.diMuonSequence +
    process.selectedZMMSequence
    )
if not ( options.lepton == "both" or options.lepton == "ele"): #only muon
     process.muonSequence.insert(0,process.PUseq)

###################################################################
# Jet Sequence: select jets and build di-jets from them           #
###################################################################
 
process.load('ExoDiBosonResonances.EDBRCommon.jet_cff')
process.load('ExoDiBosonResonances.EDBRCommon.factories.cmgDiJet_cfi')
process.load('ExoDiBosonResonances.EDBRCommon.factories.cmgDiJetKinFit_cfi')
process.load('ExoDiBosonResonances.EDBRCommon.skims.selEventsPFJet_cff')
process.load('ExoDiBosonResonances.EDBRCommon.skims.selEventsZjj_cff')

process.analysisSequenceJets = cms.Sequence(
    process.jetSequence +
    process.selectedJetSequence +
    process.diJetSequence +
    process.selectedZjjSequence+
    process.cmgDiJetKinFit
    )

process.analysisSequenceMergedJets = cms.Sequence(
    process.mergedJetSequence +
    process.selectedMergedJetSequence 
    )

###########################################################
# Resonance Sequence: build EXO resonance from Z bosons   #
###########################################################

# build X->ZZ->eejj
process.load('ExoDiBosonResonances.EDBRElectron.resonanceEle_cff')
cloneProcessingSnippet(process,process.edbrSequenceEEJJ, "Ele")
process.analysisSequenceEEJJ = cms.Sequence(
    process.analysisSequenceElectrons +

    process.analysisSequenceJets +
    
    process.edbrSequenceEEJJEle
    )

# build X->ZZ->eej
cloneProcessingSnippet(process,process.edbrSequenceMerged, "Ele")
process.analysisSequenceEEJ = cms.Sequence(
    process.analysisSequenceElectrons +
    process.analysisSequenceMergedJets +
    process.edbrSequenceMergedEle 
    )


# build X->ZZ->mmjj
process.load('ExoDiBosonResonances.EDBRMuon.resonanceMu_cff')
cloneProcessingSnippet(process,process.edbrSequenceMMJJ, "Mu")
process.analysisSequenceMMJJ = cms.Sequence(
    process.analysisSequenceMuons +
    process.analysisSequenceJets +
    process.edbrSequenceMMJJMu
    )

# build X->ZZ->mmj
cloneProcessingSnippet(process,process.edbrSequenceMerged, "Mu")
process.analysisSequenceMMJ = cms.Sequence(
    process.analysisSequenceMuons +
    process.analysisSequenceMergedJets +
    process.edbrSequenceMergedMu 
    )

if ( options.lepton == "both" or options.lepton == "ele"):
     process.preselElePath = cms.Path(process.eventFilterSequence + process.analysisSequenceEEJJ )
     process.preselEleMergedPath = cms.Path(process.eventFilterSequence + process.analysisSequenceEEJ )
     
if ( options.lepton == "both" or options.lepton == "mu"):
     process.preselMuPath = cms.Path(process.eventFilterSequence + process.analysisSequenceMMJJ )
     process.preselMuMergedPath = cms.Path(process.eventFilterSequence + process.analysisSequenceMMJ )