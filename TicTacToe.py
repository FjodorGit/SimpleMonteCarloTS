#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:42:03 2021

@author: don
"""
import itertools
import numpy as np
import os

class TicTacToe():
    
    def __init__(self,board_size=3):
        self.board_size = board_size
        self.board = np.full((self.board_size,self.board_size), " ")
        self.player_turn = 0
        
    def display_board(self):
        print(self.board,"\n")
        
        
    def make_move(self,x,y):
        if self.board[x][y] == " ":
            if self.player_turn == 0:
                self.board[x][y] = "X"
                self.player_turn = 1
            else:
                self.board[x][y] = "O"
                self.player_turn = 0
        else:
            print("Illegal move")
            
    def check_for_horizontal_win(self):
        for i in range(self.board_size):
            Xe = 0
            Os = 0
            for j in range(self.board_size):
                if self.board[i][j] == "X":
                    Xe += 1
                if self.board[i][j] == "O":
                    Os += 1
            if Xe == 3:
                print("Ende des Spiels. Spieler mit den X hat gewonnen")
                return True, "X"
            
            if Os == 3:
                print("Ende des Spiels. Spieler mit den O hat gewonnen")
                return True, "O"
            
        return False, ""
                
    def check_for_vertical_win(self):
        for i in range(self.board_size):
            Xe = 0
            Os = 0
            for j in range(self.board_size):
                if self.board[j][i] == "X":
                    Xe += 1
                if self.board[j][i] == "O":
                    Os += 1
            if Xe == 3:
                print("Ende des Spiels. Spieler mit den X hat gewonnen")
                return True, "X"
            
            if Os == 3:
                print("Ende des Spiels. Spieler mit den O hat gewonnen")
                return True, "O"
            
        return False, ""
                
    def check_for_digonal_win(self):
        if (((self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2])
        or (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]))
        and (self.board[1][1] != " ")):
            print(f"Ende des Spiels. Spieler mit den {self.board[1][1]} hat gewonnen")
    
            return True, f"{self.board[1][1]}"
        else:
            return False, ""
                
    def check_for_end(self):
        diago, winner = self.check_for_digonal_win()
        if winner == "":
            hor, winner = self.check_for_horizontal_win()
        if winner == "": 
            vert, winner = self.check_for_vertical_win()
        
        if diago or hor or vert:
            return True, winner
        
        else:
            leer = 0
            for i in range(self.board_size):
                for j in range(self.board_size):
                    if self.board[i][j] == " ":
                        break
                
                    else:
                        leer += 1
        
            if leer == 9:
                return True, " "
                print("Unentschieden")
            else:
                return False, ""
            
    def restart_game(self):
        self.board = np.full((self.board_size,self.board_size), " ")
        self.player_turn = 0
                