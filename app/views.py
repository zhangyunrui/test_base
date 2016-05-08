# -*- coding: utf-8 -*-
import json
from django.http.response import HttpResponse
from django.shortcuts import render


def get_name(request):
    test_name = None.split(',')
    links = {'Java': ['hhhhhh'], 'Python': ['hhhhhh'], '产品经理': ['hhhhhh'], 'drupal': [], '嵌入式': [], 'iOS': [],
             '动画制作': ['hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh'], }

    sorts = {
        '1': {'name': '产品运营', 'color': '#F193A2', 'categories': {'产品经理': ''}},
        '2': {'name': '设计', 'color': '#F6A479', 'categories': {'UI 设计': '', '游戏原画': ''}},
        '3': {'name': '移动开发', 'color': '#FFEA78', 'categories': {'Android': '', 'iOS': ''}},
        '4': {'name': '后台开发', 'color': '#8DCEFB', 'categories': {'Python': '', 'PHP': '', 'Java': '', 'drupal': ''}},
        '5': {'name': '前端开发', 'color': '#94AFF4', 'categories': {'Web前端': ''}},
        '6': {'name': '游戏开发', 'color': '#B091E5', 'categories': {'Cocos2d': '', 'Unity 3D': '', '动画制作': ''}},
        '7': {'name': '底层开发', 'color': '#91E5D5', 'categories': {'嵌入式': '', '物联网': ''}},
        '8': {'name': '软件测试', 'color': '#A6E591', 'categories': {'软件测试': ''}},
    }

    categories = {
        '1': '产品经理',
        '2': 'Android',
        '3': 'iOS',
        '4': 'Cocos2d',
        '5': 'Python',
        '6': '嵌入式',
        '7': 'PHP',
        '8': 'Web前端',
        '9': '物联网',
        '10': '软件测试',
        '11': '游戏原画',
        '12': 'Java',
        '13': 'Unity 3D',
        '14': 'UI 设计',
        '15': '动画制作',
        '16': 'drupal'
    }

    sorts_dicts = {}
    for sort_k, sort_v in sorts.items():
        links_dict = {}
        for link_k, link_v in links.items():
            if link_v and link_k in sort_v['categories'].keys():
                links_dict[link_k] = link_v
        if links_dict:
            ele_dict = dict(name=sort_v['name'], color=sort_v['color'], categories=links_dict)
            sorts_dicts[sort_k] = ele_dict

    return render(request, 'name.html', locals())


def save_post(request):
    return render(request, 'save_post.html', locals())


def save_post_submit(request):
    return HttpResponse(json.dumps({"status": "昵称（姓名）不能重复"}), content_type="application/json")
