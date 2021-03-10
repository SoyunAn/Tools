from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = False
config.General.transferOutputs = True
config.General.workArea = 'crab_projects_test_ex2_r'
config.General.requestName = 'test'
config.section_('JobType')
config.JobType.psetName = 'dump_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.allowUndistributedCMSSW = True
config.section_('Data')
#config.Data.inputDataset = '/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'
config.Data.inputDataset = '/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v1/MINIAODSIM'
#config.Data.inputDataset = '/store/mc/RunIIAutumn18MiniAOD/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/20000/CB19DC0C-0088-A046-84D5-D7757A4C806F.root'
#config.Data.inputDataset = '/store/mc/RunIIAutumn18MiniAOD/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/00000/06ACB6E4-D278-F04F-ABB7-DDF6415C6831.root'
config.Data.outputDatasetTag = 'test'
config.Data.unitsPerJob = 1
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.allowNonValidInputDataset = True
config.Data.outLFNDirBase = '/store/user/soan/work/test_ex2_r'
config.section_('Site')
config.Site.storageSite = 'T3_KR_KISTI'
config.section_('User')
config.section_('Debug')
