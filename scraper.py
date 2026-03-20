import requests
    from bs4 import BeautifulSoup
    import json
    import datetime
    
    TRACKS = {'OP': 'Oaklawn Park', 'FG': 'Fair Grounds'}
    def scrape_entries():
        results = []
        headers = {'User-Agent': 'Mozilla/5.0'}
        for code, name in TRACKS.items():
            url = f'https://www.equibase.com/static/entry/{code}index.html'
            try:
                r = requests.get(url, headers=headers, timeout=10)
                if r.status_code == 200:
                    results.append({'track': name, 'status': 'Data fetched', 'date': str(datetime.date.today())})
                else:
                    results.append({'track': name, 'status': f'Failed: {r.status_code}'})
            except Exception as e:
                results.append({'track': name, 'status': f'Error: {str(e)}'})
        
        with open('data.json', 'w') as f:
            json.dump(results, f, indent=4)
    
    if __name__ == '__main__':
        scrape_entries()
    
