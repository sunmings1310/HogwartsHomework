def black_wrapper(fun):
    # 捕获没找到元素的异常
    def run(*args, **kwargs):
        base_page = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            # 遍历黑名单中的元素进行处理
            for black in base_page.black_list:
                eles = base_page.finds(*black)
                # 黑名单被找到
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e
    return run