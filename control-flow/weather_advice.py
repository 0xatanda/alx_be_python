user = input("What's the weather like today? (sunny/rainy/cold): ")

match user:
    case _ if user == "sunny":
        print("Wear a t-shirt and sunglasses")
    case _ if user == "rainy":
        print("Don't forget your umbrella and a raincoat")
    case _ if user == "cold":
        print("Make sure to wear a warm coat and a scarf")
    case _ :
        print("Sorry, I don't have recommendations for this weather")