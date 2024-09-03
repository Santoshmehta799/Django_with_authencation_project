import requests
# from city_state_app.models import State, City, Country
from city_state_app.models import State, City, Country
from django.http import JsonResponse
from django.core.management.base import BaseCommand
from rest_framework.response import Response
from requests.exceptions import RequestException

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        county_obj = Country.objects.get(name="INDIA")
        url = "https://countriesnow.space/api/v0.1/countries/states"
        payload = {
            "country": "India"
        }
        try:

            response = requests.post(url, json=payload)
            response.raise_for_status()
    
        # if response.status_code == 200:
            data = response.json()
            states = data.get('data', {}).get('states', [])
            for state in states:
                state_obj,created = State.objects.get_or_create(
                    country=county_obj,
                    name=state.get('name'),
                    state_code=state.get('state_code')
                )
                if created:
                    print(f"Added new state: {state_obj.name}")
                else:
                    print(f"State already exists: {state_obj.name}")
        except RequestException as e:
            self.stdout.write(self.style.ERROR(f"Request failed=>: {e}"))
        except ValueError:
            self.stdout.write(self.style.ERROR("Invalid JSON response received"))
            
        state_objs = State.objects.all()
        for state in state_objs:
            url="https://countriesnow.space/api/v0.1/countries/state/cities"
            payload ={ 
                "country": f"{county_obj}",
                "state": f"{state}"
            }
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    cities = data.get('data')

                    for city in cities:
                        city_obj,created = City.objects.get_or_create(
                            state=state,
                            name=city,
                        )
                        if created:
                            print(f"Added new city: {city_obj.name}")
                        else:
                            print(f"city already exists: {city_obj.name}")
            except RequestException as e:
                self.stdout.write(self.style.ERROR(f"Request failed=>: {e}"))
            except ValueError:
                self.stdout.write(self.style.ERROR("Invalid JSON response received"))
    






