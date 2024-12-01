sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["linkedin", "https://www.linkedin.com"],
            ["github", "https://www.github.com"],
            ["instagram", "https://www.instagram.com"],
            ["x", "https://www.x.com"],
            ["twitter", "https://www.twitter.com"],
            ["facebook", "https://www.facebook.com"],
            ["gmail", "https://www.gmail.com"],
            ["mail", "https://www.gmail.com"],
            ["hacker rank", "https://www.hackerrank.com"],
            ["geeks for geeks", "https://www.geeksforgeeks.org"],  # Fixed typo
            ["gfg", "https://www.geeksforgeeks.org"],
            ["chatgpt", "https://chat.openai.com"],  # Updated link
            ["chat gpt", "https://chat.openai.com"],
            ["openai", "https://www.openai.com"],
            ["open ai", "https://www.openai.com"],
            ["codeforces", "https://codeforces.com"],  # Popular competitive siteming platform
            ["codechef", "https://www.codechef.com"],  # Competitive siteming
            ["leetcode", "https://leetcode.com"],  # Problem-solving platform
            ["stackoverflow", "https://stackoverflow.com"],  # siteming Q&A site
            ["coursera", "https://www.coursera.org"],  # Online courses
            ["khan academy", "https://www.khanacademy.org"],  # Learning platform
            ["physics wallah", "https://www.pw.live"],
            ["physics wallah", "https://www.pw.live"],
            ["edx", "https://www.edx.org"],  # Free online courses
            ["ndtv", "https://www.ndtv.com"],  # For news
            ["weather", "https://weather.com"],  # Weather updates
            ["amazon", "https://www.amazon.com"],  # Online shopping
            ["flipkart", "https://www.flipkart.com"],  # Online shopping (India)
            ["netflix", "https://www.netflix.com"],  # Entertainment
            ["spotify", "https://www.spotify.com"],  # Music streaming
            ["zomato", "https://www.zomato.com"],  # Food delivery
            ["swiggy", "https://www.swiggy.com"],  # Food delivery
            ["quora", "https://www.quora.com"],  # Knowledge sharing
            ["duckduckgo", "https://duckduckgo.com"],  # Privacy-focused search engine
            # Google Apps
            ["google drive", "https://drive.google.com"],
            ["google docs", "https://docs.google.com"],
            ["google sheets", "https://sheets.google.com"],
            ["google slides", "https://slides.google.com"],
            ["google calendar", "https://calendar.google.com"],
            ["google meet", "https://meet.google.com"],
            ["google photos", "https://photos.google.com"],
            ["google keep", "https://keep.google.com"],
            ["google maps", "https://maps.google.com"],
            ["google play", "https://play.google.com"],
            ["google translate", "https://translate.google.com"],
            ["google news", "https://news.google.com"],
            ["google classroom", "https://classroom.google.com"],
            ["google sites", "https://sites.google.com"],
            ["google analytics", "https://analytics.google.com"]
        ]
def open_site(query):
    import webbrowser
    from speech import say
    for site in sites:
        try:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                say(f"{site[0]} Opened Sir...")
                        
        except Exception as e:
            print("Error : ",e)
            say("An error oucurred in opening {site[0]} sir...")
