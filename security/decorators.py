# -*- coding: utf-8 -*-

'''
Created on 2013/09/09

@author: SuzukiRyota
'''

import logging
from . import backends

MIN_SAMPLE = 10


def str_length(var_name):
    '''
    このデコレータが付けられたview関数は、入力パラメタの文字列としての長さを検査される。
    他の入力より優位に長い/短い長さの入力は、警告を発し、ユーザーを特定することができる。
    '''
    
    # 判定に用いる閾値 この値を超える
    THRESHOLD_LENGTH = 10
    
    def decorator(view_func):
        def wrapper(request):
            # リクエストからデコレータの引数で指定されたものを取得
            # POST, GET どちらにも対応
            str_value = request.REQUEST[var_name]
            logging.warning('%s: %s' % (var_name, request.REQUEST[var_name]))
            
            # 過去のサンプルを取得
            str_list = backends.read_name(var_name)
            if len(str_list) == 0:
                # too few samples
                logging.warning('Too few samples')
                backends.stack(var_name, str_value)
                return view_func(request)

            # 文字列のリストを文字数の長さの整数リストに変換
            int_list = [len(s) for s in str_list]
            
            # 平均と分散を取得
            mu = backends.mean(int_list)
            sigma2 = backends.variance(int_list)
            logging.warning('mean = %f, variance = %f' % (mu, sigma2))
            
            # チェビシェフの不等式により、入力が閾値から外れる確率を計算
            probability = sigma2 / pow(THRESHOLD_LENGTH - mu, 2)
            logging.warning('p(|x-mu| > |l-mu|) == %f', probability)
            
            # 入力をファイルに保存
            backends.stack(var_name, str_value)
            backends.dump()
            
            return view_func(request)
            
        return wrapper
    
    return decorator
