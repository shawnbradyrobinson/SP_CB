#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:40:58 2026

@author: admin-dylmiley
"""
import numpy as np


def choose(n):
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
    project_proposal = {
        'people committed': n_committed,
        'people needed': n_needed, 
        'project type':  proj_type,
        'resource requirement': res_req
        }
    return project_proposal


def dialogue_navigator(n_folks, community_members, friend = 2, appeal = 4):
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