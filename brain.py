from flask import Flask, request, jsonify

app = Flask(__name__)

# Hii ndiyo "Akili" ya API yako (Database ya majibu)
AKILI_YANGU = {
    "habari": "Salama kabisa! Mimi ni Mr. Brain, API yako binafsi.",
    "mambo": "Safi sana, K D Labs iko kazini. Unataka kutengeneza nini leo?",
    "ujasiriamali": "Ujasiriamali ni uthubutu. Kumbuka: 'Wazo bila vitendo ni ndoto tu'.",
    "scania": "Scania ni mashine imara! Unataka kujua kuhusu injini gani?",
    "vfx": "VFX ni sanaa ya ajabu. Unaweza kutumia Python kutengeneza filters zako mwenyewe!"
}

@app.route('/')
def home():
    return jsonify({"message": "Mr. Brain Custom API is Online", "owner": "K D Labs"})

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    # Tunachukua ujumbe na kuuweka katika herufi ndogo
    ujumbe = user_data.get("message", "").lower()
    
    # API yako inatafuta jibu kwenye akili uliyoitengeneza
    jibu = "Samahani, hapo sijaelewa. Unaweza kunifundisha zaidi?"
    
    for neno, maelezo in AKILI_YANGU.items():
        if neno in ujumbe:
            jibu = maelezo
            break
            
    return jsonify({"response": jibu})

if __name__ == '__main__':
    app.run(debug=True)
