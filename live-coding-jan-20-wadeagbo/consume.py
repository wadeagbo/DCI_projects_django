import requests


r = requests.get("https://ohmanda.com/api/horoscope/cancer", auth=("user", "pass"))

print(r.json())

output_dic = {
    "sign": "cancer",
    "date": "2023-01-20",
    "horoscope": "Aquarius season kicks off this morning, dear Crab, invigorating you to embrace the unknown, mix up your routines, and seek to evolve throughout the next several weeks. These vibes are all about personal transformation, making it important that you lean into change. You'll also notice your relationships growing, as you connect more deeply with the ones you love. Keep your eyes peeled for signs and synchronicities as the Capricorn moon aligns with Uranus, ushering in messages from beyond the veil. A mystical energy will take hold later tonight when Luna blows a kiss to Neptune, marking the perfect occasion to meditate or lean into your spiritual side.",
}

# print(r.status_code)
# print()
# print(r.headers['content-type'])
# print()
# print(r.encoding)
# print()
# print(r.text)
