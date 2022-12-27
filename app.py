from flask import Flask, render_template, request, redirect

app = Flask(__name__)

states = {
    "MA": "Massachusetts",
    "MN": "Minnesota",
    "MT": "Montana",
    "ND": "North Dakota",
    "HI": "Hawaii",
    "ID": "Idaho",
    "WA": "Washington",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "NV": "Nevada",
    "NM": "New Mexico",
    "OR": "Oregon",
    "UT": "Utah",
    "WY": "Wyoming",
    "AR": "Arkansas",
    "IA": "Iowa",
    "KS": "Kansas",
    "MO": "Missouri",
    "NE": "Nebraska",
    "OK": "Oklahoma",
    "SD": "South Dakota",
    "LA": "Louisiana",
    "TX": "Texas",
    "CT": "Connecticut",
    "NH": "New Hampshire",
    "RI": "Rhode Island",
    "VT": "Vermont",
    "AL": "Alabama",
    "FL": "Florida",
    "GA": "Georgia",
    "MS": "Mississippi",
    "SC": "South Carolina",
    "IL": "Illinois",
    "IN": "Indiana",
    "KY": "Kentucky",
    "NC": "North Carolina",
    "OH": "Ohio",
    "TN": "Tennessee",
    "VA": "Virginia",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "DE": "Delaware",
    "DC": "District of Columbia",
    "MD": "Maryland",
    "NJ": "New Jersey",
    "NY": "New York",
    "PA": "Pennsylvania",
    "ME": "Maine",
    "MI": "Michigan",
    "AK": "Alaska"
}


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/modal")
def modal():
    state = request.args.get('state')
    if not state or state not in states.values():
        return redirect("/")

    return render_template("modal.html", state=state)