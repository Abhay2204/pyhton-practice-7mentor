newspaper = ["Times of India", "Hindustan Times", "Dainik Bhaskar", "The Indian Express", "Navbharat Times"]

print("Seller's Stock:", newspaper)


ias_basket = newspaper.copy()

print("IAS Officer's Basket:", ias_basket)


ias_basket.remove("Times of India")

print("Basket after removing Times of India:", ias_basket)
