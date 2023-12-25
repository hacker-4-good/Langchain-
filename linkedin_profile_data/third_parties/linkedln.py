# Proxycurl api key = iU3iADNLfZh5a0myZ_TjEw
# Gist = https://gist.githubusercontent.com/hacker-4-good/b359beeafab2240775eb4adf4785bd46/raw/eb7b9093aec008ce5505db38c8006b5615c2d938/eden-marco.json
import os
import requests


def scrape_linkedln_profile(linkedin_profile_url: str):
    """
    scrape information from linkedln profiles,
    manually scrape the information from the linkedln profile
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):  # type: ignore
            group_dict.pop("profile_pic_url")

    return data
