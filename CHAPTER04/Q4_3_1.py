def concat_words(*args, separator='.'):
    '''任意の数の位置引数と区切り文字を受け取り、区切り文字でつなげる'''
    return separator,join(args)

concat_words('a', 'b', 'c', 'd', separator='_')
