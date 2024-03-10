from flask import Flask
from Src.Storage.storage import storage
from Src.Logics.convert_factory import convert_factory


def get_storage_keys(cls):
    keys = []
    methods = [getattr(cls, method) for method in dir(cls) if callable(getattr(cls, method))]
    for method in methods:
        if method.__name__.endswith("_key") and callable(method):
            keys.append(method())
    return keys

app = Flask(__name__)
@app.route("/api/report/<storage_key>/<format>", methods=['GET'])
def get_report(storage_key: str, format: str):
    if format.lower() not in ['markdown', 'csv', 'json']:
        response_data = app.response_class(
        response = f" Такого формата не существует! {storage_key}",
        status = 500,
        mimetype = "application/text"
        )
        return response_data
    
    keys = get_storage_keys(storage)
    if storage_key not in keys:
        response_data = app.response_class(
        response = f" Такого ключа не существует! {storage_key}",
        status = 500,
        mimetype = "application/text"
        )
        return response_data

    response_data = app.response_class(
        response = f" ключ {convert_factory(format).convert()}",
        status = 200,
        mimetype = f"application/{format}"
    )

    return response_data



if __name__ == "__main__":
    app.run(debug=True)

