import FWCore.ParameterSet.Config as cms

from RecoBTag.BTagAnalyzerLite.bTagAnalyzerLiteCommon_cff import *

bTagAnalyzerLite = cms.EDAnalyzer("BTagAnalyzerLite",
    bTagAnalyzerLiteCommon,
    # computers
    svComputer        = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    svComputerFatJets = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    # TagInfos (need to omit the 'TagInfos' part from the label)
    ipTagInfos             = cms.string('pfImpactParameter'),
    svTagInfos             = cms.string('pfInclusiveSecondaryVertexFinder'),
    softPFMuonTagInfos     = cms.string('softPFMuons'),
    softPFElectronTagInfos = cms.string('softPFElectrons'),
    # taggers
    trackCHEBJetTags    = cms.string('pfTrackCountingHighEffBJetTags'),
    trackCNegHEBJetTags = cms.string('pfNegativeTrackCountingHighEffJetTags'),

    trackCHPBJetTags    = cms.string('pfTrackCountingHighPurBJetTags'),
    trackCNegHPBJetTags = cms.string('pfNegativeTrackCountingHighPurJetTags'),

    jetBPBJetTags    = cms.string('pfJetBProbabilityBJetTags'),
    jetBPNegBJetTags = cms.string('pfNegativeOnlyJetBProbabilityJetTags'),
    jetBPPosBJetTags = cms.string('pfPositiveOnlyJetBProbabilityJetTags'),

    jetPBJetTags     = cms.string('pfJetProbabilityBJetTags'),
    jetPNegBJetTags  = cms.string('pfNegativeOnlyJetProbabilityJetTags'),
    jetPPosBJetTags  = cms.string('pfPositiveOnlyJetProbabilityJetTags'),

    simpleSVHighPurBJetTags    = cms.string('pfSimpleSecondaryVertexHighPurBJetTags'),
    simpleSVNegHighPurBJetTags = cms.string('pfNegativeSimpleSecondaryVertexHighPurBJetTags'),
    simpleSVHighEffBJetTags    = cms.string('pfSimpleSecondaryVertexHighEffBJetTags'),
    simpleSVNegHighEffBJetTags = cms.string('pfNegativeSimpleSecondaryVertexHighEffBJetTags'),

    combinedSVBJetTags    = cms.string('pfCombinedSecondaryVertexV2BJetTags'),
    combinedSVPosBJetTags = cms.string('pfPositiveCombinedSecondaryVertexV2BJetTags'),
    combinedSVNegBJetTags = cms.string('pfNegativeCombinedSecondaryVertexV2BJetTags'),

    combinedIVFSVBJetTags    = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    combinedIVFSVPosBJetTags = cms.string('pfPositiveCombinedInclusiveSecondaryVertexV2BJetTags'),
    combinedIVFSVNegBJetTags = cms.string('pfNegativeCombinedInclusiveSecondaryVertexV2BJetTags'),

    softPFMuonBJetTags        = cms.string('softPFMuonBJetTags'),
    softPFMuonNegBJetTags     = cms.string('negativeSoftPFMuonBJetTags'),
    softPFMuonPosBJetTags     = cms.string('positiveSoftPFMuonBJetTags'),

    softPFElectronBJetTags    = cms.string('softPFElectronBJetTags'),
    softPFElectronNegBJetTags = cms.string('negativeSoftPFElectronBJetTags'),
    softPFElectronPosBJetTags = cms.string('positiveSoftPFElectronBJetTags')
)
