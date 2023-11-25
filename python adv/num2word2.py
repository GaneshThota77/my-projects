def convert(num):
    # started as grepit's version at https://stackoverflow.com/a/54002579/746054
    # large constants converted to exponential notation
    # orders of magnitude (oom) added
    # overflow message
    units = (
        "", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ",
        "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens = ("", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety ")
    oom = ('thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion',
           'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion', 'quattuordecillion',
           'quindecillion', 'sexdecillion', 'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion')

    if num < 0:
        return "minus " + convert(-num)

    if num < 20:
        return units[num]

    if num < 100:
        return tens[num // 10] + units[num % 10]

    if num < 10 ** 3:
        return units[num // 10 ** 2] + "hundred " + convert(num % 10 ** 2)

    for idx, name in enumerate(oom):
        scale = (idx + 1) * 3
        cap = scale + 3
        if num < 10 ** cap:
            return convert(num // 10 ** scale) + name + " " + convert(num % 10 ** scale)

    return "function " + convert.__name__ + " has exhausted its vocabulary"