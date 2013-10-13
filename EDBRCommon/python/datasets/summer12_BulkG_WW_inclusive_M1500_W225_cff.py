import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    noEventSort = cms.untracked.bool(True),
                    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                    fileNames = cmgFiles
                   )

cmgFiles.extend([
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_10_1_iRN.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_11_1_HSP.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_12_1_7wK.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_13_1_qbj.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_14_1_jwZ.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_15_1_YC5.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_16_1_Odg.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_17_1_QyC.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_18_1_53o.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_19_1_v77.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_1_1_jih.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_20_1_LH1.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_21_1_nZX.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_2_1_Bsq.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_3_1_VRL.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_4_1_v1k.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_5_1_vfe.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_6_1_8rk.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_7_1_9hD.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_8_1_WsK.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_M1500_W225_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_M1500_W225_GENSIM__shuai-BulkG_WW_inclusive_M1500_W225_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_9_1_la2.root',
    ])