# valueIterationAgents.py
# -----------------------
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


import mdp, util
import numpy as np

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        "Use mdp.getStates to get number of states, this can then be used to determine length of each vector Vk"
        "Run outer for loop for 'iteration' number of times"
        "Run inner for loop over each state i.e. length of vector Vk"
        "Maintain two vectors Vk and Vk-1. Update Vk using Vk-1, then replace Vk-1 with Vk"
        "Initialize Vk & Vk_1 (Vk-1) to self.values"

        numStates = len(mdp.getStates())
        Vk   = self.values.copy()
        Vk_1 = self.values.copy()

        for i in range(iterations):
            Vk_1 = Vk.copy() #old Vk is new Vk-1
            allStates = mdp.getStates()

            for j in range(numStates):
                currState = allStates[j]

                if self.mdp.isTerminal(currState)==False:
                    Actions = self.mdp.getPossibleActions(currState)#get possile actions in state
                    Vmax = float("-inf")

                    for currAction in Actions:
                        succStateandProbs = self.mdp.getTransitionStatesAndProbs(currState,currAction) #get successor states and their probabilities from (state, action)
                        Q_sa = 0 #Q value of (currState,currAction) pair

                        for succState,succStateProb in succStateandProbs:
                            Q_sa += succStateProb*(self.mdp.getReward(currState,currAction,succState) + (discount*Vk_1[succState])) #Bellman update

                        #finding the max Q-value
                        if Q_sa>Vmax:
                            Vmax = Q_sa

                    Vk[currState] = Vmax

                else:
                    Actions = self.mdp.getPossibleActions(currState)#get possile actions in state

                    for currAction in Actions:
                        succStateandProbs = self.mdp.getTransitionStatesAndProbs(currState,currAction) #get successor states and their probabilities from (state, action)
                        Q_sa = 0 #Q value of (currState,currAction) pair

                        for succState,succStateProb in succStateandProbs:
                            Q_sa += succStateProb*(self.mdp.getReward(currState,currAction,succState) + (discount*Vk_1[succState])) #Bellman update
                        Vk[currState] = Q_sa


            self.values = Vk


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        currState  = state
        currAction = action
        succStateandProbs = self.mdp.getTransitionStatesAndProbs(currState,currAction) #get successor states and their probabilities from (state, action)
        Q_sa = 0 #Q_sa is Q value of (currState,currAction) pair

        for succState,succStateProb in succStateandProbs:
            Q_sa += succStateProb*(self.mdp.getReward(currState,currAction,succState) + (self.discount*self.values[succState])) #Bellman update

        return Q_sa

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        currState = state
        Actions = self.mdp.getPossibleActions(currState)#get possile actions in state
        Qmax = float("-inf")

        if self.mdp.isTerminal(currState)==False:
            optAction = Actions[0]
            Qmax = self.getQValue(currState, optAction)
            for currAction in Actions:
                if self.getQValue(currState,currAction)>Qmax:
                    Qmax = self.getQValue(currState,currAction)
                    optAction = currAction
            return optAction

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
