def protected_input(float_flag):
    while True:
        val = input()
        try:
            if float_flag:
                val = float(val)
            else:
                val = int(val)
            return val
        except ValueError:
            if val == 'exit':
                return True
            else:
                print('Это не число')
