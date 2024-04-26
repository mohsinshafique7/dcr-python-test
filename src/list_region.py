from db import Country
from collections import defaultdict
import json
class ListRegion:
    
    def run(self):
        region_stats = defaultdict(lambda: {'number_countries': 0, 'total_population': 0})
        try:
            for i, country in enumerate(Country.list_all()):
                if i != 0:
                    region =  list(country.data.values())[-1] 
                    region_stats[region]['number_countries'] += 1
                    region_stats[region]['total_population'] += list(country.data.values())[-4]
            result = {
                "regions": [
                    {
                        "name": region,
                        "number_countries": stats["number_countries"],
                        "total_population": stats["total_population"]
                    } 
                    for region, stats in region_stats.items()
                ]
            }
            result_json = json.dumps(result, indent=4)
            print(result_json)
            return result_json
        except Exception as e:
             print("An error occurred:", e)
if __name__ == "__main__":
    ListRegion().run()
