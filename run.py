from src.micro_center_scraper.price_checker import PriceChecker


def main():
    PriceChecker().search()

if __name__ == '__main__':

    try:
        main()     
    except Exception as e:
        print(e)
