from flask import Flask, render_template
import pandas as pd


def main():
    """A simple API containing 3 endpoints for retrieving
    different types of weather data for various locations in
    the UK
    """
    app = Flask("__name__")

    df = pd.read_csv("data/stations.txt", skiprows=17)

    stations = df[["STAID", "STANAME                                 "]]

    # """@app.route decorator applies to the home() function. Means when so
    # when the url is accessed, the decorated function will be executed"""
    @app.route("/")
    def home():
        return render_template("weather.html", data=stations.to_html())

    # """The string found inside the app.route decorator defines the address
    # that users will go to in order to retrieve or upload data from your service (API)
    # """
    @app.route("/api/v1/<station>/<date>")
    def station_date(station, date):
        station_file = "data/TG_STAID" + str(station).zfill(6) + ".txt"
        df = pd.read_csv(station_file, skiprows=20, parse_dates=["    DATE"])
        temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
        return {"station": station, "date": date, "temperature": temperature}

    @app.route("/api/v1/<station>")
    def station_all(station):
        station_file = "data/TG_STAID" + str(station).zfill(6) + ".txt"
        df = pd.read_csv(station_file, skiprows=20, parse_dates=["    DATE"])
        result = df.to_dict(orient="record")
        return result

    @app.route("/api/v1/annual/<station>/<year>")
    def yearly(station, year):
        year_file = "data/TG_STAID" + str(station).zfill(6) + ".txt"
        df = pd.read_csv(year_file, skiprows=20)
        df["    DATE"] = df["    DATE"].astype(str)
        result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
        return result

    app.run(debug=True)


if __name__ == "__main__":
    main()
