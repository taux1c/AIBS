
# The base urls of the site.
base_urls:list['str'] = [
    'https://anonib.al',
    'https://anonib.pk',
]

# The headers used for requests.
headers: dict[str:str] = {
    "authority": "anonib.al",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "captchaid=653ef276f7546e9342c1dbc20GZBeDuDBgmYPF26w5RZXqo/3zDe9r6POCx8KTIPnKuO4cwBbPdl03EZUJxlEsLf0N4kFJrw9JvXqM+UIutijw==; captchaexpiration=Mon, 30 Oct 2023 00:02:58 GMT",
    "if-modified-since": "Sun, 29 Oct 2023 23:15:01 GMT",
    "sec-ch-ua": '^\^"Google Chrome^\^";v=^\^"117^\^", ^\^"Not;A=Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"117^\^"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '^\^"Windows^\^"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}

# The timeout used for requests.
timeout: int = 120

# Folder to save profiles in.
profiles_folder: str = 'profiles'

# Letter subs is used to correct messages. The key is replaced with the value.
letter_subs: dict[str:str] = {
    "0":"o",
    "7":"t",
    "4":"h",
    "1":"l",
    "!":"i",
    "3":"e",
    "@":"a",
    "<":"",
    ">":"",
    "$":"s",
}

chars_replace: dict[str:str] = {

    "?":"",
    "$":"",
    "#":"",
    "*":"",
    "&":"",
    "(":"",
    ")":"",

}

# Set the max message length to use in names and folder names.
max_message_len: int = 200

# All categories

all_categories: list[str] = [

    'ak',
    'al',
    'ar',
    'az',
    'ca',
    'co',
    'ct',
    'dc',
    'de',
    'fl',
    'ga',
    'hi',
    'ia',
    'id',
    'il',
    'in',
    'ks',
    'ky',
    'la',
    'ma',
    'md',
    'me',
    'mi',
    'mn',
    'mo',
    'ms',
    'mt',
    'nc',
    'nd',
    'ne',
    'nh',
    'nj',
    'nm',
    'nv',
    'ny',
    'oh',
    'ok',
    'or',
    'pa',
    'ri',
    'sc',
    'sd',
    'tn',
    'tx',
    'ut',
    'va',
    'vt',
    'wa',
    'wi',
    'wv',
    'wy',

    # Other Cats

    "a",
    "an",
    "ass",
    "azn",
    "b",
    "bdsm",
    "bj",
    "bt",
    "c",
    "cam",
    "cb",
    "cf",
    "ci",
    "coe",
    "cosp",
    "cut",
    "cw",
    "eb",
    "et",
    "es",
    "fa",
    "fe",
    "gf",
    "gif",
    "gin",
    "hc",
    "he",
    "hy",
    "les",
    "lt",
    "mg",
    "mil",
    "milf",
    "mod",
    "mu",
    "pan",
    "paycam",
    "pi",
    "pl",
    "pr",
    "red",
    "soc",
    "tat",
    "tblr",
    "tr",
    "tt",
    "v",
    "wc",
    "ygwbt",
    "yt",
    "au",
    "can",
    "ger",
    "uk",
    "rmw",
    "btc",
    "pol"

]
