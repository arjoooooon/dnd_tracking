import time
import weakref
import math
import random
import tkinter
import sys
import dis
import builtins
from tkinter import *

# Forgive the spaggehti code, I write much better python nowadays

class mother(object):
    def __init__(self):
        self.isDeprecated = False

class char(mother):
    instances = []
    def __init__(self, equipment, basemana, manaincrease, stren, dex, con, intel, wis, cha, hpmax, gp, sp, bp, ep,name=None):
        self.__class__.instances.append(weakref.proxy(self))
        self.name = name
        self.equip = equipment
        self.equip = []
        self.basemana = basemana
        self.manain = manaincrease
        self.str = stren
        self.strmod = int(self.str/2)
        self.dex = dex
        self.dexmod = int(self.dex/2)
        self.con = con
        self.conmod = int(self.con/2)
        self.int= intel
        self.intmod = int(self.int/2)
        self.wis = wis
        self.wismod = int(self.wis/2)
        self.cha = cha
        self.chamod = int(self.cha/2)
        self.gp = gp
        self.sp = sp
        self.bp = bp
        self.ep = ep
        self.hp = hpmax
        self.hpt = self.hp
        self.stat = []
        
    def addstat(self, stat, dmg, rounds):
        stat = stat.upper()
        for i in range(len(self.stat)):
            if self.stat[i] == stat:
                print("Invalid")
                return " "
        self.stat.append([stat, dmg, rounds])
        return True
    def rmvstat(self, stat):
        stat = stat.upper()
        for i in range(len(self.stat)):
            if self.stat[i][0] == stat:
                del self.stat[i]
                return True
        print("Invalid")
        return " "
    def givestats(self):
        for i in range(len(self.stat)):
            print(self.stat[0][0], "dealing", self.stat[0][1], "damage for", self.stat[0][2], "rounds.")
            return " "
    def givehp(self):
        print(self.name, "has", str(self.hpt)+ "/"+str(self.hp), "hp")
        return " "
    def dmg(self, dmg):
        try:
            self.hpt -= dmg
            if self.hpt < 0 - int(self.hp/2):
                self.stat.append({'DEAD':(0, 999)})
                return True
            elif self.hpt < 0:
                print("UNCONSCIOUS, make saving throws")
                return True
            else:
                return True
        except:
            return False
    def heal(self, hp):
        try:
            self.hpt += hp
            if self.hpt > self.hp:
                self.hpt = self.hp
                return True
            return True
        except:
            return False
    def givemod(self):
        print("+"+str(self.strmod), "– Strength Modifier")
        print("+"+str(self.dexmod), "– Dexterity Modifier")
        print("+"+str(self.conmod), "– Constitution Modifier")
        print("+"+str(self.intmod), "– Intelligence Modifier")
        print("+"+str(self.wismod), "– Wisdom Modifier")
        print("+"+str(self.chamod), "– Charisma Modifier")
    def addequip(self, equipment, qty):
        try:
            for i in range(len(self.equip)):
                if self.equip[i][0] == equipment:
                    self.equip[i][1]+=qty
                    return True
            self.equip.append([equipment, qty])
            return True
        except:
            return False
    def remequip(self, equip, qty):
        try:
            for i in range(len(self.equip)):
                if self.equip[i][0] == equip:
                    self.equip[i][1] -= qty
                    if self.equip[i][1] <= 0:
                        del self.equip[i]
                        return True
                    return True
            return False
        except:
            return False
    def modgp(self, gp):
        try:
            temp = self.gp+gp
            if temp < 0:
                print("Invalid transaction")
                return " "
            self.gp = temp
            return True
        except:
            return False
    def modsp(self,sp):
        try:
            temp = self.sp+sp
            if temp < 0:
                print("Invalid transaction")
                return " "
            self.sp = temp
            return True
        except:
            return False
    def modbp(self, bp):
        try:
            temp = self.bp+bp
            if temp < 0:
                print("Invalid transaction")
                return " "
            self.bp = temp
            return True
        except:
            return False
    def modep(self, ep):
        try:
            temp = self.ep+ep
            if temp < 0:
                print("Invalid transaction")
                return " "
            self.ep = temp
            return True
        except:
            return False
    def givemoney(self):
        print (self.gp, "gold pieces")
        print(self.sp, "silver pieces")
        print(self.bp, "bronze pieces")
        print(self.ep, "electrum pieces")
        return " "

class enm(mother):
    instances = []
    def __init__(self, hpmax, name=None):
        self.__class__.instances.append(weakref.proxy(self))
        self.hp = hpmax
        self.hpt = self.hp
        self.equip = []
        self.stat = []
        self.name = name
    def addstat(self, stat, dmg, rounds):
        stat = stat.upper()
        for i in range(len(self.stat)):
            if self.stat[i] == stat:
                print("Invalid")
                return " "
        self.stat.append([stat, dmg, rounds])
        return True
    def rmvstat(self, stat):
        stat = stat.upper()
        for i in range(len(self.stat)):
            if self.stat[i][0] == stat:
                del self.stat[i]
                return True
        print("Invalid")
        return " "
    def givestats(self):
        for i in range(len(self.stat)):
            print(self.stat[0][0], "dealing", self.stat[0][1], "damage for", self.stat[0][2], "rounds.")
    def addequip(self, equipment, qty):
        try:
            for i in range(len(self.equip)):
                if self.equip[i][0] == equipment:
                    self.equip[i][1]+=qty
                    return True
            self.equip.append([equipment, qty])
            return True
        except:
            return False
    def remequip(self, equip, qty):
        try:
            for i in range(len(self.equip)):
                if self.equip[i][0] == equip:
                    self.equip[i][1] -= qty
                    if self.equip[i][1] <= 0:
                        del self.equip[i]
                        return True
                    return True
            return False
        except:
            return False
    def dmg(self, dmg):
        try:
            self.hpt -= dmg
            if self.hpt < 0 - int(self.hp/2):
                self.stat.append({'DEAD':(0, 999)})
                return True
            elif self.hpt < 0:
                print("UNCONSCIOUS, make saving throws")
                return True
            else:
                return True
        except:
            return False
    def heal(self, hp):
        try:
            self.hpt += hp
            if self.hpt > self.hp:
                self.hpt = self.hp
                return True
            return True
        except:
            return False
    def givehp(self):
        print(self.name, "has", str(self.hpt)+ "/"+str(self.hp), "hp")
        return " "

    

def nextround():
    for instance in char.instances:
        if isinstance(instance, char) == False:
            print("Invalid instance")
            return " "
        for i in range(len(instance.stat)):
            instance.dmg(instance.stat[i][1])
            instance.stat[i][2] -=1
            if instance.stat[i][2] <= 0:
                del instance.stat[i]
            instance.givehp()
            try:
                print(instance.stat[i][0], "dealing", instance.stat[i][1], "damage for", instance.stat[0][2], "rounds.")
                print('–––––––––––––––––––––––––––––––––––––––––––––––')
            except:
                pass
    for instance in enm.instances:
        if isinstance(instance, enm) == False:
            print("Invalid instance")
            return " "
        for i in range(len(instance.stat)):
            instance.dmg(instance.stat[i][1])
            instance.stat[i][2] -=1
            if instance.stat[i][2] <= 0:
                del instance.stat[i]
            instance.givehp()
            try:
                print(instance.stat[i][0], "dealing", instance.stat[i][1], "damage for", instance.stat[0][2], "rounds.")
                print('–––––––––––––––––––––––––––––––––––––––––––––––')
            except:
                pass
    return True
