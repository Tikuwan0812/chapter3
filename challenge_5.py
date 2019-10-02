def henkan(mozi):
    try:
        mozi = float(mozi)
        return mozi
    except ValueError:
        print('ValueError!')

mozi = input('何か数字を入力してください')
print(henkan(mozi))
