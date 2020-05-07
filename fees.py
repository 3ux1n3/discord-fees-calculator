import locale


locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


def get_fees(n):
    return {
        'Ebay ': ebay(n),
        'Goat ': goat(n),
        'StockX  ': stockx(n)
    }


def paypal(n):
    return (0.029 * n) + 0.3


def ebay(n):
    return 0.1 * n + paypal(n - (0.1*n))


def goat(n):
    return 0.095 * n + paypal(n - 0.095*n)


def stockx(n):
    return 0.095 * n


def to_money(n):
    return locale.currency(n, grouping=True)
