#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:40:58 2026

@author: admin-dylmiley
"""
import numpy as np


def choose(n):
    """
    An user input based choice selector. 
    argument 'n' sets the number of possible choices
    does not move forward until a valid choice is made (e.g. 1, 2, or 3 in a 3 choice scenario)
    """
    y = True
    while y == True:
        x = input("choice: ")
        try: 
            int(x);
            for i in range(n):
                if int(x) == i+1:
                    y = False
        except:
            y = True
    return int(x)

def make_project_proposal(n_committed, n_needed, proj_type, res_req):
    """
    a half baked idea for how to implement planning new things
    I think the idea is that it could be applied to any type of project and that we would need to define what types of projects there are:
    project types: (?)
    - Building 
    - Resource 
    - Science 
    - Art 

    Once you create a project proposal, that goes into convincing people to collaborate??
    Would be called during dialogue with other community members and influence social interaction?
    """
    project_proposal = {
        'people committed': n_committed,
        'people needed': n_needed, 
        'project type':  proj_type,
        'resource requirement': res_req
        }
    return project_proposal


def dialogue_navigator(n_folks, community_members, friend = 2, appeal = 4):
    """
    This turned into specifically being for asking people for help
    Is only useful to demonstrate an idea of
    - enter into dialgoue with some amount of people, and there is an outcome of that dialogue that affects the game
    --- RNG values are just used to suggest that outcomes can change and should depend on the scenario
    """
    rng = np.random.default_rng()

    folks = []
    for key in community_members:
        folks.append(key)
    folks = rng.choice(folks, size = n_folks, replace = False)
    
    for person in folks:
        willingness = rng.choice(np.arange(friend, appeal))
        availability = rng.choice(np.arange(4))
        hours_helpful = willingness * availability
        print(person, 'can help you for', np.around(hours_helpful,1), 'hours tomorrow.')
    
    return 
    

def propose_project(project_proposal, community_members, resources):
    """
    This is really the engine of this idea
    people in the community can help you with your projects, 
    your approach to getting help will affect the outcome 

    the current two modes of operation are:
    - BE CASUAL: enter into small talk and convince ppl one on one
    --- current idea is that 1-on-1 convos are an easier way to get guaranteed success, though you cannot reach as many people
    --- outcomes tend to be a few people helping out for most of the day
    - BE BOLD: give a speech at the town center trying to convice ppl to help
    --- asking everyone has reduced impact since its less personal but it can be rewarding, 
    --- outcomes tend to range from nobody buys in to everyone buys in a little bit
    """
    rng = np.random.default_rng()
    choices = ['BE CASUAL', 'BE BOLD']
    punctuation = ['.', '!']
    print('you gather around the central hearthfire and look upon those around you')
    print('thinking on tomorrow\'s plans, you decide to ')
    print('1.) ' + choices[0])
    print('2.) ' + choices[1])
    x = choose(2)
    print('you decide to ' + choices[x-1] + punctuation[x-1])
    
    if x == 1:
        print('you bring up your project idea for tomorrow in small talk and manage to')
        n_folks = rng.integers(min(3, len(community_members))) + 1
        print('gather the attention of', n_folks, 'of your friends')
        dialogue_navigator(n_folks, community_members)
        
    else:
        print('you stand up and announce your idea to the crowd around the fire')
        n_folks = len(community_members)
        dialogue_navigator(n_folks, community_members, friend = 0, appeal = 2)

        
    return
    
community_members = {
    'Bob': 'Builder',
    'Felix': 'Handyman',
    'Dora': 'Explorer',
    'Bill': 'Scientist',
    'George': 'Botanist',
    'Karla': 'Teacher'
    }

propose_project(0, community_members, 0)
