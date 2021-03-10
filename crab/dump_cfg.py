import FWCore.ParameterSet.Config as cms 

process = cms.Process("Dump")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
#process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
    secondaryFileNames = cms.untracked.vstring()
)

process.out = cms.OutputModule("PoolOutputModule",
  outputCommands = cms.untracked.vstring(
    'drop *',

    'keep PileupSummaryInfos_*_*_*',
    'keep GenEventInfoProduct_*_*_*',
    'keep externalLHEProducer_*_*_*',

    'keep recoGenParticles_*_*_*',
    'keep patPackedGenParticles_*_*_*',
    'keep recoGenJets_*_*_*',
    'keep recoJetFlavourInfoMatchingCollection_*_*_*',
    'keep recoGenMETs_*_*_*',

    'drop *_*_*_Dump',
 ),
 fileName = cms.untracked.string('output_ex1_v2.root'),
)

process.p = cms.Path()

process.outPath = cms.EndPath(process.out)
process.source.fileNames = [
    '/store/mc/RunIIAutumn18MiniAOD/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2',
]

