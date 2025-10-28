import requests
import re

WIKI_API_SUMMARY = "https://en.wikipedia.org/api/rest_v1/page/summary/"
HEADERS = {
    "User-Agent": "OpenSourceRemedyApp/1.0 (contact: example@example.com)"
}

def fetch_remedy(topic):
    topic_wiki = topic.strip().replace(" ", "_")
    url = WIKI_API_SUMMARY + topic_wiki
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            summary = data.get("extract", "")
            treatment = ""
            for sent in re.split(r'(?<=[.!?]) +', summary):
                if re.search(r"\b(treatment|remedy|management|cure|recover)\b", sent, re.I):
                    treatment += sent + "\n"
            if not treatment:
                treatment = summary[:350] + "..." if summary else "No information found."
            return treatment
        elif response.status_code == 404:
            return "Sorry, no Wikipedia page found for this illness."
        else:
            return f"Error fetching data: HTTP {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Enter a disease or illness:")
    illness = input().strip()
    if not illness:
        print("Input Required: Please enter a disease or illness.")
        return
    remedy = fetch_remedy(illness)
    print("\nInformation for '{}':\n".format(illness))
    print(remedy)

if __name__ == "__main__":
    main()
