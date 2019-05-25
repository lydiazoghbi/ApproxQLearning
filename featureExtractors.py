# featureExtractors.py
# --------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"Feature extractors for Pacman game states"

from game import Directions, Actions
import util
import math
import numpy as np

class FeatureExtractor:
    def getFeatures(self, state, action):
        """
          Returns a dict from features to counts
          Usually, the count will just be 1.0 for
          indicator functions.
        """
        util.raiseNotDefined()

class IdentityExtractor(FeatureExtractor):
    def getFeatures(self, state, action):
        feats = util.Counter()
        feats[(state,action)] = 1.0
        return feats

class CoordinateExtractor(FeatureExtractor):
    def getFeatures(self, state, action):
        feats = util.Counter()
        feats[state] = 1.0
        feats['x=%d' % state[0]] = 1.0
        feats['y=%d' % state[0]] = 1.0
        feats['action=%s' % action] = 1.0
        return feats


class SimpleExtractor(FeatureExtractor):

    def getFeatures(self, state, action, predict):
        features = util.Counter()
        goal = (5,5)
        features["Distance-from-goal"] = math.sqrt(sum([(a - b) ** 2 for a, b in zip(state, goal)]))/math.sqrt(50)

        if state == (1,5):
            if action == 'north':
                features["TOP"] = 0.1
        elif state == (2,5):
            if action == 'north':
                features["TOP"] = 0.1
        elif state == (3,5):
            if action == 'north':
                features["TOP"] = 0.1
        elif state == (4,5):
            if action == 'north':
                features["TOP"] = 0.1
        elif state == (5,1):
            if action == 'north':
                features["TOP"] = 0.1
        elif state == (2,2):
            if action == 'north':
                features["TOP"] = 0.1
        elif state == (3,2):
            if action == 'north':
                features["TOP"] = 0.1
        else:
            features["TOP"] = 0

        if state == (2,5):
            if action == 'south':
                features["BOT"] = 0.1
        elif state == (3,5):
            if action == 'south':
                features["BOT"] = 0.1
        elif state == (5,4):
            if action == 'south':
                features["BOT"] = 0.1
        elif state == (1,1):
            if action == 'south':
                features["BOT"] = 0.1
        elif state == (2,1):
            if action == 'south':
                features["BOT"] = 0.1
        elif state == (3,1):
            if action == 'south':
                features["BOT"] = 0.1
        elif state == (4,1):
            if action == 'south':
                features["BOT"] = 0.1
        elif state == (5,1):
            if action == 'south':
                features["BOT"] = 0.1
        else:
            features["BOT"] = 0

        if state == (1,1):
            if action == 'west':
                features["LEFT"] = 0.1
        elif state == (1,2):
            if action == 'west':
                features["LEFT"] = 0.1
        elif state == (1,3):
            if action == 'west':
                features["LEFT"] = 0.1
        elif state == (1,4):
            if action == 'west':
                features["LEFT"] = 0.1
        elif state == (1,5):
            if action == 'west':
                features["LEFT"] = 0.1
        elif state == (4,3):
            if action == 'west':
                features["LEFT"] = 0.1
        elif state == (4,4):
            if action == 'west':
                features["LEFT"] = 0.1
        else:
            features["LEFT"] = 0

        if state == (1,3):
            if action == 'east':
                features["RIGHT"] = 0.1
        elif state == (1,4):
            if action == 'east':
                features["RIGHT"] = 0.1
        elif state == (5,1):
            if action == 'east':
                features["RIGHT"] = 0.1
        elif state == (4,2):
            if action == 'east':
                features["RIGHT"] = 0.1
        elif state == (4,3):
            if action == 'east':
                features["RIGHT"] = 0.1
        elif state == (5,4):
            if action == 'east':
                features["RIGHT"] = 0.1
        else:
            features["RIGHT"] = 0

#        if state == (2,5):
#            features["BTW_HOR"] = 0.1
#        elif state == (3,5):
#            features["BTW_HOR"] = 0.1
#        elif state == (5,1):
#            features["BTW_HOR"] = 0.1
#        else:
#            features["BTW_HOR"] = 0

#        if state == (1,3):
#            features["BTW_VER"] = 0.1
#        elif state == (1,4):
#            features["BTW_VER"] = 0.1
#        elif state == (4,3):
#            features["BTW_VER"] = 0.1
#        else:
#            features["BTW_VER"] = 0

        if state == (5,1):
            if action == 'east':
                features["CORNER"] = 0.1
            if action == 'north':
                features["CORNER"] = 0.1
            if action == 'south':
                features["CORNER"] = 0.1
        else:
            features["CORNER"] = 0

        if predict == 'north':
            if action == 'south':
                features["REPEATING_MOVE"] = 0.1
        elif predict == 'south':
            if action == 'north':
                features["REPEATING_MOVE"] = 0.1
        elif predict == 'east':
            if action == 'west':
                features["REPEATING_MOVE"] = 0.1
        elif predict == 'west':
            if action == 'east':
                features["REPEATING_MOVE"] = 0.1

        return features
