from datetime import datetime
import os
from openai import OpenAI



# GPT Call
def gptCall():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    

    wochentage = {
        0: "Montag",
        1: "Dienstag",
        2: "Mittwoch",
        3: "Donnerstag",
        4: "Freitag",
        5: "Samstag",
        6: "Sonntag"
    }

    now = datetime.now()
    datum = now.strftime("%d.%m.%Y")
    wochentag = wochentage[now.weekday()]  # ✅ nur EIN Wochentag, nicht das ganze Dict

    systemmessage = f"""
    Heute ist der {datum} ({wochentag}). Überlege dir, ob an diesem Tag ein besonderes Ereignis, ein Feiertag oder eine typische Stimmung vorliegt (z. B. Ostersonntag, Wochenbeginn, Wochenende usw.).

    Verfasse dann eine besonders kreative, motivierende Nachricht, die perfekt zu diesem Tag passt – so, als würde sie ein charismatischer Coach oder ein weiser Mensch wie Gandhi oder Tony Robbins persönlich sagen.

    Die Botschaft soll:
    – inspirierend, mutig und positiv sein  
    – je nach Anlass ruhig, energetisch oder feierlich klingen  
    – maximal 2–3 Sätze lang sein  
    – passende Emojis enthalten (aber nicht übertreiben)  
    – gelegentlich ein kurzes Zitat enthalten (z. B. von Gandhi, Steve Jobs, Maya Angelou, Seneca etc.)  
    – niemals generisch oder langweilig sein

    Vermeide Wiederholungen. Schreib so, dass man es gerne weiterleiten oder als Tagesmotto behalten würde.
    """

    systemmessage_filled = systemmessage.format(datum=datum, wochentag=wochentag)


    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "Du bist ein inspirierender Coach."},
        {"role": "user", "content": systemmessage}
    ],
    max_tokens=1000,
    temperature=0.9)

    return response.choices[0].message.content.strip()

print(gptCall())