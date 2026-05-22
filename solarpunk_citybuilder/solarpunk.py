# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:21:55 2026

@author: dylan
"""

'''
societal draw:
    social capital of the community? 
    can be used to influence trading or info exchange with other communities? 
    maybe determines retention rate of citizens? or flux of incoming citizens?
    or just generally visitors?
    im imagining things like: wandering traders or theater troups or scholars
    or artists that have an increasing chance of visiting if there are specific
    societal draws or just generally higher magnitude of social capital
    
    e.g. having an observatory will increase some stat like 'innovation'
         which then increases visits by scholars and likelihood of producing a scholar
    
         having an auditorium or stage will increase 'performance'?
    
'''
class building:
    '''
    generic object? 
    can have a number of attributes 
    e.g. windows, doors, square ft, floors, electrical wiring, plumbing, 
    water, water reuse mechanisms 
    
    can inherit from other classes e.g. fish hatchery
    - in this case, the building would ~become~ a fish hatchery 
   
    once a building has become a specific thing, it can be converted to 
    other types of buildings with dificulty and resources dependent on the 
    current state and converted state, 
    - e.g. easy: turn an aquarium into a fish hatchery
    -      hard: turn an aquarium into a grain cellar
    
    will be made of specific materials, 
    - which would affect the temperature and difficulty of construction,
    - conversion, and destruction
    '''
    def __init__():
        return

class fish_hatchery:
    '''
    materials: netting, wood, sand
    - requires water filtration
    
    convert some land to water source
    or use existing water source, e.g. a pond
    can be created from aquarium
    
    need initial live fish source 
    need continual food source for fish
    
    increases risk of foodborne illness
    increases risk of genetic modification of fish
    
    increases stability of food 
    
    direct conversion: (from) aquarium, aquaponics
    '''
    def __init__():
        return

class aquarium:
    '''
    materials: glass, metal, sand
    - need intial water source
    - requires water filtration
    
    can add fish, coral, rocks, seaplants, trinkets
    - adding decorative things buffs societal draw?
    
    direct conversion: (to) fish hatchery, aquaponics
    
    increases happiness
    increases societal draw
    '''
    def __init__():
        return
    
class aquaponics:
    '''
    materials: glass, metal, ceramics, soil, seeds
    - requires water filtration
    - requires initial water source
    
    can add fish, seaplants
    - these buff productivity of crops
    - fish adds food source
    
    slower output of fish than a hatchery
    faster output of crops than standard farm
    
    unlike hatchery, does NOT increase foodborne illness or genetic modification of fish
    
    direct conversion: fish hatchery, aquarium
    secondary conversion: standard farm
        
    scholars stationed in the aquaponics building can study crop genetics, 
    '''
    def __init__():
        return
    
class scholar:
    '''
    scholars can be stationed at various buildings or locations in the community
    their station and speciality will influence the type of advancements they can make
    
    'insight' or 'inspiration': impacts the chance of making an advancement
        - e.g. astronomy scholar stationed at the aquarium gains inspiration and 
               is more likely to make an advancement when returning to the observatory
               
    'advancement': can be a new technology, or a new output from a technology,
                   or increase the attributes of a thing 
        - e.g. advancement by an agrarian scholar at the aquaponics station might 
               be a genetic modification that increases productivity of soy, this 
               would impact all soy production regardless of the building
        - e.g. advancement by a marine biologist scholar at the aquaponics station might
               be on evolution and reduce chances of disease
        
        - advancements can be shared with other communities in an exchange or as a gift
        
    - interdisciplinary scholars can gain 'insight' or 'inspiration' from visiting stations
      outside of their specialty

    - scholars stationed within their specialty can make 'advancements' 
    '''
    def __init__():
        return
    
    