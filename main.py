def reverse_string():
    print("文字列逆順プログラムへようこそ！")
    
    user_input = input("文字列を入力してください: ")
    reversed_string = user_input[::-1]
    
    print(f"逆順にすると: {reversed_string}")

reverse_string()
