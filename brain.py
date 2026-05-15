import wikipedia
from flask import Flask, request, jsonify

app = Flask(__name__)

# Unaweza kuweka 'en' kwa Kiingereza au 'sw' kwa Kiswahili
wikipedia.set_lang("sw")

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    swali = user_data.get("message", "")
    
    try:
        # Mr. Brain anatafuta muhtasari wa swali lako yeye mwenyewe
        jibu_logic = wikipedia.summary(swali, sentences=3)
        bot_response = jibu_logic
    except wikipedia.exceptions.DisambiguationError as e:
        bot_response = f"Kuna maana nyingi za '{swali}'. Hebu fafanua kidogo unachotaka."
    except wikipedia.exceptions.PageError:
        bot_response = f"Samahani, nimejaribu kutafuta kuhusu '{swali}' lakini sijapata jibu bado."
    except Exception:
        bot_response = "Nimepata hitilafu wakati wa kutafuta. Jaribu tena baada ya muda."

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)

