# -*- coding: utf-8 -*-
import json
from django.http.response import HttpResponse
from django.shortcuts import render
import operator


def get_name(request):
    links = {'Java': ['hhhhhh'], 'Python': ['hhhhhh'], '产品经理': ['hhhhhh'], 'drupal': [], '嵌入式': [], 'iOS': [],
             '动画制作': ['hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh',
                      'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh', 'hhhhhh'], }

    # sorts = {
    #     '产品运营': {'index': '1', 'color': '#F193A2', 'categories': {'产品经理': ''}},
    #     '设计': {'index': '2', 'color': '#F6A479', 'categories': {'UI 设计': '', '游戏原画': ''}},
    #     '移动开发': {'index': '3', 'color': '#FFEA78', 'categories': {'Android': '', 'iOS': ''}},
    #     '后台开发': {'index': '4', 'color': '#8DCEFB', 'categories': {'Python': '', 'PHP': '', 'Java': '', 'drupal': ''}},
    #     '前端开发': {'index': '5', 'color': '#94AFF4', 'categories': {'Web前端': ''}},
    #     '游戏开发': {'index': '6', 'color': '#B091E5', 'categories': {'Cocos2d': '', 'Unity 3D': '', '动画制作': ''}},
    #     '底层开发': {'index': '7', 'color': '#91E5D5', 'categories': {'嵌入式': '', '物联网': ''}},
    #     '软件测试': {'index': '8', 'color': '#A6E591', 'categories': {'软件测试': ''}},
    # }

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
    # for sort_k, sort_v in sorts.items():
    #     categories = sort_v['categories']
    #     for link_k, link_v in links.items():
    #         if link_k in categories.keys():
    #             sorts[sort_k]['categories'][link_k] = link_v

    sorts_dicts = {}
    for sort_k, sort_v in sorts.items():
        links_dict = {}
        for link_k, link_v in links.items():
            if link_v and link_k in sort_v['categories'].keys():
                links_dict[link_k] = link_v
        if links_dict:
            ele_dict = dict(name=sort_v['name'], color=sort_v['color'], categories=links_dict)
            sorts_dicts[sort_k] = ele_dict
    # sorts_dicts = sorted(sorts_dicts.iteritems(), reverse=True)

    return render(request, 'name.html', locals())


def save_post(request):
    return render(request, 'save_post.html', locals())


def save_post_submit(request):
    return HttpResponse(json.dumps({"status": "昵称（姓名）不能重复"}), content_type="application/json")
