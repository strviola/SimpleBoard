'''
Created on 2013/09/09

@author: SuzukiRyota
'''

import logging
from . import backends


def str_length(var_name):
    '''
    このデコレータが付けられたview関数は、入力パラメタの文字列としての長さを検査される。
    他の入力より優位に長い/短い長さの入力は、警告を発し、ユーザーを特定することができる。
    '''
    
    # 判定に用いる閾値 平均からの差がこの値を超える確率を算出
    THRESHOLD = 20
    
    def decorator(view_func):
        def wrapper(request):
            # リクエストからデコレータの引数で指定されたものを取得
            # POST, GET どちらにも対応
            str_input = request.REQUEST[var_name]
            logging.warning('%s: %s' % (var_name, request.REQUEST[var_name]))
            
            # 過去のサンプルを取得
            str_list = backends.read_name(var_name)
            if len(str_list) == 0:
                # too few samples
                logging.warning('Too few samples')
                backends.stack(var_name, str_input)
                return view_func(request)

            # 文字列のリストを文字数の長さの整数リストに変換
            int_list = [len(s) for s in str_list]
            
            # 平均と分散を取得
            mu = backends.mean(int_list)
            sigma2 = backends.variance(int_list)
            dev = backends.deviation(int_list)
            logging.warning('mean = %f, variance = %f, d = %f'
                            % (mu, sigma2, dev))
            
            # 閾値 <= 分散であれば、計算式に意味が無いことを警告
            if THRESHOLD <= dev:
                logging.warning('This threshold will not make sense.')
            
            # チェビシェフの不等式により、入力が閾値から外れる確率を計算
            probability = sigma2 / pow(THRESHOLD, 2)
            logging.warning('p(|x-mu| > |l-mu|) == %f', probability)
            
            # TODO: 条件に該当した時に、確率をAnomaly Scoreとして返す
            if abs(len(str_input) - mu) > THRESHOLD:
                logging.warning('Rare case (probability: %f) has occurred'
                                % probability)
            
            # 入力をファイルに保存
            backends.stack(var_name, str_input)
            
            return view_func(request)
            
        return wrapper
    
    return decorator
