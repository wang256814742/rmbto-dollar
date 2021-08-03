# coding；utf-8

print('************欢迎使用货币转换服务****************')
while True:
    choose = input('请您选择需要的服务: \n 1.人民币转换美元 \n 2.美元转换人民币 \n 3. 人民币转换欧元 \n 4.结束程序\n')
    print('~~~~~~~~~~~~~~~~~~~~~~')
    if choose == '1':

        while True:
            try:
                print('欢迎使用人民币转换美元服务')
                choose = float(input('请您输入需要转换的人民币金额: '))
                print(f'你需要转换的人民币为: {choose}')
                jiner = (choose * 0.14 )
                print(f'兑换成美元是：{jiner}＄')
                print('==========================')# 兑换成美元
            except:
                print('请输入数字')
            break

    elif choose == '2':

        while True:
            try:
                print('欢迎使用美元转换人民币服务')
                choose = float(input('请您输入需要转换的美元金额: '))
                print(f'你需要转换的人民币为: {choose}')
                rmb = (choose * 7.06)
                print(f'兑换成人民币是: {rmb} ￥')
                print('==========================')# 兑换成人民币
            except:
                print('请输入数字')
            break
    elif choose == '3' :

        while True:
            try:
                print('欢迎使用人民币转换欧元服务')
                choose = float(input('请您输入需要转换的人民币金额: '))
                print(f'你需要转换的人民币为: {choose}')
                rmb = (choose * 0.12)
                print(f'兑换成欧元是: {rmb} €')# 转换成欧元的
                print('==========================')
            except:
                print('请输入数字')
            break
    elif choose == '4':
        print('程序正常结束了')
        break




