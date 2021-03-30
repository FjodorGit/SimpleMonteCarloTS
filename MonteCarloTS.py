#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:54:51 2021

@author: don
"""
import os
import numpy as np
import random
import copy

from TicTacToe import TicTacToe


class MonteCarloTreeSearch():
    
    states_dict = {}
    current_rollout = []
    
    def __init__(self):
        self.ttt = TicTacToe()
        self.state = self.ttt.board
        self.total_runs = 0
        self.player_turn = 0
        
    def possible_moves(self):
        possible_moves = []
        for i in range(self.state.shape[0]):
            for j in range(self.state.shape[0]):
                if self.state[i][j] == " ":
                    possible_moves.append((i,j))
        return possible_moves
        
    def choose_move(self):
        best_move_barrier = 0
        possible_moves = self.possible_moves()
        random.shuffle(possible_moves)
        for move in possible_moves:
            self.ttt.board = np.copy(self.state)
            self.ttt.player_turn = copy.copy(self.player_turn)
            #print("Board state:\n", self.ttt.board,"\n")
            self.ttt.make_move(move[0], move[1])
            #print("Simulating move:\n", self.ttt.board,"\n")
            next_key = np.array2string(self.ttt.board)
            
            if next_key in self.states_dict:
                next_state_value = self.states_dict[next_key][0]/self.states_dict[next_key][1] + \
                    np.sqrt(2*np.log(self.states_dict[next_key][1])/self.total_runs)
            else:
                next_state_value = 0
            
            if next_state_value >= best_move_barrier:
                if next_state_value > 0:
                    print("Found a better than random move: ", move)
                best_move = move
                best_move_barrier = next_state_value
                
        if self.player_turn == 0:
            self.player_turn = 1
        else:
            self.player_turn = 0
            
        return best_move
            
        
    def update_state(self, board):
        self.current_rollout.append(np.array2string(board))
        self.state = board
        
    def update_tree(self,winner):
        for state in self.current_rollout:
            print("X: ", state.count("X"), "  O: ", state.count("O"))
            if state not in self.states_dict:
                self.states_dict.update({state:[0,0]})
            self.states_dict[state][1] += 1
            
            if winner == " ":
                self.states_dict[state][0] += 0.5
            
            if (state.count("X") > state.count("O")) and (winner == "X"):
                self.states_dict[state][0] += 1
                
            if state.count("X") == state.count("O") and winner == "O":
                self.states_dict[state][0] += 1
                
        self.total_runs+=1
        self.current_rollout = []
        self.ttt.restart_game()
        self.state = self.ttt.board
            
            
ttt = TicTacToe()
mcts = MonteCarloTreeSearch()
end = False
for _ in range(10000):
    while end != True:
        move = mcts.choose_move()
        ttt.make_move(move[0], move[1])
        mcts.update_state(ttt.board)
        ttt.display_board()
        end, winner = ttt.check_for_end()
        
    mcts.update_tree(winner)
    #print(mcts.states_dict.values())
    ttt.restart_game()
    end = False
    
    
